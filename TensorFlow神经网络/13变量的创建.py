import tensorflow as tf

x = tf.constant([10, 20, 30, 40])
# 定义变量
y = tf.Variable(initial_value=x * 20 + 10)
# 修改命名空间
with tf.variable_scope('Melo_scope'):
    b = tf.Variable(initial_value=100)

print('x:', x)
print('y:', y)
print('b:', b)

'''
    必须初始化变量,否则报如下错：
    tensorflow.python.framework.errors_impl.FailedPreconditionError: Attempting to use uninitialized value Variable
'''
model = tf.global_variables_initializer()
# 开启会话
with tf.Session() as sess:
    # 运行初始化变量
    sess.run(model)
    y_value = sess.run(y)
    print('y_value:', y_value)
    b_value = sess.run(b)
    print('b_value:', b_value)
