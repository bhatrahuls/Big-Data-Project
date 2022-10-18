import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def Naive(trainingX, testingX, trainingY, testingY,types):
	nb = GaussianNB()
	nb.partial_fit(trainingX,trainingY,classes = types)
	predictedY = nb.predict(testingX)
	print("Naive Bayes:")
	print("Accuracy of the model: ",accuracy_score(predictedY,testingY))
	print("Classification report:")
	print(classification_report(testingY,predictedY,labels=types))
	nb = accuracy_score(predictedY,testingY)   
		
	#saving Models 
	pickle.dump(nb, open('naive.sav', 'wb'))
