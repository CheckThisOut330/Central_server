from queue import Queue
from mtcnn import MTCNN
import cv2

class Recognizer:
    def __init__(self) :
        self.roomQ = self.RoomQueue()
        self.resultQ = Queue()
        self.detector = MTCNN()
        self.locations = None
        self.saveCount = 0
        self.color = (0, 0, 255) # b, g, r
        self.thickness = 2

    def setColor(self, color):
        for i in color:
            if i < 0:
                print('color value error')
                return

        self.color = color
    
    def setThickness(self,thickness):
        if thickness <= 0:
            print('thickness value error')
            return

        self.thickness = thickness

    def addImage(self, roomN ,image):
        self.roomQ.add(roomN, image)
    
    def recognizeHumanFaces(self, drawBox):
        roomN, image = self.roomQ.pop()
        print(image)
        self.locations = self.detector.detect_faces(image)

        if drawBox:
            if len(self.locations) > 0:
                image = image.copy()

                for face in self.locations:
                    x,y,w,h = face['box']
                    cv2.rectangle(image,(x,y),(x+w,y+h),self.color,self.thickness)

                cv2.imwrite(str(self.saveCount) + '.jpg', image)
                self.saveCount += 1

        return len(self.locations)
    
    def run(self, drawBox):
        while True:
            sizeOfQ = self.roomQ.sizeOfQ()
            if  sizeOfQ <= 0:
                continue

            facesN = self.recognizeHumanFaces(drawBox)
            self.resultQ.put(facesN)
            
    class RoomQueue:
        def __init__(self):
            self.imageQ = Queue()
            self.roomNQ = Queue()
            self.size = 0

        def add(self, roomN, image):
            self.roomNQ.put(roomN)
            self.imageQ.put(image)
            self.size += 1

        def pop(self):
            self.size -= 1
            return self.roomNQ.get(), self.imageQ.get()
        
        def sizeOfQ(self):
            print(self.size)
            return int(self.size)