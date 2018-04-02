import tensorflow as tf
import numpy as np

batch_size = 5
dim = 3
hidden_units = 8


sess = tf.Session()

with sess.as_default():
    x = tf.placeholder(dtype=tf.float32, shape=[None, dim], name="x")
    y = tf.placeholder(dtype=tf.int32, shape=[None], name="y")
    w = tf.Variable(initial_value=tf.random_normal(shape=[dim, hidden_units]), name="w")
    b = tf.Variable(initial_value=tf.zeros(shape=[hidden_units]), name="b")

    logits = tf.nn.tanh(tf.matmul(x, w) + b)
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits, name="xentropy")

    pred = tf.add(tf.matmul(x, w), b)
    cost = tf.reduce_sum(tf.pow(pred - tf.one_hot(y,8), 2))

    # begin training
    optimizer = tf.train.GradientDescentOptimizer(1e-5)
    grads_and_vars = optimizer.compute_gradients(cost, tf.trainable_variables())

    # generate data
    data = np.random.randn(batch_size, dim)
    labels = np.random.randint(0, 8, size=batch_size)

    sess.run(tf.initialize_all_variables())
    gradients_and_vars = sess.run(grads_and_vars, feed_dict={x:data, y:labels})
    for g, v in gradients_and_vars:
        if g is not None:
            print("****************this is variable*************")
            print("variable's shape:", v.shape)
            print(v)
            print("****************this is gradient*************")
            print("gradient's shape:", g.shape)
            print(g)

sess.close()