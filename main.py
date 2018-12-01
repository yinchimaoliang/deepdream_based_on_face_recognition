import sys
import cv2
sys.path.append("my_face_recognition")
import my_face_recognition
import my_deepdream
import get_camera_image

class take_image():
    def __init__(self):
        camera = get_camera_image.getCamera()
        camera.getImage()
        face = my_face_recognition.my_face_recognition()
        face.getImage("camera_image.jpg")
        face.getFace()
    def getDeepdream(self):
        deepdream = my_deepdream.my_deep_dream()
        deepdream.get_image("face_output.jpg")
        deepdream.deep_dream()

class load_image():
    def __init__(self,path):
        self.path = path
        print(self.path)
    def getDeepdream(self):
        deepdream = my_deepdream.my_deep_dream()
        deepdream.get_image(self.path)
        deepdream.deep_dream()