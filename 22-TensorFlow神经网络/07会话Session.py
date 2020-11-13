import tensorflow as tf


def session_demo():
    a = tf.constant(20)
    b = tf.constant(30)
    c = a + b
    print('c:', c)
    # 开启会话
    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                          log_device_placement=True)) as sess:
        c_value = sess.run(c)
        print('c_value:', c_value)


if __name__ == '__main__':
    session_demo()
