from flask import Flask, request
import pickle
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


with open("sentiment_model_v1.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def hello_world():
    return "<p>Hello, hi World hjkl 45! testi</p>"


@app.route("/api", methods=["POST"])
def sentiment():
    body_data = request.get_json()

    text = body_data["data"]

    prediction = model.predict([text])

    print("INPUT:", text)
    print("PREDICTION:", prediction)

    return {"sentiment": prediction[0]}