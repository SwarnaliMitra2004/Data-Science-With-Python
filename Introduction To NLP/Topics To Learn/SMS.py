
# SMS SPAM CLASSIFICATION USING NLP
# Text Preprocessing + Bag of Words + TF-IDF + Naive Bayes

import pandas as pd
import string
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


# 1. Download Stopwords

# Download the English stopwords list from NLTK.
# This is needed to remove common words such as "the", "is", and "and".
nltk.download("stopwords")

# Store stopwords in a set for faster lookup.
stop_words = set(stopwords.words("english"))


# 2. Load Dataset

# Read the training and testing CSV files.
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Remove extra spaces and accidental quotation marks from column names.
train.columns = train.columns.astype(str).str.strip().str.strip("'\"")
test.columns = test.columns.astype(str).str.strip().str.strip("'\"")

# Rename columns so the rest of the program uses consistent names.
# Training data has "type" for the target label and "text" for the SMS.
train = train.rename(columns={
    "text": "message",
    "type": "label"
})

# Test data has messages but normally no labels.
test = test.rename(columns={
    "text": "message"
})

# Check that the required columns exist before continuing.
if not {"message", "label"}.issubset(train.columns):
    raise ValueError(
        "train.csv must contain 'text' and 'type' columns. "
        f"Found: {train.columns.tolist()}"
    )

if "message" not in test.columns:
    raise ValueError(
        "test.csv must contain a 'text' column. "
        f"Found: {test.columns.tolist()}"
    )

# Remove rows where the message or label is missing.
train = train.dropna(subset=["message", "label"]).copy()
test = test.dropna(subset=["message"]).copy()

# Convert message text to strings.
train["message"] = train["message"].astype(str)
test["message"] = test["message"].astype(str)

print("\nTraining dataset:")
print(train.head())
print("\nTraining shape:", train.shape)

print("\nTesting dataset:")
print(test.head())
print("\nTesting shape:", test.shape)


# 3. Text Preprocessing

def textPreprocessing(data):

    # Convert all text to lowercase.
    # Example: "FREE Offer" becomes "free offer".
    data = data.lower()

    # Remove punctuation marks such as ! , . ? and @.
    data = "".join(
        character
        for character in data
        if character not in string.punctuation
    )

    # Split the sentence into individual words.
    words = data.split()

    # Remove common English stopwords.
    # Example: "this is a great offer" becomes ["great", "offer"].
    words = [
        word
        for word in words
        if word not in stop_words
    ]

    # Return the cleaned list of words.
    return words


# Try preprocessing one sample message.
sample_sms = "Congratulations! You have WON a FREE prize."
print("\nOriginal SMS:", sample_sms)
print("Preprocessed SMS:", textPreprocessing(sample_sms))


# 4. Create Bag of Words

# CountVectorizer converts words into numerical word-count features.
# Our custom preprocessing function is applied to each message.
vectorizer = CountVectorizer(
    analyzer=textPreprocessing
)

# Learn the vocabulary from the training messages
# and convert those messages into a Bag of Words matrix.
bow_train = vectorizer.fit_transform(train["message"])

# Transform test messages using the SAME vocabulary.
# Do not fit a new vocabulary on the test data.
bow_test = vectorizer.transform(test["message"])

print("\nBag of Words training shape:", bow_train.shape)
print("Bag of Words testing shape:", bow_test.shape)

# Show a few vocabulary entries.
print("\nFirst 20 vocabulary entries:")
print(list(vectorizer.vocabulary_.items())[:20])


# 5. Calculate TF-IDF

# TF-IDF gives numerical weights to words.
# It generally reduces the importance of words appearing in many messages.
tfidf = TfidfTransformer()

# Learn IDF weights from the training data and transform it.
tfidf_train = tfidf.fit_transform(bow_train)

# Transform test data using the learned training weights.
tfidf_test = tfidf.transform(bow_test)

print("\nTF-IDF training shape:", tfidf_train.shape)
print("TF-IDF testing shape:", tfidf_test.shape)


# 6. Train Naive Bayes Model

# Multinomial Naive Bayes is commonly used for text classification.
model = MultinomialNB()

# Train the model using TF-IDF features and known labels.
# The labels come from the original "type" column, renamed to "label".
model.fit(tfidf_train, train["label"])

print("\nModel training completed!")


# 7. Predict Test Messages

# Predict the class of each test message.
predictions = model.predict(tfidf_test)

print("\nFirst 10 predictions:")
print(predictions[:10])


# 8. Save Predictions

# Preserve test IDs if the dataset provides them.
# Use "type" as the predicted-label column to match the training data.
if "id" in test.columns:
    submission = pd.DataFrame({
        "id": test["id"],
        "type": predictions
    })
else:
    submission = pd.DataFrame({
        "type": predictions
    })

# Save the results to a new CSV file.
# index=False prevents Pandas from adding an extra index column.
submission.to_csv("submission.csv", index=False)

print("\nPrediction completed!")
print("Submission saved as submission.csv")