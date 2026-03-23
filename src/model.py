import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def prepare_data(df):
    le = LabelEncoder()
    df["level"] = le.fit_transform(df["level"])
    df["length_category"] = le.fit_transform(df["length_category"])

    X = df[[
        "price",
        "num_subscribers",
        "num_reviews",
        "content_duration",
        "level",
        "length_category",
        "engagement_score",
        "popularity_score"
    ]]

    y = df["completed"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))