'''
回顾线性回归原理
1.构造模型
 y = w1*x1+w2*x2....+b
2.构建损失函数
  均方误差
3.优化损失
  梯度下降
  使用梯度下降优化损失，当损失最小时候所对应的权重和偏置就是我们想要的模型参数
设计方案：
1.准备数据
 假定随机指定100个点，只有一个特征。x和y之间的关系满足y=kx+b。
 x = (100,1)
 真是的y_true = (100,1)

 数据分布满足 y = 0.8*x +0.7
 x(100,1) * weight(1,1) +bias(1,1)= y_true(100,1)
 预测y_predict = tf.matmul(x,weight) +bias
2.构造损失函数
  error = tf.reduce_mean(tf.square(y_predict-y_true))
3.优化损失
  optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)
  最后在会话中不断迭代optimizer 当损失最小时候获取模型参数(权重weight和偏置bias)
'''
import tensorflow as tf
def linear_regression():
    #1.准备数据
    X = tf.random_normal(shape=[100,1])
    y_true = tf.matmul(X,[[0.8]])+0.7
    #构造权重weight 和偏置 使用变量来创建
    weight = tf.Variable(initial_value=tf.random_normal(shape=[1,1]))
    bias = tf.Variable(initial_value=tf.random_normal(shape=[1,1]))
    y_predict = tf.matmul(X,weight)+bias
    #2.构造损失函数
    error = tf.reduce_mean(tf.square(y_predict-y_true))
    #3.优化损失
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(error)

    #初始化变量
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        #运行初始化变量
        sess.run(init)
        print('训练前查看模型参数：权重：%f,偏置：%f,损失：%f'%(weight.eval(),bias.eval(),error.eval()))
        # 训练
        for i in range(100):
            sess.run(optimizer)
            print('训练%d次后查看模型参数：权重：%f,偏置：%f,损失：%f' % ((i+1),weight.eval(), bias.eval(), error.eval()))
if __name__ == '__main__':
    linear_regression()