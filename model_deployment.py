import ray
from ray import serve
import pickle
import numpy as np
from starlette.requests import Request
from typing import Dict

@serve.deployment
class Model:
    def __init__(self):
        with open("./model.pkl", "rb") as f:
            self.model = pickle.load(f)

    async def __call__(self, starlette_request: Request) -> Dict:
        payload = await starlette_request.json()
        input_vector = [
            payload["data"]["x1"],
            payload["data"]["x2"],
            payload["data"]["x3"],
            payload["data"]["x4"],
            payload["data"]["x5"],
            payload["data"]["x6"]
        ]
        input_vector = np.transpose(input_vector)
        prediction = self.model.predict(input_vector)
        return {"tail grade g/t": prediction}

model = Model.bind()
