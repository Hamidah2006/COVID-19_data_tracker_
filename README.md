COVID-19 Global Data Tracker

Overview

This project analyzes the global impact of COVID-19 using real-world data from Our World in Data. It provides a comprehensive data analysis report including trends in cases, deaths, and vaccinations across selected countries and over time. The project was developed using Python in a Jupyter Notebook environment, with visualizations created using matplotlib, seaborn, and plotly.


---

Objectives

Import and clean COVID-19 data

Analyze trends in cases, deaths, and vaccinations

Compare metrics across multiple countries

Visualize patterns using graphs and maps

Summarize insights and report findings in a clear and structured notebook



---

Dataset

Source: Our World in Data - owid-covid-data.csv

Format: CSV

Features used: date, location, total_cases, new_cases, total_deaths, new_deaths, total_vaccinations, people_fully_vaccinated_per_hundred, iso_code



---

Tools Used

Python

Jupyter Notebook

Libraries:

pandas – for data manipulation

matplotlib, seaborn – for static plots

plotly – for interactive visualizations

numpy – for numerical operations (if required)




---

Project Structure

1. Data Collection: Download and load COVID-19 data


2. Data Exploration: Examine structure, check for missing values


3. Data Cleaning: Filter relevant countries, handle nulls, convert date


4. EDA: Visualize total cases, deaths, new cases, death rates


5. Vaccination Analysis: Show vaccination progress over time


6. Choropleth Maps (Optional): Global case and vaccine distribution


7. User Input (Optional): Compare data interactively by country/date


8. Insights & Reporting: Narrative summary of trends and findings




---

Insights Extracted

The United States had the highest recorded COVID-19 burden.

India saw rapid vaccine rollout phases after mid-2021.

Kenya had lower absolute case counts but slower vaccine progress.

Death rates decreased as vaccinations increased globally.

Geographic inequality is clearly visible in global vaccine access.



---

How to Run the Project

1. Install Python and Jupyter Notebook (or use Google Colab)


2. Download the owid-covid-data.csv dataset and place it in your project folder


3. Open the .ipynb notebook and run cells sequentially


4. Optional: Interact with user input section for customized country/date queries


5. Export notebook as PDF for final submission




---

Stretch Goals (Implemented Optionally)

User input for dynamic country/date analysis

Interactive Choropleth maps using Plotly



---

Author

Olaniyi Hamidah Olaitan
Biochemistry Student | Aspiring Data Analyst
hamidaholaniyi@gmail.com
