from cache import Cache
from dense_model import DenseModel

cache = Cache(None)
flight_data = cache.load(stop_at=150)
model = DenseModel()
model.fit(flight_data, epochs=30, model_name='lunar_brain_06_20')