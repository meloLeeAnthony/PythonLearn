import tensorflow as tf


def events_demo():
    a = tf.constant(20, name='a')
    b = tf.constant(30, name='b')
    c = a + b
    print('c:', c)
    # 开启会话
    with tf.Session() as sess:
        c_value = sess.run(c)
        print('c_value:', c_value)
        # 生成events文件
        writer = tf.summary.FileWriter('E:/TensorBoard', graph=tf.get_default_graph())
        writer.close()


if __name__ == '__main__':
    events_demo()
