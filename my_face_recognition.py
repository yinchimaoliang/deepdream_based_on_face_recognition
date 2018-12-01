# filename : find_faces_in_picture.py
# -*- coding: utf-8 -*-
# 导入pil模块 ，可用命令安装 apt-get install python-Imaging
from PIL import Image
# 导入face_recogntion模块，可用命令安装 pip install face_recognition
import face_recognition

class my_face_recognition():
    def __init__(self):
        pass
    def getImage(self,dir):
    # 将jpg文件加载到numpy 数组中
        self.image = face_recognition.load_image_file(dir)

    # 使用默认的给予HOG模型查找图像中所有人脸
    # 这个方法已经相当准确了，但还是不如CNN模型那么准确，因为没有使用GPU加速
    # 另请参见: find_faces_in_picture_cnn.py
    def getFace(self):
        face_locations = face_recognition.face_locations(self.image)

    # 使用CNN模型
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    # 打印：我从图片中找到了 多少 张人脸
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))

    # 循环找到的所有人脸
    #     for face_location in face_locations:

                # 打印每张脸的位置信息
        face_location = face_locations[0]
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# 指定人脸的位置信息，然后显示人脸图片
        face_image = self.image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
        pil_image.save("face_output.jpg")