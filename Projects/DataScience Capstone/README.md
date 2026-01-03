# 🚀 SpaceX Launch Success Prediction  
### IBM Applied Data Science Capstone Project

> **End-to-end data science project** analyzing SpaceX Falcon 9 launches to understand and predict **first-stage landing success**, a key factor in SpaceX’s reusable rocket strategy.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Repository Structure](#-repository-structure)
- [Data Collection](#-data-collection)
- [Data Wrangling](#-data-wrangling)
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [Interactive Visual Analytics](#-interactive-visual-analytics)
- [Predictive Analysis](#-predictive-analysis)
- [Results & Insights](#-results--insights)
- [Limitations & Future Work](#-limitations--future-work)
- [How to Run](#-how-to-run)
- [Author & Certificate](#-author--certificate)

---

## 📖 Project Overview
This repository contains all work completed for the **IBM Applied Data Science Professional Certificate – Capstone Project**.

The project applies the **full data science lifecycle**:
- Data collection (API & web scraping)
- Data wrangling & feature engineering
- Exploratory data analysis using **SQL & visualization**
- Interactive analytics with **Folium & Plotly Dash**
- Predictive modeling using **machine learning classification**

All notebooks, datasets, dashboards, and the final presentation are included for **peer review and reproducibility**.

---

## 🎯 Business Problem
SpaceX dramatically reduces launch costs by **reusing Falcon 9 first-stage boosters**.  
However, reuse depends on whether the booster lands successfully.

This project answers:
- What factors influence landing success?
- How do **payload mass, orbit type, and launch site** affect outcomes?
- Can landing success be **predicted before launch** using ML?

---

## 🗂 Repository Structure

```text
.
├── 📄 spacex_web_scraped.csv
├── 📄 dataset_part_1.csv
├── 📄 dataset_part_2.csv
├── 📄 dataset_part_3.csv
├── 📄 my_data1.db
│
├── 📓 jupyter-labs-spacex-data-collection-api.ipynb
├── 📓 jupyter-labs-webscraping.ipynb
├── 📓 labs-jupyter-spacex-Data wrangling.ipynb
├── 📓 jupyter-labs-eda-sql-coursera_sqllite.ipynb
├── 📓 edadataviz.ipynb
├── 📓 lab_jupyter_launch_site_location.ipynb
├── 📓 SpaceX_Machine Learning Prediction_Part_5.ipynb
│
├── 📁 foliumDash/
│   ├── spacex-dash-app.py
│   └── spacex_launch_dash.csv
│
├── 📊 Presentation.pptx
└── 📄 README.md
````

---

## 📡 Data Collection

### 🔹 SpaceX REST API

* Notebook: `jupyter-labs-spacex-data-collection-api.ipynb`
* Retrieved launch details, payload mass, booster version, orbit, and landing outcomes.

### 🔹 Web Scraping

* Notebook: `jupyter-labs-webscraping.ipynb`
* Scraped historical launch data from Wikipedia using **BeautifulSoup**.
* Output: `spacex_web_scraped.csv`

---

## 🧹 Data Wrangling

* Notebook: `labs-jupyter-spacex-Data wrangling.ipynb`
* Cleaned missing values and inconsistent records
* Converted landing outcomes to **binary classification**
* Engineered features for ML readiness

---

## 🔍 Exploratory Data Analysis (EDA)

### 📊 Visualization

* Notebook: `edadataviz.ipynb`
* Explored relationships between:

  * Payload Mass & Launch Site
  * Flight Number & Orbit Type
  * Yearly success trends

### 🧮 SQL Analysis

* Notebook: `jupyter-labs-eda-sql-coursera_sqllite.ipynb`
* Database: `my_data1.db`
* Key SQL insights:

  * Success rate by launch site and orbit
  * Payload aggregations
  * First successful ground landing
  * Ranking landing outcomes over time

---

## 🌍 Interactive Visual Analytics

### 🗺 Folium Map

* Notebook: `lab_jupyter_launch_site_location.ipynb`
* Features:

  * Launch site markers
  * Success/failure color coding
  * Distance calculations to coastlines, highways, railways, cities

### 📈 Plotly Dash Dashboard

* Folder: `foliumDash/`
* App file: `spacex-dash-app.py`
* Interactive features:

  * Launch site dropdown
  * Payload range slider
  * Success pie charts & scatter plots

---

## 🤖 Predictive Analysis

* Notebook: `SpaceX_Machine Learning Prediction_Part_5.ipynb`

### Models Implemented

| Model                  | Description                   |
| ---------------------- | ----------------------------- |
| Logistic Regression    | Interpretable linear baseline |
| Support Vector Machine | Kernel-based classifier       |
| Decision Tree          | Rule-based model              |
| K-Nearest Neighbors    | Distance-based model          |

### Methodology

* Feature standardization
* Train/Test split (80/20)
* Hyperparameter tuning with **GridSearchCV**
* Evaluation via accuracy & confusion matrix

---

## 📊 Results & Insights

* All models achieved **~83.33% test accuracy**
* No single model significantly outperformed others
* Payload mass, orbit type, and launch site are key predictors
* Success rate improved substantially over time

---

## ⚠️ Limitations & Future Work

* Limited dataset size
* No weather or sea condition data
* Future improvements:

  * Weather integration
  * Ensemble learning
  * Real-time prediction dashboards
  * Deep learning models

---

## ▶️ How to Run

```bash
pip install pandas numpy scikit-learn seaborn matplotlib plotly dash folium beautifulsoup4
```

To run the dashboard:

```bash
python foliumDash/spacex-dash-app.py
```

---

## 🧾 Presentation

* File: `Presentation.pptx`
* Fully aligned with Coursera peer-review rubric
* Can be exported to PDF for final submission

---

## 👤 Author & Certificate

**IBM Applied Data Science Capstone**
Completed as part of the **IBM Data Science Professional Certificate** on Coursera.

---

⭐ *If you found this project useful, feel free to fork or star the repository.*

```

