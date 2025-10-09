from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your ML models
placement_model = pickle.load(open('./models/is_placement.pkl', 'rb'))
salary_model = pickle.load(open('./models/salary_model.pkl', 'rb'))

@app.route('/predict-placement', methods=['POST'])
def predict_placement():
    data = request.json
    features = np.array([list(data.values())]).astype(float)
    pred = placement_model.predict(features)[0]
    return jsonify({'placement': int(pred)})

@app.route('/predict-salary', methods=['POST'])
def predict_salary():
    data = request.json
    features = np.array([list(data.values())]).astype(float)
    pred = salary_model.predict(features)[0]
    return jsonify({'predicted_salary': float(pred)})

if __name__ == '__main__':
    app.run(debug=True)
