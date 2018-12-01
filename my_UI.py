# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import main


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(400, 300)
        self.load_image = QtWidgets.QPushButton(Form)
        self.load_image.setGeometry(QtCore.QRect(30, 240, 93, 28))
        self.load_image.setObjectName("load_image")
        self.take_image = QtWidgets.QPushButton(Form)
        self.take_image.setGeometry(QtCore.QRect(260, 240, 93, 28))
        self.take_image.setObjectName("take_image")

        self.retranslateUi(Form)
        self.load_image.clicked.connect(Form.on_load_image_click)
        self.take_image.clicked.connect(Form.on_take_image_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def on_load_image_click(self):
        self.absolute_path = QFileDialog.getOpenFileName(self, 'Open file', '.', "jpg files (*.jpg)")
        print(self.absolute_path)
        load_image = main.load_image(self.absolute_path[0])
        load_image.getDeepdream()

    def on_take_image_click(self):
        take_image = main.take_image()
        take_image.getDeepdream()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基于人脸识别的deepdream"))
        self.load_image.setText(_translate("Form", "加载图片"))
        self.take_image.setText(_translate("Form", "拍摄图片"))

