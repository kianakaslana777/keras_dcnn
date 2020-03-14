from keras.layers import MaxPooling1D, Conv1D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import Sequential

from preprocessing.preprocessing import input_shape


def build_model():
    model = Sequential()
    model.add(Conv1D(32, 3, activation='tanh', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(64, 3, activation='tanh'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(256, activation='tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(23, activation='softmax'))
    print(model.summary())
    return model
