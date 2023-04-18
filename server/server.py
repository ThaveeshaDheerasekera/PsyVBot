from flask import Flask, request, jsonify
from flask_cors import CORS

from prediction import predict_depression

app = Flask(__name__)
CORS(app)

user_inputs = [];

@app.route('/sendUserInputs', methods=['POST'])
def receive_user_inputs():
    global user_inputs
    user_inputs = request.json.get('userInputs', [])
    
    # Return a success message to the frontend
    return 'OK', 200

@app.route('/getPrediction', methods=['GET'])
def get_user_prediction():
    
    prediction = predict_depression(user_inputs)

    # result = "PsyVBot: The average prediction is: ", prediction

    # Return the prediction to the frontend
    return jsonify({'prediction': prediction})
