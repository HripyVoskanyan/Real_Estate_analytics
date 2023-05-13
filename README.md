# Real_Estate_Analytics

This repository contains code and data about an end-to-end pipeline for storing Armenian Real Estate market with Business Intelligence tools. The code is written in Python and SQL using variety of libraries, data manipulation, and visualization.

### Contents

* data: contains a version of data scraped from websites
* assets: contains information about scraping parameters
* preprocessing: containing .py files for preprocessing
* sql_scripts: contains sql scripts to create, update, and delete tables
* src: contains the main code of scraping

### Requirements
To have the necessary libraries,  run the following code:

`>> pip install -r requirements.txt`

### Scrape and Preprocess
As the data model includes data scraping, the user needs to scrape the data and then preprocess it.
The scripts for that are in scraping and preprocessing folders.
In scraping, run the main.py in terminal:

`>> python main.py`

Please note that you can change the configuration file name to which platform you want to scrape at that moment.
After scraping the necessary data, preprocessing for the data file can be done:

`>> python preprocessing.py`


### Data Warehousing
After scraping the data it needs to be stored in the data warehouse, in this case, it is first archived in Google Drive using the necessary credentials, after which it is ingested into BigQuery project.
After being ingested into staging raw table in BigQuery, it is being ingested into dimensional and fact tables.

If the code is being run for the first time, infrastructure: dim and fact tables should be created, which can be done in this way:

`>> python infrastructure_initiation.py`

After that each time, when the data is being uploaded, flow.py should be run, with the right values to parameters  reload and ingestion_date. If the data is fresh and is being uploaded to dim and fact for the first time
ingestion_date should be given the date it is being ingested. However, in case of errors or other technical problems, when the data is being ingested for the second time during one day: reloaded, reload argument should be given a True value in order
to avoid duplicates. Here is an example:

`>> python flow.py --ingestion_date=2023-05-13 --reload=True`

Please note that there are four types of credential files that one would need to run the codes. Those can be either received via email (hripsime_voskanyan@edu.aua.am) or one can create their own.
Credentials are as follows (naming is done according to my file names, as they are used in the configuration files):

* clients_secrets.json: credentials for accessing the Google oAuth 2.0 client and the particular project. The information in the json are used for authenticating and authorizing access to the user. 
* credentials.json: as the previous one, this is also used for authenticating and authorizing access to Google APIs on behalf of a user.
* capstone-384712.json: these credentials are for a Google Cloud service account. The private key in it is necessary for authenticating the service account and accessing resources within the Google Cloud project.
* my_creds.txt: this is an OAth 2.0 access token. It is used for authenticating and authorizing access to the Google Drive API with the specified scope. It allows the user to make API requests.

### Dashboard
For getting the live data in the dashboard and see it with visuals, download the pbix file into your computer and click on Refresh. After several minutes the dashboard will be up-to-date.

### Test
To check whether there is a data in the table, the following can be done:

`>> python check_data.py`

This gives the first 10 lines of each table.


### Usage
To use this repository, you can clone it to your local machine:
`git clone https://github.com/HripyVoskanyan/Real_Estate_analytics.git

### Contributing
If you want to contribute to this repository, you can fork it and create a pull request with your changes. 
Please make sure to follow the existing code style and add tests for your code and use your credentials for Google Drive and Cloud.
`
