msg = "hello"
print(msg)

import numpy as np

msg = "Roll a dice"
print(msg)

print(np.random.randint(1,9))

import tensorflow as tf
print(tf.__version__)


# # Get the GPU device name.
# device_name = tf.test.gpu_device_name()
#
# # The device name should look like the following:
# if device_name == '/device:GPU:0':
#     print('Found GPU at: {}'.format(device_name))
# else:
#     raise SystemError('GPU device not found')