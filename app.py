import streamlit as st
import pandas as pd

from analysis.data_loader import load_data
from analysis.data_cleaning import (
    clean_data, validate_columns, REQUIRED_COLUMNS
)

from analysis.analysis import (
    price_distribution,
    room_type_distribution,
    neighbourhood_distribution,
    room_type_price_distribution,
    reviews_over_time
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Airbnb Data Analysis",
    page_icon="🏠",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("🏠 Airbnb Data Analysis")


# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("📊 Airbnb Analysis")

st.sidebar.header("📁 Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload another CSV file (optional)",
    type=["csv"]
)


# ==========================================
# Load Data
# ==========================================

if uploaded_file is not None:

    df = load_data(uploaded_file)

    missing_columns = validate_columns(df)

    if missing_columns:

        st.error(
            "The uploaded CSV does not have the required "
            "column headings for this Airbnb analysis."
        )

        st.warning(
            "Please rename your CSV columns to match the "
            "column headings in the original Airbnb dataset."
        )

        st.subheader("Required Column Headings")

        st.write(
            "Please rename your CSV columns to match the headings below."
        )

        column_status = pd.DataFrame({
            "Column Heading": REQUIRED_COLUMNS,
            "Status": [
                "❌ Missing" if column in missing_columns else "✅ Found"
                for column in REQUIRED_COLUMNS
            ]
        })

        st.dataframe(
            column_status,
            use_container_width=True,
            hide_index=True
        )

        st.stop()

    st.sidebar.success(
        f"Using: {uploaded_file.name}"
    )

else:

    df = load_data("data/Airbnb_data.csv")

    st.sidebar.info(
        "Using default: Airbnb_data.csv"
    )

# ==========================================
# Clean Data
# ==========================================

df, cleaning_stats = clean_data(df)


# ==========================================
# Navigation
# ==========================================

st.sidebar.header("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Data Preview",
        "Price Analysis",
        "Room Analysis",
        "Location Analysis",
        "Review Analysis"
    ]
)


# ==========================================
# Dashboard
# ==========================================

if page == "Dashboard":

    st.header("📊 Dashboard")

    st.write(
        "Key statistics and data quality overview of the Airbnb dataset."
    )

    # KPI calculations
    total_listings = len(df)

    average_price = df["price"].mean()

    average_service_fee = df["service fee"].mean()

    total_reviews = int(df["number of reviews"].sum())

    room_types = df["room type"].nunique()

    neighbourhood_groups = df["neighbourhood group"].nunique()


    # KPI cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Listings",
            f"{total_listings:,}"
        )

    with col2:
        st.metric(
            "Average Price",
            f"${average_price:,.2f}"
        )

    with col3:
        st.metric(
            "Average Service Fee",
            f"${average_service_fee:,.2f}"
        )

    # KPI cards - second row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Reviews",
            f"{total_reviews:,}"
        )

    with col2:
        st.metric(
            "Room Types",
            f"{room_types:,}"
        )

    with col3:
        st.metric(
            "Neighbourhood Groups",
            f"{neighbourhood_groups:,}"
        )

    st.divider()

    st.subheader("🧹 Data Quality")

    st.write(
        "Overview of the dataset before and after data cleaning."
    )

    # Cleaning summary
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Rows Before",
            f"{cleaning_stats['rows_before']:,}"
        )

    with col2:
        st.metric(
            "Rows After",
            f"{cleaning_stats['rows_after']:,}"
        )

    with col3:
        st.metric(
            "Rows Removed",
            f"{cleaning_stats['rows_removed']:,}"
        )

    with col4:
        st.metric(
            "Duplicates Found",
            f"{cleaning_stats['duplicates_before']:,}"
        )

    st.divider()

    # Missing values
    st.subheader("Missing Values")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Missing Before Cleaning",
            f"{cleaning_stats['missing_before']:,}"
        )

    with col2:
        st.metric(
            "Missing After Cleaning",
            f"{cleaning_stats['missing_after']:,}"
        )

    st.divider()

    # Current missing values by column
    st.subheader("Remaining Missing Values by Column")

    missing_values = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing_values.columns = [
        "Column",
        "Missing Values"
    ]

    missing_values = missing_values[
        missing_values["Missing Values"] > 0
        ]

    if missing_values.empty:
        st.success(
            "No missing values found after cleaning."
        )
    else:
        st.dataframe(
            missing_values,
            use_container_width=True,
            hide_index=True
        )

    st.divider()


