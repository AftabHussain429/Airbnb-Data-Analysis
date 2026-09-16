import pandas as pd

REQUIRED_COLUMNS = [
    "NAME",
    "host name",
    "neighbourhood group",
    "room type",
    "price",
    "service fee",
    "last review",
    "review per month",
    "number of reviews"
]

def validate_columns(df):
    """
    Check whether the DataFrame contains all required columns.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    return missing_columns

def clean_data(df):

    # -----------------------------
    # Statistics before cleaning
    # -----------------------------

    rows_before = len(df)
    duplicates_before = df.duplicated().sum()
    missing_before = df.isnull().sum().sum()

    # -----------------------------
    # Convert last review to datetime
    # -----------------------------

    df["last review"] = pd.to_datetime(
        df["last review"],
        errors="coerce"
    )

    # Change future dates to current date
    today = pd.Timestamp.now().normalize()

    df["last review"] = df["last review"].where(
        df["last review"] <= today,
        today
    )

    # Fill empty cells
    df.fillna(
        {
            "review per month": 0,
            "last review": df["last review"].min()
        },
        inplace=True
    )

    # Delete rows where NAME or host name is empty
    df.dropna(
        subset=["NAME", "host name"],
        inplace=True
    )

    # Delete duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert price
    df["price"] = pd.to_numeric(
        df["price"].replace(r"[\$,]", "", regex=True),
        errors="coerce"
    )

    # Convert service fee
    df["service fee"] = pd.to_numeric(
        df["service fee"].replace(r"[\$,]", "", regex=True),
        errors="coerce"
    )

    # Standardize neighbourhood group
    df["neighbourhood group"] = (
        df["neighbourhood group"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # Correct known spelling mistakes
    df.loc[
        df["neighbourhood group"] == "Brookln",
        "neighbourhood group"
    ] = "Brooklyn"

    df.loc[
        df["neighbourhood group"] == "Manhatan",
        "neighbourhood group"
    ] = "Manhattan"

    # -----------------------------
    # Statistics after cleaning
    # -----------------------------

    rows_after = len(df)
    missing_after = df.isnull().sum().sum()

    cleaning_stats = {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "rows_removed": rows_before - rows_after,
        "duplicates_before": duplicates_before,
        "missing_before": missing_before,
        "missing_after": missing_after,
    }

    return df, cleaning_stats
