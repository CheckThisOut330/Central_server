from mtcnn import MTCNN
import cv2
import numpy as np
from PIL import Image
import urllib

class Recognizer:
    def __init__(self):
        self.roomIp = {} # {"1": "127.0.0.1", "2": "127.0.0.1"}
        self.roomQ = {} # {"1": image, "2": image}
        self.resultQ = {} # {"1": 2, "2": 5}
        self.detector = MTCNN()
        self.locations = None
        self.saveCount = 0
        self.color = (0, 0, 255) # b, g, r
        self.thickness = 2

    def setColor(self, color):
        for i in color:
            if i < 0:
                return 'color value error'

        self.color = color
    
    def setThickness(self, thickness):
        if thickness <= 0:
            return 'thickness value error'

        self.thickness = thickness

    def addImage(self, roomN: str, image):
        self.roomQ[roomN] = image

    def recognizeHumanFaces(self, drawBox):
        image = self.roomQ.pop(list(self.roomQ)[0])
        self.locations = self.detector.detect_faces(image)

        if drawBox:
            if len(self.locations) > 0:
                image = image.copy()

                for face in self.locations:
                    x, y, w, h = face['box']
                    cv2.rectangle(image, (x, y), (x + w, y + h), self.color, self.thickness)

                cv2.imwrite(str(self.saveCount) + '.jpg', image)
                self.saveCount += 1

        return len(self.locations)

    def run(self, drawBox: bool):
        # 결과 초기화
        self.resultQ = {}

        for num in self.roomIp:
            # print(num)
            # 이미지 받아오기
            try:
                image = Image.open(urllib.request.urlopen(f"http://{self.roomIp[num]}/capture"))
                self.addImage(num, np.array(image))
            except Exception as e:
                print(e)
            else:
                # 몇명인지 체크
                facesN = self.recognizeHumanFaces(drawBox)
                self.resultQ[num] = facesN

        # 리턴
        return self.resultQ