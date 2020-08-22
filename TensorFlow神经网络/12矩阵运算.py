import tensorflow as tf

A = tf.constant([[1, 2, 3], [4, 5, 6]])
B = tf.fill([3, 4], 3)
C = tf.constant([[1, 2, 3, 4], [11, 12, 13, 14]])

with tf.Session() as sess:
    A_value = sess.run(A)
    B_value = sess.run(B)
    print('A_value\n', A_value)
    print('B_value\n', B_value)
    print('C_value\n', sess.run(C))
    print('矩阵相乘运算')
    matmal = tf.matmul(A, B)
    print(matmal)
    print('matmal_value\n', sess.run(matmal))
    print('矩阵相加运算')
    add = tf.add(matmal, C)
    print(add)
    print('add_value\n', sess.run(add))
