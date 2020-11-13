import tensorflow as tf


def session_demo():
    a = tf.constant(20)
    b = tf.constant(30)
    c = a + b
    print('c:', c)
    # 开启会话
    with tf.Session() as sess:
        c_value = sess.run(c)
        print('c_value:', c_value)

        print('run()方法中传入列表')
        v = sess.run([a, b, c])
        print('传入列表获取的结果：', v)

        print('run()方法中传入元组')
        a_value, b_value, c_value = sess.run((a, b, c))
        print('传入元组获取的结果：', a_value, b_value, c_value)
        print('使用eval()获取结果:', c.eval())


if __name__ == '__main__':
    session_demo()
