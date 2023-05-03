# Real_Estate_Analytics

This repository contains code and data about an end-to-end pipeline for storing Armenian Real Estate market with Business Intelligence tools. The code is written in Python and SQL using variety of libraries, data manipulation, and visualization.

### Contents

* data: contains a version of data scraped from websites
* assets: contains information about scraping parameters
* preprocessing: containg .py files for preprocessing
* sql_scripts: contains sql scripts to create, update, and delete tables
* src: contains the main code of scraping

### Requirements
To have the necessary libraries run the following code:
`pip install -r requirements.txt`

### Scrape and Preprocess
To scrape and preprocess the data run `main.py` and `preprocessing.py`.

### Data Warehousing
In order to store the data into its place, run in the python console `infrastructure_initiation.py` only for the first time. However, please note, that it was already created and in order not to lose the data you need to skip this step.
Afterwards, just run `tasks.py`, which will store the data in the right tables.

### Dashboard
For getting the live data in the dashboard, download the pbix file into your computer and click on Refresh. After several minutes the dashboard will be up-to-date.

### Usage
To use this repository, you can clone it to your local machine:
`git clone https://github.com/HripyVoskanyan/Real_Estate_analytics.git

### Contributing
If you want to contribute to this repository, you can fork it and create a pull request with your changes. 
Please make sure to follow the existing code style and add tests for your code and use your credentials for Google Drive and Cloud.
`
