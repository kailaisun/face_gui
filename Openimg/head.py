# -*- coding:utf-8 -*-
"""
@author:Skl
@file:head.py
@time:2018/5/322:01
"""
from PyQt5 import QtWidgets, QtGui
import sys
from first import Ui_Form   # 导入生成first.py里生成的类
from PyQt5.QtWidgets import QFileDialog

import cv2
import numpy as np
import dlib

image_path = ' '
image_save = '../save/save.jpg'
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(
    '../data/shape_predictor_68_face_landmarks.dat')
Back_t = 0


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        # 定义槽函数

    def bule2red(self, img):
        global Back_t
        # print(type(img))
        rows, cols, channels = img.shape
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([78, 43, 46])
        upper_blue = np.array([110, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # cv2.imshow('Mask', mask)
        # 腐蚀膨胀
        erode = cv2.erode(mask, None, iterations=1)
        dilate = cv2.dilate(erode, None, iterations=1)
        # 遍历替换
        Back_t += 1
        if Back_t % 3 == 1:
            for i in range(rows):
                for j in range(cols):
                    if dilate[i, j] == 255:
                        img[i, j] = (0, 0, 255)  # BGR
        if Back_t % 3 == 2:
            for i in range(rows):
                for j in range(cols):
                    if dilate[i, j] == 255:
                        img[i, j] = (225, 166, 23)  # BGR
        if Back_t % 3 == 0:
            for i in range(rows):
                for j in range(cols):
                    if dilate[i, j] == 255:
                        img[i, j] = (255, 255, 255)  # BGR
        return img

    def openimage(self):
        global image_path
   # 打开文件路径
   # 设置文件扩展名过滤,注意用双分号间隔
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开图片", "", " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        # imgName='../data/1.jpg'
        # 利用qlabel显示图片
        print('open:' + imgName)
        self.png = QtGui.QPixmap(imgName).scaled(
            self.label.width(), self.label.height())
        self.label.setPixmap(self.png)
        image_path = str(imgName)

        img = cv2.imread(image_path)  # 读取
        self.imgg = img.copy()
        t = img.shape
        faces = detector(img, 1)

        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        if (len(faces) > 0):
            for k, d in enumerate(faces):
                left = max(int((3 * d.left() - d.right()) / 2), 1)
                top = max(int((3 * d.top() - d.bottom()) / 2) - 50, 1)
                right = min(int((3 * d.right() - d.left()) / 2), t[1])
                bottom = min(int((3 * d.bottom() - d.top()) / 2), t[0])
                self.rect = (left, top, right, bottom)
                rect_reg = (d.left(), d.top(), d.right(), d.bottom())
                shape = landmark_predictor(img, d)
                xx, yy = 0, 0
                for i in range(68):
                    xx += shape.part(i).x
                    yy += shape.part(i).y
                    # cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
                #     cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))
                xx, yy = int(xx / 68), int(yy / 68)
        else:
            exit(0)
        cv2.grabCut(img, mask, self.rect, bgdModel, fgdModel, 5,
                    cv2.GC_INIT_WITH_RECT)  # 函数返回值为mask,bgdModel,fgdModel
        mask2 = np.where(
            (mask == 2) | (
                mask == 0),
            0,
            1).astype('uint8')  # 0和2做背景

        # cv2.imshow('b',img)
        img = img * mask2[:, :, np.newaxis]  # 使用蒙板来获取前景区域
        erode = cv2.erode(img, None, iterations=1)
        dilate = cv2.dilate(erode, None, iterations=1)
        for i in range(t[0]):  # 高
            for j in range(t[1]):
                if max(dilate[i, j]) <= 0:
                    # if (abs(j - xx) * abs(j - xx)) < 100:  # 距离调整
                    #     continue
                    # else:
                    dilate[i, j] = (225, 166, 23)  # BGR
        img = img[self.rect[1]:self.rect[3], self.rect[0]:self.rect[2]]
        dilate = dilate[self.rect[1]:self.rect[3], self.rect[0]:self.rect[2]]
        self.output_im = cv2.resize(dilate, (361, 381))
        self.output_imreg = cv2.resize(img, (361, 381))

    def image_crop(self):
        # 截取图片，预处理
        self.imgg = self.imgg[self.rect[1]
            :self.rect[3], self.rect[0]:self.rect[2]]
        self.imgg = cv2.resize(self.imgg, (361, 381))
        cv2.imwrite('output_crop.jpg', self.imgg)
        self.label_2.setPixmap(
            QtGui.QPixmap('output_crop.jpg').scaled(
                self.label.width(),
                self.label.height()))
    pass

    def change(self):
          # 显示轮廓
        cv2.imwrite('output.jpg', self.output_im)
        cv2.imwrite('output_reg.jpg', self.output_imreg)
        self.label_3.setPixmap(
            QtGui.QPixmap('output_reg.jpg').scaled(
                self.label.width(),
                self.label.height()))
    pass

    def generate(self):
        # 生成证件照
        self.label_4.setPixmap(
            QtGui.QPixmap('output.jpg').scaled(
                self.label.width(),
                self.label.height()))
    pass

    def backchange(self):
        # 更换背景
        self.back_img = cv2.imread('output.jpg')
        self.back_img = self.bule2red(self.back_img)
        cv2.imwrite('output1.jpg', self.back_img)
        self.label_4.setPixmap(
            QtGui.QPixmap('output1.jpg').scaled(
                self.label.width(),
                self.label.height()))
        pass

    def save(self):
        file_path, file_p = QFileDialog.getSaveFileName(
            self, "save file", "../save/save.jpg", "*.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        print('save:' + file_path)
        cv2.imwrite(file_path, self.back_img, None)
        pass


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
