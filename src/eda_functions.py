import seaborn as sns
import matplotlib.pyplot as plt
import os


def create_visual_folder(path="../visuals"):
    os.makedirs(path, exist_ok=True)


def plot_completion_by_length(df):
    plt.figure(figsize=(8,5))
    sns.barplot(x="length_category", y="completion_rate", data=df)
    plt.title("Completion Rate by Course Length")
    plt.savefig("../visuals/completion_rate.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_engagement_by_level(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(x="level", y="engagement_score", data=df)
    plt.title("Engagement by Course Level")
    plt.savefig("../visuals/engagement_vs_completion.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_price_vs_subscribers(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="price", y="num_subscribers", data=df)
    plt.title("Price vs Subscribers")
    plt.savefig("../visuals/price_vs_subscribers.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_heatmap(df):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("../visuals/correlation_heatmap.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_completion_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["completion_rate"], bins=30, kde=True)
    plt.title("Completion Rate Distribution")
    plt.savefig("../visuals/drop_off_analysis.png", dpi=300, bbox_inches='tight')
    plt.show()