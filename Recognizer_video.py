from queue import Queue as Q
from mtcnn import MTCNN
import cv2

class Recognizer_video:
    def __init__(self):
        self.videos = []
        self.resultQ = Q()
        self.detector = MTCNN()
        self.color = (0, 0, 255)
        self.thickness = 2

    def setVideosFromUrls(self, urls):
        for i in enumerate(urls):
            print(f'{str(i[0])} loading...')

            self.videos.append(cv2.VideoCapture(i[1]))

            print(f'{str(i[0])} success')
    
    def setColor(self, color):
        for i in color:
            if i < 0:
                print('color value error')
                return

        self.color = color

    # 사각형 두께
    def setThickness(self,thickness):
        if thickness <= 0:
            print('thickness value error')
            return

        self.thickness = thickness

    def recognizeHumanFaces(self, roomN, drawBox) -> str:
        ret, frame = self.videos[roomN - 1].read()

        if ret is True:

            location = self.detector.detect_faces(frame)
            humansN = len(location)

            if humansN > 0 and drawBox:

                for face in location:
                    x, y, w, h = face['box']
                    cv2.rectangle(frame, (x, y), (x + w, y + h), self.color, self.thickness)

                cv2.imshow("Room" + str(roomN), frame)

            return humansN

a = Recognizer_video()
a.videos = {1: "127.0.0.1",
            2: "127.0.0.1"}