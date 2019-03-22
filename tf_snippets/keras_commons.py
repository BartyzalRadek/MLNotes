import tensorflow as tf
import tensorflow.keras as keras
import logging
import os

logger = logging.getLogger(__name__)


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


class CustomModelCheckpointCallback(keras.callbacks.ModelCheckpoint):
    def __init__(self, restore_best_weights=True, **kw):
        """
        Extends ModelCheckpoint Callback with restore_best_weights functionality.
        :param restore_best_weights: True = restore weight from the best epoch at the end of training.

        ModelCheckpoint params:
        :param filepath: string, path to save the model file.
        :param monitor: quantity to monitor.
        :param verbose: verbosity mode, 0 or 1.
        :param save_best_only: if `save_best_only=True`,
            the latest best model according to
            the quantity monitored will not be overwritten.
        :param save_weights_only: if True, then only the model's weights will be
            saved (`model.save_weights(filepath)`), else the full model
            is saved (`model.save(filepath)`).
        :param mode: one of {auto, min, max}.
            If `save_best_only=True`, the decision
            to overwrite the current save file is made
            based on either the maximization or the
            minimization of the monitored quantity. For `val_acc`,
            this should be `max`, for `val_loss` this should
            be `min`, etc. In `auto` mode, the direction is
            automatically inferred from the name of the monitored quantity.
        :param period: Interval (number of epochs) between checkpoints.
        """
        super(CustomModelCheckpointCallback, self).__init__(**kw)
        self.restore_best_weights = restore_best_weights
        self.best_value = None
        self.best_epoch = 0
        self.best_weights = None
        self.best_save_path = None

    def on_epoch_end(self, epoch, logs=None):
        super(CustomModelCheckpointCallback, self).on_epoch_end(epoch=epoch, logs=logs)
        if self.restore_best_weights:
            current = logs.get(self.monitor)
            if self.best_value is None or self.monitor_op(current, self.best_value):
                self.best_value = current
                self.best_epoch = epoch
                self.best_weights = self.model.get_weights()
                self.best_save_path = self.filepath.format(epoch=epoch + 1, **logs)

    def on_train_end(self, logs=None):
        super(CustomModelCheckpointCallback, self).on_train_end(logs)
        if self.restore_best_weights:
            logger.info('End of training: Restoring model weights from the epoch {} with {}={}'
                        .format(self.best_epoch + 1, self.monitor, self.best_value))
            self.model.set_weights(self.best_weights)

        if not os.path.exists(self.best_save_path):
            if self.restore_best_weights:
                self.model.save_weights(self.best_save_path)
            else:
                #TODO save weights
                logger.warning('The weights from best epoch have not been saved to best_save_path, '
                               'either use period=1, or restore_weights=True to make sure the weights are saved.')
