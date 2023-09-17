from flask import Flask,request,jsonify
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
    feat_data = request.json
    df = pd.DataFrame(feat_data)
    prediction = list(model.predict(df))
    
    return jsonify({'prediction':str(prediction)})

if __name__ == 'main':
    model = joblib.load("Customer_Churn_prediction_model.pkl")
    app.run(debug=True)