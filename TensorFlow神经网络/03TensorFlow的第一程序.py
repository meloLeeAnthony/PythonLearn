import tensorflow as tf


def add_demo():
    # 计算两个变量的和
    # 回顾原生的python计算两数的和
    a = 10
    b = 20
    c = a + b
    print('原生python计算的和：', c)
    a_t = tf.constant(10)
    b_t = tf.constant(20)
    print('a_t:', a_t)
    c_t = a_t + b_t
    print('tensorflow计算两数的和：', c_t)
    # TensorFlow中无法看到计算结果，必须开启Session会话
    with tf.Session() as sess:
        c_t_value = sess.run(c_t)
        print('c_t_value:', c_t_value)


if __name__ == '__main__':
    add_demo()
