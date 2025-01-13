import uvicorn
from fastapi import FastAPI, HTTPException
import joblib
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load your model (which includes the vectorizer)
try:
    phish_model = joblib.load('phishing.pkl')  # Ensure this is your trained pipeline
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise SystemExit(1)

@app.get('/predict/')
async def predict(features: str):
    logging.info(f"Received features: {features}")
    
    if not features:
        raise HTTPException(status_code=422, detail="Missing required query parameter: features")

    # Make prediction
    try:
        y_predict = phish_model.predict([features])  # Pass input directly to the pipeline
        logging.info(f"Prediction: {y_predict}")
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Error during prediction")

    result = "This is a Phishing Site" if y_predict[0] == 'bad' else "This is not a Phishing Site"
    
    return {"input": features, "result": result}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

