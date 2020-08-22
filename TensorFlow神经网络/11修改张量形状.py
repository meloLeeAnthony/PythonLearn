import tensorflow as tf


def tensor_shape_demo():
    a_p = tf.placeholder(dtype=tf.float32, shape=[None, None])
    b_p = tf.placeholder(dtype=tf.float32, shape=[None, 5])
    print('静态形状修改')
    print('修改前形状：')
    print('a_p:', a_p)
    print('b_p:', b_p)

    print('修改后形状')
    a_p.set_shape([2, 5])
    print('a_p:', a_p)
    b_p.set_shape([5, 5])
    print('b_p:', b_p)
    '''
    静态形状进行修改：对已经固定好的静态形状的张量，不能再次设置静态形状
        否则：ValueError: Dimensions 2 and 5 are not compatible
              ValueError: Shapes (?, 5) and (5, 6) are not compatible
    '''
    # a_p.set_shape([5, 2])
    # print('a_p:', a_p)
    '''
    动态修改形状，修改前和修改后张量的元素个数必须一致
    '''
    print('动态形状修改')
    c_p = tf.placeholder(dtype=tf.float32, shape=[3, 4])
    print('动态修改前：')
    print('c_p:', c_p)
    print('动态修改后')
    c_p = tf.reshape(c_p, shape=[2, 6])
    print('c_p:', c_p)
    c_p = tf.reshape(c_p, shape=[6, 2])
    print('c_p:', c_p)
    c_p = tf.reshape(c_p, shape=[4, 3])
    print('c_p:', c_p)
    c_p = tf.reshape(c_p, shape=[4, 3, 1])
    print('c_p:', c_p)

    # c_p = tf.reshape(c_p, shape=[4, 3, 2])
    # print('c_p:', c_p)


if __name__ == '__main__':
    tensor_shape_demo()
