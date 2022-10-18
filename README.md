# crime
Libraries used:
pyspark - for streaming and performing some operations on the RDDs
sklearn - for ML models
json - for reading the RDD in json format
pickle- for saving the trained models in .sav file


Streaming: 
Data from the csv file was streamed to the tcp socket localhost 6100. Those streamed RDDs were captured and analyzed.

Pre-Processing: 
It was observed that the descript column served no purpose as it wasn’t a text classification problem and also the descript column was missing in the test.csv file. So we only considered the rest features. The target variable in this case was the crime category. All of the categorical data were assigned numeric lables as a part of encoding process and these encoded data sets were used for training the models.

Model Construction:
Here we needed an incremental model i.e the ones which allow partial fitting as they had to learn from the live streaming data arriving at different times in batches. We had options of Naïve Bayes, Stochastic Gradient Descent, Kmeans etc. Here we have used Naïve Bayes for this particular project.

Surface Level Implementation:

Feature Extraction:Features were extracted from the RDDs which were converted into data frames and the required columns were selected and preprocessed.
The pre-processed data is transformed into numpy arrays, and is sent to the model to be trained.

Testing: To test the models and access their respective accuracies, we use the test dataset. The model was able to predict the crime category and the maximum accuracy we achieved with Naïve Bayes was around 0.26


Reason behind Design Decisions:
Importing libraries:
We used the Pyspark library since it allows us to develop spark apps with python APIs.

Streaming:
Data Streams have been employed because they allow us to extract and process data in real-time.

Pre-Processing:
We needed the categorical data to be converted into some numeric lables to be supplied to the Naïve Bayes model. And the simplest way was to allot them serial numbers.

Model Construction:
Naïve Bayes is one of the simplest, fast , accurate algorithm and have high accuracy and speed on large datasets

Takeaway From Project:
Working with streaming data and RDDs. 
ML Model training and testin
