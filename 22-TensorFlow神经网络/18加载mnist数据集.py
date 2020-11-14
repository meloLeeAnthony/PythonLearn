# MNIST数据集：http://yann.lecun.com/exdb/mnist/
from tensorflow.examples.tutorials.mnist import input_data

# 加载数据集
mnist = input_data.read_data_sets('e:/soft/MNIST_DATA', one_hot=True)
# 加载训练集样本
train_x = mnist.train.images
# 加载验证集样本
validation_x = mnist.validation.images
# 加载测试集样本
test_x = mnist.test.images

# 加载训练集标签
train_y = mnist.train.labels
# 加载验证集标签
validation_y = mnist.validation.labels
# 加载测试集标签
test_y = mnist.test.labels
print('train_x.shape:', train_x.shape, 'train_y.shape:', train_y.shape)
# 查看训练集中第一个样本的内容和标签
print(train_x[1])
print(train_y[1])
# 获取训练集数据的前100个
images, labels = mnist.train.next_batch(100)
print('images.shape:', images.shape, 'labels.shape:', labels.shape)
import matplotlib.pyplot as plt

# 绘制训练集前20个样本
fig, ax = plt.subplots(nrows=4, ncols=5)
ax = ax.flatten()
for i in range(20):
    img = train_x[i].reshape(28, 28)
    ax[i].imshow(img, cmap='Greys')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.show()