# ==========================================
# Data Preview
# ==========================================

elif page == "Data Preview":

    st.header("🔍 Data Preview")

    st.write(
        f"Rows: {len(df):,} | "
        f"Columns: {len(df.columns)}"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("Dataset Information")

    dataset_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Non-Null Values": df.notna().sum().values,
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(
        dataset_info,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# Price Analysis
# ==========================================

elif page == "Price Analysis":

    st.header("💰 Price Analysis")

    # First row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Price",
            f"${df['price'].mean():,.2f}"
        )

    with col2:
        st.metric(
            "Minimum Price",
            f"${df['price'].min():,.2f}"
        )

    with col3:
        st.metric(
            "Maximum Price",
            f"${df['price'].max():,.2f}"
        )

    # Second row
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Number of Listings",
            f"{len(df):,}"
        )

    with col2:
        st.metric(
            "Average Service Fee",
            f"${df['service fee'].mean():,.2f}"
        )

    st.divider()

    st.subheader("Price Distribution")

    fig = price_distribution(df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================
# Room Analysis
# ==========================================

elif page == "Room Analysis":

    st.header("🏠 Room Type Analysis")

    # Room type summary
    room_summary = (
        df.groupby("room type")
        .agg(
            Listings=("room type", "size"),
            Average_Price=("price", "mean")
        )
        .reset_index()
    )

    room_summary["Average_Price"] = (
        room_summary["Average_Price"]
        .round(2)
    )

    room_summary = room_summary.rename(
        columns={
            "room type": "Room Type",
            "Average_Price": "Average Price"
        }
    )

    st.subheader("Room Type Summary")

    st.dataframe(
        room_summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Number of Listings")

    fig = room_type_distribution(df)

    st.pyplot(
        fig,
        use_container_width=True
        )


    st.subheader("Price by Room Type")

    fig = room_type_price_distribution(df)

    st.pyplot(
        fig,
        use_container_width=True
        )


# ==========================================
# Location Analysis
# ==========================================

elif page == "Location Analysis":

    st.header("📍 Location Analysis")

    # Neighbourhood summary
    location_summary = (
        df.groupby("neighbourhood group")
        .agg(
            Listings=("neighbourhood group", "size"),
            Average_Price=("price", "mean")
        )
        .reset_index()
    )

    location_summary["Average_Price"] = (
        location_summary["Average_Price"]
        .round(2)
    )

    location_summary = location_summary.rename(
        columns={
            "neighbourhood group": "Neighbourhood Group",
            "Average_Price": "Average Price"
        }
    )

    # Sort by number of listings
    location_summary = location_summary.sort_values(
        "Listings",
        ascending=False
    )

    st.subheader("Neighbourhood Summary")

    st.dataframe(
        location_summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Neighbourhood distribution
    st.subheader("Listings by Neighbourhood Group")

    fig = neighbourhood_distribution(df)

    st.pyplot(
        fig,
        use_container_width=True
    )


# ==========================================
# Review Analysis
# ==========================================

elif page == "Review Analysis":

    st.header("⭐ Review Analysis")

    # Review summary
    total_reviews = df["number of reviews"].sum()

    average_reviews = df["number of reviews"].mean()

    listings_with_reviews = (
        (df["number of reviews"] > 0).sum()
    )

    listings_without_reviews = (
        (df["number of reviews"] == 0).sum()
    )

    # First row
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Reviews",
            f"{total_reviews:,.0f}"
        )

    with col2:
        st.metric(
            "Average Reviews per Listing",
            f"{average_reviews:,.2f}"
        )

    # Second row
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Listings with Reviews",
            f"{listings_with_reviews:,}"
        )

    with col2:
        st.metric(
            "Listings without Reviews",
            f"{listings_without_reviews:,}"
        )

    st.divider()

    st.subheader("Reviews Over Time")

    fig = reviews_over_time(df)

    st.pyplot(
        fig,
        use_container_width=True
    )