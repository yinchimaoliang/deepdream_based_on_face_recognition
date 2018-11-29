import sys
import cv2
sys.path.append("my_face_recognition")
import my_face_recognition
import my_deepdream
face = my_face_recognition.my_face_recognition()
face.getImage("img8.jpg")
img = face.getFace();

deepdream = my_deepdream.my_deep_dream()
deepdream.get_image("face_output.jpg")
deepdream.deep_dream()
#cv2.imshow("image",img)
#cv2.waitKey(0)
# face.getImage("8.jpg")