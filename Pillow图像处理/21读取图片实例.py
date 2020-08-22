import os
import pickle

import numpy as np
from PIL import Image

# 读取图片的目录
image_dir = './imageArrays/'
# 保存图片的目录
result_dir = './imageArrayResults/'
# 保存数组的文件
array_file = './imageDatas/array.bin'


# 读取images目录下的图片，将图片保存为大的一维数组，将数组保存到文件
def image_to_array_file():
    # 获取8张图片的名称
    filenames = os.listdir(image_dir)
    # 定义变量保存8张图片的大数组
    image_arrs = np.array([])
    for filename in filenames:
        # 读取图片
        img = Image.open(image_dir + filename)
        # 将每张图片分隔
        r, g, b = img.split()
        # 将r g b 转换为一维的数组
        r_arr = np.array(r).reshape(62500)
        g_arr = np.array(g).reshape(-1)
        b_arr = np.array(b).reshape(62500)
        # 将 r_arr  g_arr  b_arr 拼接为一维数组
        arrs = np.concatenate((r_arr, g_arr, b_arr))
        # 将 arrs  image_arrs 拼接为一维数组
        image_arrs = np.concatenate((arrs, image_arrs))

    # 将一维数组保存到文件中
    with open(array_file, 'wb') as f:
        pickle.dump(image_arrs, f)


# 读取文件中的内容，转换图片
def file_to_image():
    with open(array_file, 'rb') as f:
        images = pickle.load(f)
        # 一维数组中 8,3,250,250
        image_arr = images.reshape((8, 3, 250, 250))
    for i in range(8):
        r = Image.fromarray(image_arr[i][0]).convert('L')
        g = Image.fromarray(image_arr[i][1]).convert('L')
        b = Image.fromarray(image_arr[i][2]).convert('L')
        # 合并图片
        image = Image.merge('RGB', (r, g, b))
        image.save(result_dir + str(i) + '.jpg')


if __name__ == '__main__':
    image_to_array_file()
    file_to_image()
