import numpy as np 
import csv 


X_train = np.zeros((10000, 1000))
X_pred = np.zeros((10000, 1000))

with open('data_train.csv', 'rt') as csvfile:
	next(csvfile)
	datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
	counting = 0
	for row in datareader:
		delim = ', '
		i,j = row[0].split('r')[1].split('_c')
		i = int(i)-1
		j = int(j)-1
		X_train[i,j] = int(row[1])
		counting += 1

print("We have read the data from our csv, it had #values:")
print(counting)

average = np.mean(X_train[X_train!=0])

print("whats the average?")
print(average)
X_pred[X_train==0] = average
print(X_pred[X_train==0])

print("nonzero values in TRAIN set")
print(len(X_train[X_train!=0]))
print("zero values in TRAIN set")
print(len(X_train[X_train==0.0]))
print("filled values in our pred set")
print(len(X_pred[X_pred!=0.0]))
print("zero vvalues in our pred set")
print(len(X_pred[X_pred==0]))

count = 0
with open('submission.csv', 'wt') as csvfile:
	datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	datawriter.writerow(['Id', 'Prediction'])
	count = 1
	for i in range(0, 10000):
		for j in range(0, 1000):
			val = X_train[i,j]
			if(val != 0):
				s0 = 'r'+str(i+1)+'_c'+str(j+1)
				s1 = str(X_pred[i,j])
				data = [s0, s1]
				datawriter.writerow(data)
				count += 1
				#print(s0)
				#	print(s1)


print("Number of rows is")
print(count)
