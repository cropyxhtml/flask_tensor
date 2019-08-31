import tensorflow as tf
class CalculatorModel:
    def __init__(self):
        pass
    def create_add_model(self):
        w1 = tf.placeholder(tf.float32,name='w1')
        w2 = tf.placeholder(tf.float32,name='w2')
        feed_dict = {'w1':8.0,'w2':2.0}
        r = tf.add(w1,w2,name='op_add')
        sess = tf.Session()
        _=tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1:feed_dict['w1'],w2:feed_dict['w2']})
        print('TF 덧셈결과 : {0}'.format(result))
        saver.save(sess, './saved_add_model/model',global_step=1000)