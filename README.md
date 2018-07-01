# face_gui
进度报告

1.	头部局部照识别与截取模块设计
运用hog人脸特征算子和adaboost级联分类器进行人脸的检测与定位，再利用Vahid Kazemi 和 Josephine Sullivan提出的基于gradient boosting的回归树算法检测面部的68个关键点位置，实验效果如下
    

2.	图像前景分割：opencv中的grabcut：
论文：https://wenku.baidu.com/view/4b8db16a58fafab069dc0292.html
讲解：https://www.cnblogs.com/qiaozhoulin/p/4509965.html
 


3.	证件照规范化：
按照规格进行图片处理:可以选择不同的背景模板决定图片的分辨率，暂时采取的是：
分辨率：361×381，分辨率96dpi，位深度24，大小30k左右
4.	背景替换:
我们取到图片的背景颜色，根据颜色进行替换背景，如蓝背景变为红背景：将BGR图像转为HSV图像，蓝颜色H通道在78和110之间，然后转换通道将这些像素替换为(0，0，255)即可，同理，白色背景和红色背景也是一样。效果如下：
    
5.	界面设计：
我们利用pyqt5进行界面设计，UI效果如下：

 

