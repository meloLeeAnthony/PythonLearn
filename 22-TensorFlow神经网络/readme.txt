人工神经网络（Artificial Neural Networks）也简称为神经网络（NN）。是模拟人类大脑神经网络的结构和行为。

神经网络原理
经典的神经网络有以下三个层次组成：输入层(input layer), 隐藏层(hidden layers), 输出层(output layers)。

感知机是一种基本的分类模型，类似于逻辑回归。
    不同的是感知机的逻辑函数用的是sign，而逻辑回归用的是Sigmoid函数，感知机也具有连接权重和偏置

http://playground.tensorflow.org/

TensorFlow是一个开源的、基于Python的机器学习框架，它由Google开发，并在图形分类、音频处理、推荐系统和自然语言处理等场景下有着丰富的应用，是目前最热门的机器学习框架。
除了Python，TensorFlow也提供了C/C++、Java、Go、R等其它编程语言的接口。

TensorFlow官网：www.tensorflow.org
模型仓库网址：github.com/tensorflow/models

TensorFlow提供CPU版本和GPU加速的版本。
CPU是核芯的数量更少，但是每一个核芯的速度更快，性能更强，更适合于处理连续性任务。
GPU是核芯数量更多，但是每一个核芯的处理速度较慢，更适合于并行任务。


TensorFlow程序通常被组织成一个构建图阶段和一个执行图阶段

TensorFlow的结构有：
1-图：这是TensorFlow将计算表示为指令之间的依赖关系的一种表示法。
2-会话：TensorFlow跨一个或多个本地或远程设备运行数据流图的机制。
3-张量：TensorFlow中的基本数据对象。
4-节点：提供图当中执行的操作。

TensorBoard:
一、
    #将图写入本地生成的events 文件
    writer = tf.summary.FileWriter('e:/events/test',graph=tf.get_default_graph())
    writer.close()

二、启动TensorBoard：tensorboard --logdir=’e:/events/test’
三、浏览器输入：输入http://localhost:6006


参数feed_dict:允许调用者覆盖图中张量的值，运行时赋值。
使用占位符的方式，占位符是一个可以在之后赋给它数据的变量。它是用来接收外部输入的。占位符可以是一维或者多维，用来存储n 维数组。
    feed_dict必须与tf.placeholder搭配使用，则会检测值的形状是否与占位符兼容

---------------------------------------------------------------------------------------------------------
张量是一个数学对象，它是对标量、向量和矩阵的泛化。张量可以表示为一个多维数组。
零秩张量就是标量。向量或者数组是秩为1的张量，而矩阵是秩为2的张量。

TensorFlow的张量具有两种形状变换，动态形状和静态形状
静态形状转换调用set_shape()，转换的时候必须和初始创建张量时形状相同，
对于已经固定好静态形状的张量，不能再次设置静态形状
    否则：ValueError: Dimensions 2 and 5 are not compatible