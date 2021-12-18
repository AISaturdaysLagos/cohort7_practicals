from flask import Flask, jsonify, request
import traceback
import joblib
import numpy as np

# initialize the flask app
app = Flask(__name__)

# load model
model = joblib.load("breast_cancer_model.sav")

@app.route("/", methods=["GET"])
def home():
    return "PINGing Successful!"

# API endpoint to make prediction
@app.route("/predict", methods=['POST'])
def inference():
    if model:
        try:
            # get input data and confirm that it's in the right format
            r_json = request.get_json(force=True)
            query = r_json if type(r_json[0]) == list else [r_json]

            # make prediction and decode label
            status = {1: "Positive", 0: "Negative"}
            prediction = [status[i] for i in model.predict(query).tolist()]

            return jsonify(prediction=prediction)
        except:
            return jsonify({"trace": traceback.format_exec()})
    else:
        return ("Model is not available")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
