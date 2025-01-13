import joblib

# Load the model
try:
    model = joblib.load('phishing.pkl')
    print("Model loaded successfully.")
    
    # Inspect the model (this will depend on the model type)
    print("Model type:", type(model))
    print("Model details:", model)  # This may give you useful information based on the model
    
except Exception as e:
    print(f"Error loading model: {e}")