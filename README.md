# 🏠 Airbnb Data Analysis

A Python-based data analysis and interactive dashboard project built with **Pandas, Matplotlib, Seaborn, Plotly, and Streamlit**.

The project analyzes Airbnb listing data, performs data cleaning and validation, and presents the results through an interactive web dashboard.

---

## 🌐 Project Overview

This project was developed as a practical **data analysis portfolio project** to demonstrate how Python and Pandas can be used to transform a raw dataset into meaningful business insights and an interactive analytical dashboard.

The application allows users to:

* Load the default Airbnb dataset
* Upload another CSV using the same dataset structure
* Validate required column headings
* Clean and prepare the data
* Explore the dataset
* Analyze listing prices
* Compare room types
* Analyze neighbourhood groups
* Analyze review activity
* View interactive visualizations

---

## ✨ Features

### 📊 Dashboard

Provides a high-level overview of the Airbnb dataset through key performance indicators:

* Total Listings
* Average Price
* Average Service Fee
* Total Reviews
* Number of Room Types
* Number of Neighbourhood Groups

The dashboard also provides data-quality statistics including:

* Rows Before Cleaning
* Rows After Cleaning
* Rows Removed
* Duplicate Records
* Missing Values Before Cleaning
* Missing Values After Cleaning
* Remaining Missing Values by Column

---

### 🔍 Data Preview

Provides access to the cleaned dataset and displays:

* Complete dataset
* Number of rows
* Number of columns
* Column names
* Data types
* Non-null values
* Missing values

---

### 💰 Price Analysis

Analyzes Airbnb listing prices using:

* Average price
* Minimum price
* Maximum price
* Number of listings
* Average service fee
* Interactive price-range Treemap

The Treemap groups listings into price ranges and represents the number of listings through the size of each section.

---

### 🏠 Room Type Analysis

Compares Airbnb listings by room type.

Includes:

* Number of listings by room type
* Average price by room type
* Room type summary table
* Price distribution by room type

---

### 📍 Location Analysis

Analyzes listings by neighbourhood group.

Includes:

* Number of listings by neighbourhood group
* Average price by neighbourhood group
* Neighbourhood summary table
* Listings by neighbourhood group visualization

---

### ⭐ Review Analysis

Examines review activity across the dataset.

Includes:

* Total reviews
* Average reviews per listing
* Listings with reviews
* Listings without reviews
* Reviews over time

---

## 🧹 Data Cleaning

The project includes a dedicated data-cleaning module using Pandas.

The cleaning process includes:

* Converting review dates to datetime
* Handling future review dates
* Filling selected missing values
* Removing records with missing listing or host names
* Removing duplicate records
* Converting price and service-fee fields to numeric values
* Standardizing neighbourhood group names
* Correcting known spelling errors

The application also records statistics before and after cleaning so the effect of the cleaning process can be monitored.

---

## 📁 CSV Validation

Uploaded CSV files are validated before the cleaning process begins.

The application checks whether the uploaded file contains the required Airbnb dataset columns.

If required columns are missing, the application displays a clear table showing which columns are:

* ✅ Found
* ❌ Missing

This prevents incompatible datasets from entering the cleaning and analysis process.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| **Python**       | Application and analysis logic                      |
| **Pandas**       | Data loading, cleaning, transformation and analysis |
| **Matplotlib**   | Data visualization                                  |
| **Seaborn**      | Statistical visualizations                          |
| **Plotly**       | Interactive Treemap                                 |
| **Streamlit**    | Interactive web dashboard                           |
| **Git / GitHub** | Version control and portfolio hosting               |

---

## 📂 Project Structure

```text
Airbnb1/
│
├── data/
│   └── Airbnb_data.csv
│
├── analysis/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   └── analysis.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Overview

**`app.py`**

Main Streamlit application responsible for:

* User interface
* Navigation
* Dataset selection
* Dashboard
* Analysis pages
* Displaying tables and charts

**`analysis/data_loader.py`**

Responsible for loading CSV files into Pandas DataFrames.

**`analysis/data_cleaning.py`**

Responsible for:

* Dataset validation
* Data cleaning
* Missing-value handling
* Duplicate removal
* Data standardization
* Cleaning statistics

**`analysis/analysis.py`**

Contains reusable visualization functions for the analytical pages.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/AftabHussain429/Airbnb-Data-Analysis.git
```

### 2. Navigate to the project

```bash
cd Airbnb-Data-Analysis
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📊 Analysis Workflow

The project follows a simple data-analysis workflow:

```text
Raw CSV Data
     │
     ▼
Load Dataset
     │
     ▼
Validate Columns
     │
     ▼
Clean Data
     │
     ▼
Explore Dataset
     │
     ▼
Analyze Data
     │
     ▼
Create Visualizations
     │
     ▼
Interactive Streamlit Dashboard
```

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

* Python programming
* Pandas
* Data cleaning
* Data validation
* Exploratory data analysis
* Data aggregation
* GroupBy operations
* Missing-value handling
* Duplicate detection
* Data type conversion
* Data visualization
* Interactive dashboards
* Streamlit application development
* Modular Python project structure
* Git and GitHub

---

## 🚀 Future Improvements

Possible future enhancements include:

* Additional interactive filters
* More advanced statistical analysis
* Price analysis by location
* Review and price relationships
* Host-level analysis
* Interactive geographic visualizations
* Additional dashboard KPIs
* Deployment of the Streamlit application
* Improved dashboard styling and theming

---

## 📌 Project Status

**Status: Completed**

The core data loading, validation, cleaning, analysis, visualization, and Streamlit dashboard functionality has been implemented.

---

## 👤 Author

**Aftab Hussain**

GitHub:
https://github.com/AftabHussain429
