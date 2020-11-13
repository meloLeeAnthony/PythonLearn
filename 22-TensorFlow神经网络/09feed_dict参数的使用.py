import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a + b
cc = tf.add(a, b)
x = tf.placeholder(tf.float32, None)
y = x * 20 + 100

# 开启session会话
with tf.Session() as sess:
    c_value = sess.run(c, feed_dict={a: 20, b: 30})
    print('c_value:', c_value)
    cc_value = sess.run(cc, feed_dict={a: 20, b: 30})
    y_value = sess.run(y, feed_dict={x: 10})
    print('y_value:', y_value)
    y_value = sess.run(y, feed_dict={x: [10, 20, 30, 40]})
    print('y_value:', y_value)
