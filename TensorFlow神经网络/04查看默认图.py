import tensorflow as tf


def default_graph_demo():
    a = tf.constant(10)
    b = tf.constant(20)
    c = a + b
    print('tf默认图：', tf.get_default_graph())
    print('a默认图属性：', a.graph)
    print('b默认图属性：', b.graph)
    print('c默认图属性：', c.graph)
    with tf.Session() as sess:
        c_value = sess.run(c)
        print('c_value:', c_value)
        print('session默认图属性：', sess.graph)


if __name__ == '__main__':
    default_graph_demo()
