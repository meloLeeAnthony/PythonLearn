openCV官网：https://opencv.org

OpenCV的全称是Open Source Computer Vision Library，是一个跨平台的计算机视觉库。
OpenCV是由英特尔公司发起并参与开发，以BSD许可证授权发行
OpenCV用C++语言编写
    pip install opencv-python
--------------------------------------------------------------------------------
提取出图像的细节对产生稳定分类结果和跟踪结果很有用。这些提取的结果被称为特征;
Haar特征是一种用于实现实时人脸跟踪的特征

--------------------------------------------------------------------------------
本机路径：D:\opencv\sources\data\haarcascades
人脸检测器（默认）：haarcascade_frontalface_default.xml
人脸检测器（快速Harr）：haarcascade_frontalface_alt2.xml
人脸检测器（侧视）：haarcascade_profileface.xml
眼部检测器（左眼）：haarcascade_lefteye_2splits.xml
眼部检测器（右眼）：haarcascade_righteye_2splits.xml
嘴部检测器：haarcascade_mcs_mouth.xml
鼻子检测器：haarcascade_mcs_nose.xml
身体检测器：haarcascade_fullbody.xml
人脸检测器（快速LBP）：lbpcascade_frontalface.xml

--------------------------------------------------------------------------------
视频是一张一张图片组成的，在视频的帧上重复这个过程就能完成视频中的人脸检测

--------------------------------------------------------------------------------
使用Python 3 &OpenCV 3.0.0进行人脸识别训练时发现异常
    AttributeError: ‘module’ object has no attribute ‘LBPHFaceRecognizer_create’OpenCV
解决方案：pip install opencv-contrib-python

pgm文件是人脸识别图片

--------------------------------------------------------------------------------
LBPH（Local Binary Pattern Histogram）将检测到的人脸分为小单元，
并将其与模型中的对应单元进行比较，对每个区域的匹配值产生一个直方图。
由于这种方法的灵活性，LBPH是唯一允许模型样本人脸和检测到的人脸在形状、大小上可以不同的人脸识别算法。

调整后的区域中调用predict()函数，该函数返回两个元素的数组：第一个元素是所识别个体的标签，第二个是置信度评分

0 表示完全匹配。
可能有时不想保留所有的识别结果，则需要进一步处理，因此可用自己的算法来估算识别的置信度评分。
LBPH一个好的识别参考值要低于50，任何高于80的参考值都会被认为是低的置信度评分

--------------------------------------------------------------------------------
orl_faces是网上的人脸识别训练库