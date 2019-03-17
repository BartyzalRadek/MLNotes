import tensorflow as tf
import tensorflow.keras as keras


def get_config_proto():
    """
    Create default Session config:
     - allow_soft_placement=True
     - log_device_placement=True
     - gpu_options.allow_growth = True
    :return: new tf.ConfigProto instance
    """
    config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
    config.gpu_options.allow_growth = True
    return config


def set_session_config(config: tf.ConfigProto):
    """
    Sets the global tf.Session used by Keras.
    :param config: tf.ConfigProto instance - get default one by get_config_proto()
    :return: Nothing
    """
    sess = tf.Session(config=config)
    keras.backend.set_session(sess)


class CustomTensorBoardCallback(keras.callbacks.TensorBoard):
    def __init__(self, update_freq='epoch', **kw):
        """
        This is already implemented in TF 1.13:
        https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/callbacks.py
        So use this only for TF 1.11 and 1.12
        :param update_freq: 'batch', 'epoch' or a number of batches
        """
        super(CustomTensorBoardCallback, self).__init__(**kw)
        if update_freq == 'batch':
            self.update_freq = 1
        else:
            self.update_freq = update_freq

    def on_batch_end(self, batch, logs=None):
        if self.update_freq != 'epoch' and batch % self.update_freq == 0:
            super(CustomTensorBoardCallback, self).on_batch_end(batch, logs)
            # print('Updated TensorBoard on batch ', batch)
