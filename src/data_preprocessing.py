import pandas as pd
import numpy as np


def load_data(path):
    return pd.read_csv(path)


def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def handle_missing(df):
    df = df.drop_duplicates()
    for col in df.select_dtypes(include=np.number).columns:
        df[col].fillna(df[col].median(), inplace=True)
    return df


def convert_types(df):
    df["content_duration"] = pd.to_numeric(df["content_duration"], errors="coerce")
    df["content_duration"].fillna(df["content_duration"].median(), inplace=True)
    return df


def feature_engineering(df):
    df["num_subscribers"] = df["num_subscribers"].replace(0, 1)

    df["engagement_score"] = df["num_reviews"] / df["num_subscribers"]
    df["completion_rate"] = df["num_reviews"] / df["num_subscribers"]

    df["popularity_score"] = (
        df["num_subscribers"] * 0.6 +
        df["num_reviews"] * 0.4
    )

    def length_category(x):
        if x < 5:
            return "Short"
        elif x < 20:
            return "Medium"
        else:
            return "Long"

    df["length_category"] = df["content_duration"].apply(length_category)

    df["completed"] = (df["completion_rate"] > df["completion_rate"].median()).astype(int)

    return df


def save_data(df, path):
    df.to_csv(path, index=False)