from queue import Queue
from mtcnn import MTCNN
import cv2

class Recognizer_video:
    def __init__(self):
        self.videos = {}
        self.resultQ = Queue()
        self.detector = MTCNN()
        self.color = (0, 0, 255)
        self.thickness = 2
    
    def setColor(self, color):
        for i in color:
            if i < 0:
                return 'color value error'

        self.color = color

    # 사각형 두께
    def setThickness(self, thickness):
        if thickness <= 0:
            return 'thickness value error'

        self.thickness = thickness

    def recognizeHumanFaces(self, roomN: str, drawBox):
        ret, frame = self.videos[roomN].read()

        if ret is True:
            location = self.detector.detect_faces(frame)
            humansN = len(location)

            if humansN > 0 and drawBox:

                for face in location:
                    x, y, w, h = face['box']
                    cv2.rectangle(frame, (x, y), (x + w, y + h), self.color, self.thickness)

                cv2.imshow("Room" + str(roomN), frame)

            return humansN