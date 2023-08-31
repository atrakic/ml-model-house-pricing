import os
import pickle

import numpy as np
from flask import Flask, jsonify, render_template, request

model_file = os.getenv("MODEL_FILE")
model = pickle.load(open(model_file, "rb"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # rooms = int(request.form["rooms"])
    # distance = int(request.form["distance"])
    int_inputs = [int(x) for x in request.form.values()]
    arr = [np.array(int_inputs)]
    prediction = model.predict(arr)
    # prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template(
        "index.html",
        prediction_text=f"A house with {rooms} rooms located {distance} km has a value of ${output}",
    )


@app.route("/api", methods=["POST"])
def api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
    app.run(port=PORT)
