import tensorflow as tf


def graph_demo():
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

    # 自定义图
    new_g = tf.Graph()
    print('自定义图：', new_g)
    # 在自定图中定义数据和操作
    with new_g.as_default():
        a_new = tf.constant(100)
        b_new = tf.constant(200)
        c_new = a_new + b_new
        print('c_new:', c_new)

    # 开启会话，传入图参数
    with tf.Session(graph=new_g) as sess:
        c_new_value = sess.run(c_new)
        print('c_new_value:', c_new_value)


if __name__ == '__main__':
    graph_demo()
