from pyspark.sql import DataFrame
from pyspark.sql.functions import hour, month, year, col,udf
from pyspark.sql.functions import to_timestamp

def encoding(data_frame):
	#encoding functions
	ctg= udf(lambda row : categories.get(row,row))
	dis= udf(lambda row : dist.get(row,row))
	d= udf(lambda row : day.get(row,row))
	
	#value encoding
	data_frame = data_frame.withColumn("feature1", ctg(col("feature1")))
	data_frame = data_frame.withColumn("feature4", dis(col("feature4")))
	data_frame = data_frame.withColumn("feature3", d(col("feature3")))
	data_frame = data_frame.withColumn("Timestamp",to_timestamp(data_frame.feature0))
	data_frame=data_frame.withColumn("Hour",hour(data_frame.Timestamp)).withColumn("Month",month(data_frame.Timestamp)).withColumn("Year",year(data_frame.Timestamp))
	return data_frame
	

#Crime categories

categories = {'ARSON':0,'ASSAULT':1,'BAD CHECKS':2,'BRIBERY':3,'BURGLARY':4,'DISORDERLY CONDUCT':5,'DRIVING UNDER THE INFLUENCE':6, 
'DRUG/NARCOTIC':7,'DRUNKENNESS':8,'EMBEZZLEMENT':9,'EXTORTION':10,'FAMILY OFFENSES':11,'FORGERY/COUNTERFEITING':12,'FRAUD':13,'GAMBLING':14,
'KIDNAPPING':15,'LARCENY/THEFT':16,'LIQUOR LAWS':17,'LOITERING':18,'MISSING PERSON':19,'NON-CRIMINAL':20,'OTHER OFFENSES':21,'PORNOGRAPHY/OBSCENE MAT':22,
'PROSTITUTION':23,'RECOVERED VEHICLE':24,'ROBBERY':25,'RUNAWAY':26,'SECONDARY CODES':27,'SEX OFFENSES FORCIBLE':28,'SEX OFFENSES NON FORCIBLE':29,
'STOLEN PROPERTY':30,'SUICIDE':31,'SUSPICIOUS OCC':32,'TREA':33,'TRESPASS':34,'VANDALISM':35,'VEHICLE THEFT':36,'WARRANTS':37,'WEAPON LAWS':38}

#Unique district names

dist={'BAYVIEW':0,'CENTRAL':1,'INGLESIDE':2,'MISSION':3,'NORTHERN':4,'PARK':5,'RICHMOND':6,'SOUTHERN':7,'TARAVAL':8,'TENDERLOIN':9}

#Days
day={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
