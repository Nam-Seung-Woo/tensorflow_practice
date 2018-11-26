import tensorflow as tf
x_value=[1,2,3,4,5,6,7,8,9,10]
y_value=[3,5,7,9,11,13,15,17,19,21]

W=tf.Variable(tf.random_normal([1]))
b=tf.Variable(tf.random_normal([1]))

hypothesis=x_value*W+b

cost=tf.reduce_mean(tf.square(hypothesis-y_value))

optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(20001):
    sess.run(train)
    if i%100==0:
        print(i, sess.run(cost), sess.run(W), sess.run(b))