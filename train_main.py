import json
from sklearn.model_selection import train_test_split
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql import DataFrame
from pyspark import SparkContext
import train_encoding
import feature_extraction
from pyspark.sql.types import StructField, StructType, StringType,DoubleType,TimestampType
import train_naive


def train(rdd):
	if not rdd.isEmpty():
		data = rdd.collect()
    		#create a data_frame
		data_frame = spark.createDataFrame(data=json.loads(data[0]).values(), schema=sch)
		data_frame=train_encoding.encoding(data_frame)
		print("The dataframe is")
		data_frame.show()
    
		features,target,types=feature_extraction.extract(data_frame)
    
		#Split into training and testing coordinates
		trainingX, testingX, trainingY, testingY = train_test_split(features, target, test_size=0.3, random_state=0)
    
		#Naive Bayes Classifier
		train_naive.Naive(trainingX, testingX, trainingY, testingY,types)
    
  

sch=StructType([ StructField("feature0",StringType()),StructField("feature1",StringType()),StructField("feature2",StringType()),StructField("feature3",StringType()),StructField("feature4",StringType()),StructField("feature5",StringType()),StructField("feature6",StringType()),StructField("feature7",DoubleType()),StructField("feature8",DoubleType())])


sc = SparkContext(appName="crime")
sc.setLogLevel('OFF')
strSpk_context = StreamingContext(sc, batchDuration= 4)
spark = SparkSession.builder.getOrCreate()

#data stream
stream =  strSpk_context.socketTextStream("localhost", 6100)

#rdd operation
stream.foreachRDD(lambda rdd:train(rdd) )


strSpk_context.start()            
strSpk_context.awaitTermination(timeout=450)
print("Training Successful")
strSpk_context.stop()
