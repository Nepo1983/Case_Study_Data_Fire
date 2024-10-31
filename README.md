# Case_Study_Data_Fire
Case of study to analyse data of fire in San Francisco

## Description
This repository contains the solution for making the fire incidents dataset of San Francisco available in a data warehouse, enabling efficient analysis.

## Solution Overview
- **Data Warehouse**: The data is stored in DuckDB, a fast, in-process SQL OLAP database management system.
- **Dimensions for Aggregation**: Aggregation views are provided for time period, district, and battalion.
- **Daily Updates**: The data model assumes daily updates, and scripts are provided to refresh the DuckDB tables accordingly.

## Repository Structure
- `daily_load_fire_incidents.py`: Python script to load and store data in DuckDB.
- `Data_Of_Fire.ipynb`: Example queries demonstrating data usage.
- `test_daily_load_fire_incidents.py`: Example queries demonstrating data usage.
- `README.md`: Documentation of the solution.

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/Nepo1983/Case_Study_Data_Fire.git

## Plan Overview:
1. Inspect Dataset and Data Dictionary: First, inspect the CSV dataset you provided along with the data dictionary from earlier to understand the fields available and their respective data types.

2. Data Modeling:

- Load the dataset using Pandas and perform initial cleaning if needed.
- Create a schema to define how this data can be represented in DuckDB for efficient querying.

3. Data Warehouse Design:

- Store the data in DuckDB, simulating a data warehouse that supports aggregations along the dimensions of time period, district, and battalion.

4. Dynamic Query Support:

- Create views or helper functions to enable dynamic queries to meet the business intelligence team requirements.
