# This file contains a generalised architecture for Physics-Informed PointNet

# Library installs

import tensorflow as tf
from tensorflow.python.keras import optimizers
from tensorflow.python.keras import backend
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.layers import Input
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Dense, Reshape
from tensorflow.python.keras.layers import Convolution1D, MaxPooling1D, AveragePooling1D
from tensorflow.python.keras.layers import Lambda, concatenate
from tensorflow.python.keras import initializers
from tensorflow import keras

