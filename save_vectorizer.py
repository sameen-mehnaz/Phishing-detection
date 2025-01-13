from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data (replace this with your actual data)
X_train = ["example phishing text", "example safe text"]
y_train = ["bad", "good"]

# Create and train a pipeline with CountVectorizer and LogisticRegression
vectorizer = CountVectorizer(stop_words='english')
model_pipeline = Pipeline([
    ('countvectorizer', vectorizer),
    ('logisticregression', LogisticRegression())
])

# Fit the pipeline to your data
model_pipeline.fit(X_train, y_train)

# Save the vectorizer and model
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model_pipeline, 'phishing.pkl')
