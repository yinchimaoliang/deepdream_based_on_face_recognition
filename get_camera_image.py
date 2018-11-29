import cv2

class getCamera():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def getImage(self):
        while(1):
            # get a frame
            ret, frame = self.cap.read()
            # show a frame
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite("camera_image.jpg", frame)
                self.cap.release()
                cv2.destroyAllWindows()
                return