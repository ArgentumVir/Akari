import tensorflow as tf
import numpy as np
from lib.cli import handleArgs
try:
	from tqdm import tqdm
except ImportError:
	def tqdm(x, *args, **kwargs):
		return x

handleArgs()

np.random.seed(0)

session = tf.Session()

init_op = tf.global_variables_initializer()
session.run(init_op)


session.close()
