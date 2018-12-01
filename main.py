import sys
import cv2
sys.path.append("my_face_recognition")
import my_face_recognition
import my_deepdream
import get_camera_image

#相机捕捉
# camera = get_camera_image.getCamera()
# camera.getImage()
# face = my_face_recognition.my_face_recognition()
# face.getImage("camera_image.jpg")
# face.getFace();
# img = face.getFace();

# img = cv2.imread("camera_image.jpg")
deepdream = my_deepdream.my_deep_dream()
deepdream.get_image("img8.jpg")
deepdream.deep_dream()
#cv2.imshow("image",img)
#cv2.waitKey(0)
# face.getImage("8.jpg")