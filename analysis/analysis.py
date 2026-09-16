import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px


def reviews_over_time(df):

    reviews = (
        df.groupby(
            df["last review"].dt.to_period("M")
        ).size()
    )

    return reviews

def basic_statistics(df):

    return df.describe()

def price_distribution(df):

    price_bins = [0, 200, 400, 600, 800, float("inf")]

    price_labels = [
        "$0–200",
        "$201–400",
        "$401–600",
        "$601-800",
        "$801+"
    ]

    price_ranges = pd.cut(
        df["price"],
        bins=price_bins,
        labels=price_labels,
        include_lowest=True
    )

    price_summary = (
        price_ranges
        .value_counts()
        .sort_index()
        .reset_index()
    )

    price_summary.columns = [
        "Price Range",
        "Listings"
    ]

    fig = px.treemap(
        price_summary,
        path=["Price Range"],
        values="Listings",
        title="Airbnb Listings by Price Range"
    )

    fig.update_traces(
        textinfo="label+value+percent root"
    )

    fig.update_layout(
        height=500,
        margin=dict(t=60, l=10, r=10, b=10)
    )

    return fig

def room_type_distribution(df):

    #Show the number of listings for each room type.

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.countplot(
        x=df["room type"],
        ax=ax
    )

    ax.set_title("Distribution of Room Type")
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Count")

    return fig

def neighbourhood_distribution(df):

    #Show the number of listings in each neighbourhood group.

    fig, ax = plt.subplots(figsize=(8, 4))

    order = df["neighbourhood group"].value_counts().index

    sns.countplot(
        y=df["neighbourhood group"],
        order=order,
        ax=ax
    )

    ax.set_title("Distribution of Neighbourhood Group")
    ax.set_xlabel("Count")
    ax.set_ylabel("Neighbourhood Group")

    return fig

def room_type_price_distribution(df):

    #Compare listing prices across different room types.

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.boxplot(
        x=df["room type"],
        y=df["price"],
        ax=ax
    )

    ax.set_title("Price Distribution by Room Type")
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Price")

    return fig

def reviews_over_time(df):

    #Show the number of reviews over time.

    reviews = (
        df.groupby(
            df["last review"].dt.to_period("M")
        ).size()
    )

    # Convert PeriodIndex to timestamp for plotting
    reviews.index = reviews.index.to_timestamp()

    fig, ax = plt.subplots(figsize=(12, 6))

    reviews.plot(
        kind="line",
        ax=ax
    )

    ax.set_title("Number of Reviews Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Reviews")

    return fig
