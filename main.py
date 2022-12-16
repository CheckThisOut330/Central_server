import time
import requests
from Recognizer import Recognizer

class Main:
    def __init__(self):
        self.cam_ip = {"1": "192.168.15.89",
                       "2": "192.168.15.204"}
        self.server_link = "http://119.63.246.253:8000"

    def run(self):
        while True:
            video_class = Recognizer()
            video_class.roomIp = self.cam_ip

            result = video_class.run(False)
            print(result)

            for key, value in result.items():
                requests.post(f"{self.server_link}/api/", json={"room": int(key), "count": int(value)})

            time.sleep(10)

main = Main()
main.run()