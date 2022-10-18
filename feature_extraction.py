import numpy 
import pickle
from pyspark.sql import DataFrame

def extract(data_frame):
	req_features = ['feature3','feature4','feature7','feature8','Hour','Month','Year']
	features = data_frame.select([i for i in req_features])
	target = data_frame.select('feature1')
    
	#Converts them to array
	features = numpy.asarray(features.collect())
	target= numpy.asarray(target.collect())
	#print(numpy.unique(target))
    
	types = [str(a) for a in range(39)]
	#print("types: ",types)
	return(features,target,types)
