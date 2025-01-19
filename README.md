Spotify Data Pipeline for Analytics and Visualization
====================================================

Transforming and Visualizing Spotify Data with AWS
--------------------------------------------------

This project demonstrates an end-to-end **Spotify data pipeline** built with AWS services, processing raw data and enabling queries using **AWS Athena**. The pipeline processes data from **Spotify** (in S3), transforms it, and loads it for querying. The results are saved as CSV files directly in **S3** for further analysis or visualization.

Project Workflow
----------------

1. **Spotify Data Staging in S3**:  
   - Raw **Spotify data** (data have 3 csv files named albums, artists and tracks) is uploaded to an **S3 staging bucket**.

2. **AWS Glue Pipeline**:  
   - **AWS Glue** is used to process and transform the data. This part of the pipeline ensures the raw data is organized and ready for querying.  

3. **AWS Glue Crawler**:  
   - The **Glue Crawler** is used to automatically populate the **Glue Data Catalog** with metadata. The raw data in **S3** is mapped for easy querying.

4. **Data Querying with AWS Athena**:  
   - **AWS Athena** queries the data directly from **S3** based on the metadata catalog, allowing exploration of key metrics like top-streamed tracks, artist engagement, and more. The results of these queries are saved automatically as **CSV files** back to **S3**. Here, only simple queries were made using Limit10
     but any sort of queries can be performed

5. **Exporting Results**:  
   - The query results are stored as CSV files in **S3** and can be downloaded for further analysis or visualization.  

Key Deliverables
----------------

- **Preprocessed Spotify Dataset**: Original dataset, preprocessed and ready for analysis.  
- **Data Pipeline Script**: A script detailing the process, including data transformation and querying with Athena.  
- **Pipeline Diagram**: Visual representation of the data pipeline, illustrating the flow from raw data in S3 to final querying in Athena.  
- **CSV Query Results**: Saved CSV file with query results, ready for further analysis or visualization. You can use quicksight
                          for visualization/or any other visualization tool.  

Technology Stack
----------------

- **AWS S3**: For staging and storing raw Spotify data and saving query results.  
- **AWS Glue**: For data transformation and metadata cataloging.  
- **AWS Glue Crawler**: To map and define schemas for the processed data.  
- **AWS Athena**: For querying data directly in S3 using SQL.  

Getting Started
---------------

Prerequisites
-------------
- **AWS Account** with access to S3, Glue, and Athena.(Free tier works like a charm)  
- **Spotify Data** (original dataset in CSVformat).  
- Basic knowledge of **SQL** for querying in Athena.  

Setup
-----
1. **Upload Spotify Data to S3**:  
   - Upload your raw Spotify dataset into an **S3 bucket**.  

2. **Run AWS Glue Pipeline**:  
   - Use **AWS Glue** to process the raw Spotify data and load it into a data warehouse for querying.  

3. **Run AWS Glue Crawler**:  
   - Configure the **Glue Crawler** to create the metadata catalog for your data.  

4. **Query Data with Athena**:  
   - Run SQL queries in **Athena** to analyze Spotify data and extract meaningful insights. The results will automatically be stored as CSV files in **S3**.  

5. **Export Query Results**:  
   - Access the query results stored as **CSV files** in **S3** for download.  

**This project is for personal showcase purpose only**
