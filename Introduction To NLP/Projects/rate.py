
# Rating Prediction using NLP

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
data = pd.read_csv("yelp.csv")

# Step 2: Check the column names
print(data.columns)
print(data.head())

# Step 3: Keep only the feedback and rating columns
data = data[["text", "stars"]].dropna()

# Step 4: Separate input (customer feedback) and output (rating)
X = data["text"]
y = data["stars"]

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Convert text into numerical features using TF-IDF
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Step 7: Create and train the model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Step 8: Predict ratings for the test feedback
predictions = model.predict(X_test_tfidf)

# Step 9: Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Step 10: Predict the rating for new customer feedback
new_feedback = ["The food was delicious and the service was excellent."]
new_feedback_tfidf = tfidf.transform(new_feedback)
predicted_rating = model.predict(new_feedback_tfidf)

print("Predicted rating:", predicted_rating[0], "stars")
