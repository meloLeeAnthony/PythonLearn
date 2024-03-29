import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def mnist_demo():
    # 加载数据集
    mnist = input_data.read_data_sets('e:/soft/MNIST_DATA', one_hot=True)
    images, labels = mnist.train.next_batch(100)
    # print('images.shape',images.shape,'labels.shape:',labels.shape)
    # 1.准备数据
    x = tf.placeholder(dtype=tf.float32, shape=[None, 784])
    y_true = tf.placeholder(dtype=tf.float32, shape=[None, 10])
    # 2.构建模型  x(None,784)  * weight(784,10) +bias = y(None,10)
    weight = tf.Variable(initial_value=tf.random_normal(shape=[784, 10]))
    bias = tf.Variable(initial_value=tf.random_normal(shape=[10]))
    y_predict = tf.matmul(x, weight) + bias
    # 3.构建损失函数 softmax  交叉熵损失
    error = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))
    # 4.优化损失
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(error)
    # 初始化变量
    init = tf.global_variables_initializer()
    # 开始会话
    with tf.Session() as sess:
        # 运行初始化变量
        sess.run(init)
        print('训练模型前的损失:%f' % (sess.run(error, feed_dict={x: images, y_true: labels})))
        # 训练
        for i in range(1000):
            op, loss = sess.run([optimizer, error], feed_dict={x: images, y_true: labels})
            print('第%d次训练模型的损失:%f' % ((i + 1), loss))


if __name__ == '__main__':
    mnist_demo()
