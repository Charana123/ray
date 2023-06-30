import ray
from ray import serve
import pickle
import numpy as np
from starlette.requests import Request
from typing import Dict
import time

@serve.deployment
class Model:
    def __init__(self):
        with open("./model.pkl", "rb") as f:
            self.model = pickle.load(f)

    async def __call__(self, starlette_request: Request) -> Dict:
	try:
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
	    input_vector = np.nan_to_num(input_vector, nan=np.inf)
	    prediction = self.model.predict(input_vector)
	    return {"success": true, "data": prediction}
	except Exception as e:
	    return {"success": false, "error": e.message}

model = Model.bind()
