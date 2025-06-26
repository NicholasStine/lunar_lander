import numpy as np
from tensorflow import keras

class DenseModel():
    def __init__(self, load_model=None):
        if load_model:
            self.model = keras.models.load_model(f"brains/{load_model}.keras")
            return
        self.model = keras.Sequential([
            keras.layers.Input((3,)),
            keras.layers.Dense(256, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(3, activation='softmax')
        ])
        optimizer = keras.optimizers.Adam(learning_rate=1e-3)
        self.model.compile(optimizer=optimizer, loss="mean_squared_error", metrics=['accuracy'])
        
    def mutate(self):
        mutated = []
        weights = self.model.get_weights()
        # print(mutated)
        for weight in weights:
            mutation = np.random.normal(0, 0.05, weight.shape)
            mutated.append(weight + mutation)
        self.model.set_weights(mutated)
    
    def fit(self, flight_data, epochs=3, model_name='default_model'):
        data = np.array(flight_data, dtype="float64")
        print(data.shape)
        x = data[:,0]
        y = data[:,1]
        self.model.fit(x, y, epochs=epochs, batch_size=32)
        self.save(model_name)
        
    def fly(self, flight_data):
        x = np.array(flight_data, dtype="float64").reshape((-1,3))
        prediction = list(self.model.predict(x, verbose=0))[0]
        # print("prediction: ", prediction)
        thrust = prediction[0] > 0.6
        right = prediction[2] > 0.4
        left = prediction[1] > 0.4
        return thrust, right, left
        
    def save(self, model_name):
        self.model.save(f'brains/{model_name}.keras')