import tensorflow as tf


def tensor_demo():
    print('固定张量的创建')
    tensor1 = tf.constant(3.5)
    print('tensor1:', tensor1)
    tensor2 = tf.constant([1, 2, 3, 4, 5])
    print('tensor2:', tensor2)
    tensor3 = tf.constant([[1, 2, 3], [4, 5, 6]])
    print('tensor3:', tensor3)

    print('随机张量的创建')
    t_ones = tf.ones(shape=[2, 3])
    t_zeros = tf.zeros(shape=[3, 4])
    print('t_ones:', t_ones)
    print('t_zeros:', t_zeros)
    t_uniform = tf.random_uniform(shape=[1, 2], minval=1, maxval=4)
    print('t_uniform:', t_uniform)
    t_normal = tf.random_normal(shape=[2, 2], mean=1.0, stddev=3)
    print('t_normal:', t_normal)

    # 开启session会话
    with tf.Session() as sess:
        t_ones_value = sess.run(t_ones)
        print('t_ones_value')
        print(t_ones_value)
        t_zeros_value = sess.run(t_zeros)
        print('t_zeros_value')
        print(t_zeros_value)
        t_uniform_value = sess.run(t_uniform)
        print('t_uniform_value')
        print(t_uniform_value)
        t_normal_value = sess.run(t_normal)
        print('t_normal_value')
        print(t_normal_value)


if __name__ == '__main__':
    tensor_demo()
