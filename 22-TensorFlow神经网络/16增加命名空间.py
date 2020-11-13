import tensorflow as tf


def linear_regression():
    with tf.variable_scope('prepare_data'):
        # 1.准备数据
        X = tf.random_normal(shape=[100, 1], name='feature')
        y_true = tf.matmul(X, [[0.8]]) + 0.7
    with tf.variable_scope('create_mode'):
        # 构造权重weight 和偏置 使用变量来创建
        weight = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]), name='weight')
        bias = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]), name='bias')
        y_predict = tf.matmul(X, weight) + bias
    with tf.variable_scope('loss_function'):
        # 2.构造损失函数
        error = tf.reduce_mean(tf.square(y_predict - y_true))
    with tf.variable_scope('optimizer'):
        # 3.优化损失
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(error)
    # （2）增加变量显示 收集变量
    tf.summary.scalar('error', error)
    tf.summary.histogram('weights', weight)
    tf.summary.histogram('bias', bias)
    # （3）增加变量显示 合并变量
    merged = tf.summary.merge_all()
    # 初始化变量
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        # 运行初始化变量
        sess.run(init)
        print('训练前查看模型参数：权重：%f,偏置：%f,损失：%f' % (weight.eval(), bias.eval(), error.eval()))
        # （1）增加变量显示 创建事件文件
        fileWriter = tf.summary.FileWriter('e:/events/test', graph=sess.graph)
        # 训练
        for i in range(100):
            sess.run(optimizer)
            print('训练%d次后查看模型参数：权重：%f,偏置：%f,损失：%f' % ((i + 1), weight.eval(), bias.eval(), error.eval()))
            # （4）增加变量显示 运行合并变量
            summary = sess.run(merged)
            # （5）增加变量显示 将变量写入事件文件
            fileWriter.add_summary(summary, i)


if __name__ == '__main__':
    linear_regression()
