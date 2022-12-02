from queue import Queue as Q
from mtcnn import MTCNN
from multiprocessing import Process, Queue
import cv2

class Recognizer_video:
    def __init__(self):
        self.videos = []
        self.resultQ = Q()
        self.detector = MTCNN()
        self.color = (0,0,255)
        self.thickness = 2

    def setVideosFromUrls(self, urls):
        index = 1
        for i in urls:
            print(str(index) + 'loading...')
            temp = cv2.VideoCapture(i)
            self.videos.append(temp)
            print(str(index) + ' success')
            index += 1
    
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

    def recognizeHumanFaces(self, roomN, drawBox):
        ret, frame = self.videos[roomN-1].read()

        if ret == True:

            location = self.detector.detect_faces(frame)
            humansN = len(location)

            if humansN > 0 and drawBox:

                for face in location:
                    x,y,w,h = face['box']
                    cv2.rectangle(frame,(x,y),(x+w,y+h),self.color,self.thickness)

                cv2.imshow("Room" + str(roomN), frame)
        
            return humansN