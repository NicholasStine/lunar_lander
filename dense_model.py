import numpy as np
from tensorflow import keras

class DenseModel():
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Input((3,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(3, activation='softmax')
        ])
        self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])
    
    def fit(self, flight_data):
        data = np.array(flight_data, dtype="float64")
        print(data.shape)
        x = data[:,0]
        y = data[:,1]
        print(x)
        print(y)
        self.model.fit(x, y, epochs=3, batch_size=32)