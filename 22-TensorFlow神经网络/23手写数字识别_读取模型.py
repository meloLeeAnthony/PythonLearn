import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def mnist_demo():
    # 加载数据集
    mnist = input_data.read_data_sets('e:/soft/MNIST_DATA', one_hot=True)
    images, labels = mnist.train.next_batch(100)
    # print('images.shape',images.shape,'labels.shape:',labels.shape)
    with tf.variable_scope('prepare_data'):
        # 1.准备数据
        x = tf.placeholder(dtype=tf.float32, shape=[None, 784], name='feature')
        y_true = tf.placeholder(dtype=tf.float32, shape=[None, 10], name='y_true')
    with tf.variable_scope('create_mode'):
        # 2.构建模型  x(None,784)  * weight(784,10) +bias = y(None,10)
        weight = tf.Variable(initial_value=tf.random_normal(shape=[784, 10]), name='weight')
        bias = tf.Variable(initial_value=tf.random_normal(shape=[10]), name='bias')
        y_predict = tf.matmul(x, weight) + bias
    with tf.variable_scope('loss_function'):
        # 3.构建损失函数 softmax  交叉熵损失
        error = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))
    with tf.variable_scope('optimizer'):
        # 4.优化损失
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(error)
    # （2）增加变量显示  添加变量
    tf.summary.scalar('error', error)
    tf.summary.histogram('weight', weight)
    tf.summary.histogram('bias', bias)

    # （3）增加变量显示  合并变量
    merged = tf.summary.merge_all()

    # （1）读取模型  创建saver对象
    saver = tf.train.Saver()
    # 初始化变量
    init = tf.global_variables_initializer()
    # 开始会话
    with tf.Session() as sess:
        # 运行初始化变量
        sess.run(init)
        print('训练模型前的损失:%f' % (sess.run(error, feed_dict={x: images, y_true: labels})))
        # （1）增加变量显示  创建事件文件
        fileWriter = tf.summary.FileWriter('e:/mnist/events', graph=sess.graph)

        # (2)读取模型  判断模型是否存在
        ckpt = tf.train.get_checkpoint_state('./ckpt/')
        if ckpt and ckpt.model_checkpoint_path:
            # 读取模型
            saver.restore(sess, './ckpt/mnist.ckpt')
        print('训练后模型参数损失：%f' % (sess.run(error, feed_dict={x: images, y_true: labels})))


if __name__ == '__main__':
    mnist_demo()
