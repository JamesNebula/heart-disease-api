from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

model_path = 'model.joblib'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file {model_path} not found!")

# Load the saved model
model = joblib.load('model.joblib')
print("Model loaded successfully!")

@app.route('/')
def home():
    return "🫀 Heart Disease Prediction API (Use POST /predict)"

@app.route('/predict', methods=['POST'])
def predict():
    try:
    # Get json data from request
        data = request.get_json(force=True)
     
    #Convert to dataframe (important for model input)
        df = pd.DataFrame([data])
    
    # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0].max()
    
    # return JSON response
        return jsonify({
            'prediction': int(prediction),
            'probability': round(float(probability), 2),
            'message': 'Heart disease detected' if prediction == 1 else 'No heart disease'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)