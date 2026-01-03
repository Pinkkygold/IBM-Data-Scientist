# 🚀 SpaceX Launch Success Prediction

## IBM Applied Data Science Capstone Project

![IBM](https://img.shields.io/badge/IBM-Applied%20Data%20Science-blue?style=for-the-badge\&logo=ibm)
![Coursera](https://img.shields.io/badge/Coursera-Capstone-0056D2?style=for-the-badge\&logo=coursera)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge\&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-F7931E?style=for-the-badge\&logo=scikit-learn)
![Plotly](https://img.shields.io/badge/Plotly-Dashboards-3F4F75?style=for-the-badge\&logo=plotly)
![Folium](https://img.shields.io/badge/Folium-Maps-77B829?style=for-the-badge)

> **End-to-end data science project** analyzing SpaceX Falcon 9 launches to understand and predict
> **first-stage landing success**, a critical factor in SpaceX’s reusable rocket strategy.

---

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Business Problem](#-business-problem)
* [Repository Structure](#-repository-structure)
* [Data Collection](#-data-collection)
* [Data Wrangling](#-data-wrangling)
* [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
* [Interactive Visual Analytics](#-interactive-visual-analytics)
* [Predictive Analysis](#-predictive-analysis)
* [Results & Insights](#-results--insights)
* [Limitations & Future Work](#-limitations--future-work)
* [How to Run](#-how-to-run)
* [Presentation](#-presentation)
* [Author & Certificate](#-author--certificate)

---

## 📖 Project Overview

This repository contains all work completed for the
**IBM Applied Data Science Professional Certificate – Capstone Project**.

The project follows the **complete data science lifecycle**:

* 📡 Data collection (REST API & web scraping)
* 🧹 Data wrangling & feature engineering
* 🔍 Exploratory Data Analysis (EDA) using **SQL & visualization**
* 🌍 Interactive analytics with **Folium & Plotly Dash**
* 🤖 Predictive modeling using **machine learning classification**

All notebooks, datasets, dashboards, and the final presentation are included for
**peer review, reproducibility, and portfolio demonstration**.

---

## 🎯 Business Problem

SpaceX reduces launch costs by **reusing Falcon 9 first-stage boosters**.
However, reuse is only possible when the booster **lands successfully**.

This project aims to answer:

* What factors influence landing success?
* How do **payload mass**, **orbit type**, and **launch site** affect outcomes?
* Can landing success be **predicted before launch** using machine learning?

---

## 🗂 Repository Structure

```text
.
├── data/
│   ├── spacex_web_scraped.csv
│   ├── dataset_part_1.csv
│   ├── dataset_part_2.csv
│   ├── dataset_part_3.csv
│   └── my_data1.db
│
├── notebooks/
│   ├── jupyter-labs-spacex-data-collection-api.ipynb
│   ├── jupyter-labs-webscraping.ipynb
│   ├── labs-jupyter-spacex-Data_wrangling.ipynb
│   ├── jupyter-labs-eda-sql-coursera_sqllite.ipynb
│   ├── edadataviz.ipynb
│   ├── lab_jupyter_launch_site_location.ipynb
│   └── SpaceX_Machine_Learning_Prediction.ipynb
│
├── dashboard/
│   ├── spacex-dash-app.py
│   └── spacex_launch_dash.csv
│
├── AwabCapstone.pdf(Presentation)
└── README.md
```

---

## 📡 Data Collection

### 🔹 SpaceX REST API

* Notebook: `jupyter-labs-spacex-data-collection-api.ipynb`
* Retrieved:

  * Launch details
  * Payload mass
  * Booster version
  * Orbit type
  * Landing outcomes

### 🔹 Web Scraping

* Notebook: `jupyter-labs-webscraping.ipynb`
* Scraped historical launch data from Wikipedia using **BeautifulSoup**
* Output dataset: `spacex_web_scraped.csv`

---

## 🧹 Data Wrangling

* Notebook: `labs-jupyter-spacex-Data_wrangling.ipynb`
* Tasks performed:

  * Handling missing values
  * Removing inconsistencies
  * Encoding landing outcomes as **binary labels**
  * Feature engineering for machine learning

---

## 🔍 Exploratory Data Analysis (EDA)

### 📊 Visualization

* Notebook: `edadataviz.ipynb`
* Analysis included:

  * Payload mass vs. launch success
  * Orbit type distributions
  * Launch site performance
  * Year-over-year success trends

### 🧮 SQL Analysis

* Notebook: `jupyter-labs-eda-sql-coursera_sqllite.ipynb`
* Database: `my_data1.db`
* Key insights:

  * Success rate by launch site
  * Orbit-level performance
  * Payload aggregations
  * Timeline of first successful landings

---

## 🌍 Interactive Visual Analytics

### 🗺 Folium Map

* Notebook: `lab_jupyter_launch_site_location.ipynb`
* Features:

  * Launch site markers
  * Success/failure color coding
  * Distance calculations to:

    * Coastlines
    * Highways
    * Railways
    * Nearby cities

### 📈 Plotly Dash Dashboard

* Folder: `dashboard/`
* App: `spacex-dash-app.py`
* Interactive components:

  * Launch site dropdown
  * Payload range slider
  * Success pie charts
  * Payload vs. success scatter plots

---

## 🤖 Predictive Analysis

* Notebook: `SpaceX_Machine_Learning_Prediction.ipynb`

### Models Implemented

| Model               | Purpose                       |
| ------------------- | ----------------------------- |
| Logistic Regression | Interpretable baseline model  |
| SVM                 | Kernel-based classification   |
| Decision Tree       | Rule-based learning           |
| K-Nearest Neighbors | Distance-based classification |

### Methodology

* Feature standardization
* Train/Test split (80/20)
* Hyperparameter tuning using **GridSearchCV**
* Evaluation via accuracy & confusion matrices

---

## 📊 Results & Insights

* All models achieved **~83.33% test accuracy**
* No single model dominated performance
* Key predictors:

  * Payload mass
  * Orbit type
  * Launch site
* Landing success **improved significantly over time**

---

## ⚠️ Limitations & Future Work

**Limitations**

* Relatively small dataset
* No weather or sea condition data

**Future Enhancements**

* Weather and environmental data integration
* Ensemble & boosting methods
* Deep learning approaches
* Real-time prediction dashboards

---

## ▶️ How to Run

### Install dependencies

```bash
pip install pandas numpy scikit-learn seaborn matplotlib plotly dash folium beautifulsoup4
```

### Run the dashboard

```bash
python dashboard/spacex-dash-app.py
```

---

## 🧾 Presentation

* File: `Presentation.pptx`
* Fully aligned with **Coursera peer-review rubric**
* Ready for PDF export and academic submission

---

## 👤 Author & Certificate

**IBM Applied Data Science Capstone Project**
Completed as part of the **IBM Data Science Professional Certificate** on Coursera.

---

⭐ *If you found this project useful, feel free to fork, star, or reference it.*

