Reddit Streaming Project

This repository contains all the files related to a Reddit streaming project. The project involves collecting real-time data from Reddit using a socket streaming method combined with the Reddit API. It includes the data collection process, storage, and analytics.

Data Collection

The data collection process involves two main components: the Reddit listener and the Reddit producer.

Reddit Listener
The Reddit listener component utilizes the PRAW (Python Reddit API Wrapper) library to establish a connection with the Reddit API. It subscribes to specific subreddits or topics of interest and receives real-time data as it becomes available. The listener captures various information such as the post content, author details, timestamp, and associated metadata. It continuously collects data until a specified time duration is reached.

Reddit Producer
The Reddit producer component processes the data received from the Reddit listener. It performs additional actions or transformations on the data as required and sends it to another system, such as a Spark instance or a data processing pipeline, for further analysis. In this project, the producer sends the processed data as JSON strings via a socket connection.



Data Storage: Here, you will find information on the data storage approach used in the project. It covers the database schema, file formats, and any relevant considerations for storing Reddit data efficiently and securely.

Analytics: This section showcases the analytics performed on the collected Reddit data. It includes exploratory data analysis, data visualization, and any specific methodologies or algorithms used for deriving insights from the data. For this section I used pandas, numpy and Spark.
