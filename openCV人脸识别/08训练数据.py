import os

import cv2
import numpy as np
from PIL import Image


def getImageAndLabels(path):
    '''
        获取图像数组和id标签数组
    :param path: 模型图片的路径
    :return:
        facesSamples：模型坐标数组
        ids：图片名称数组
    '''
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path, file) for file in os.listdir(path)]
    # 检测人脸
    face_detector = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片
        PIL_img = Image.open(imagePath).convert('L')
        # 将图像转换为数组
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
    return facesSamples, ids


if __name__ == '__main__':
    # 模型图片的路径
    path = './trainerData/'
    # 获取图像数组和id标签数组
    faces, ids = getImageAndLabels(path)
    # 获取训练对象
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    # Save the model into trainerResult/trainerResult.yml
    # error: (-2:Unspecified error) File can't be opened for writing! in 03-function函数 'cv::face::FaceRecognizer::write'
    # 该error需要自行创建trainer文件夹
    recognizer.write('trainerResult/trainer.yml')
