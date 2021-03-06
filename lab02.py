import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility
 # X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

#X=tf.placeholder(tf.float32)
#Y=tf.placeholder(tf.float32)

W=tf.Variable(tf.random_normal([1]), name='weight')
b=tf.Variable(tf.random_normal([1]), name='bias')

hypothesis=x_train*W+b
#hypothesis=X*W+b

cost=tf.reduce_mean(tf.square(hypothesis-y_train))
#cost=tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess=tf.Session()

sess.run(tf.global_variables_initializer())
for step in range(4001):
    sess.run(train)
    if step%20==0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
'''
for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X: [1,2,3,4,5,6,7,8,9,10], Y: [3,5,7,9,11,13,15,17,19,21]})
    if step%20==0:
        print(step, cost_val, W_val, b_val)
'''