from Recognizer import Recognizer

class Main:
    def __init__(self):
        self.cam_ip = {"1": "192.168.15.89",
                       "2": "192.168.15.204"}
        self.server_link = ""

    def run(self):
        video_class = Recognizer()
        video_class.roomIp = self.cam_ip


        result = video_class.run(False)
        print(result)

main = Main()
main.run()