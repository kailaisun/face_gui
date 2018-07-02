# face_gui
## 项目介绍 
### 1.	头部局部照识别与截取模块设计
利用Vahid Kazemi 和 Josephine Sullivan提出的基于gradient boosting的回归树算法检测面部的68个关键点位置.</br>
[论文](http://www.nada.kth.se/~vahidk/face_ert.html)
       
### 2.	图像前景分割：opencv中的grabcut：
[论文](https://wenku.baidu.com/view/4b8db16a58fafab069dc0292.html)</br>
[讲解](https://www.cnblogs.com/qiaozhoulin/p/4509965.html)
 
### 3.	证件照规范化：
按照规格进行图片处理:分辨率：361×381，分辨率96dpi，位深度24，大小30k左右.

### 4.	背景替换:
根据图片的背景颜色特征进行替换背景（蓝-红-白），如蓝背景变为红背景：将BGR图像转为HSV图像，蓝颜色H通道在78和110之间，然后转换通道将这些像素替换为(0，0，255)即可。
    
### 5.	界面设计：
利用pyqt5进行界面设计.
![image](https://github.com/kailaisun/face_gui/blob/master/show.jpg)

 ## 项目配置
 平台：python3.6</br>
 模块安装：opencv-python PyQt5  dlib</br>
 文件下载：文件下载后放入data目录中[shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
