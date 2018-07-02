# face_gui
## 项目介绍 
该项目能够从给定的正面照片中，自动识别脸部区域，并对图像前景进行提取分割，然后替换背景，并按照证件照的规格进行规范化处理。一共由5个模块组成：</br>

### 1.	头部局部照识别与截取模块设计
利用Vahid Kazemi 和 Josephine Sullivan提出的基于gradient boosting的回归树算法检测面部的68个关键点位置.</br>
[论文:One Millisecond Face Alignment with an Ensemble of Regression Trees](http://www.nada.kth.se/~vahidk/face_ert.html)</br>
       
### 2.	图像前景分割</br>
利用opencv中的grabcut方法对人脸周围区域进行分割，将人头和衣服等前景分离出来.</br>
[论文:GrabCut” — Interactive Foreground Extraction using Iterated Graph Cuts](https://wenku.baidu.com/view/4b8db16a58fafab069dc0292.html)</br>
 
### 3.	证件照规范化
按照规格进行图片处理:分辨率：361×381，分辨率96dpi，位深度24，大小30k左右.</br>

### 4.	背景替换
根据图片的背景颜色特征进行替换背景（蓝-红-白），如蓝背景变为红背景：将BGR图像转为HSV图像，蓝颜色H通道在78和110之间，然后转换通道将这些像素替换为(0，0，255)即可。</br>
    
### 5.	界面设计
利用pyqt5进行界面设计.</br>

 ## 项目配置
 ### 环境平台</br>
 python3</br>
 
 ### 模块安装</br>
      pip install opencv-python 
      pip install pyqt5 
      pip install dlib 
      
 ### 文件下载</br>
 [shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)下载后放入data目录中</br>
 
 ### 脚本运行</br>
 python head.py
 
  ## 项目展示
  ![image](https://github.com/kailaisun/face_gui/blob/master/For%20show.png)
