# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QCoreApplication

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1127, 879)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 40, 361, 381))
        self.label.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(610, 40, 361, 381))
        self.label_2.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 420, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 530, 100, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 640, 100, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 200, 100, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 310, 100, 60))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 750, 100, 60))
        self.pushButton_7.setObjectName("pushButton_7")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(230, 460, 361, 381))
        self.label_3.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(610, 460, 361, 381))
        self.label_4.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 430, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(760, 430, 72, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(380, 850, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(750, 850, 72, 15))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openimage)
        self.pushButton_5.clicked.connect(Form.image_crop)
        self.pushButton_6.clicked.connect(Form.change)
        self.pushButton_2.clicked.connect(Form.generate)
        self.pushButton_3.clicked.connect(Form.backchange)
        self.pushButton_4.clicked.connect(Form.save)
        self.pushButton_7.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "打开图片"))
        self.pushButton.setText(_translate("Form", "打开图片"))
        self.pushButton_2.setText(_translate("Form", "生成证件照"))
        self.pushButton_3.setText(_translate("Form", "背景转换"))
        self.pushButton_4.setText(_translate("Form", "保存图片"))
        self.pushButton_5.setText(_translate("Form", "截取"))
        self.pushButton_6.setText(_translate("Form", "轮廓提取"))
        self.pushButton_7.setText(_translate("Form", "退出"))
        self.label_5.setText(_translate("Form", "原始图像"))
        self.label_6.setText(_translate("Form", "截取图片"))
        self.label_7.setText(_translate("Form", "轮廓图像"))
        self.label_8.setText(_translate("Form", "最终图像"))

