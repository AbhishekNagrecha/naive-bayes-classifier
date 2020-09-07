import csv
import math
import random
def loadCsv(filename):
lines = csv.reader(open(r'C:\Users\Kislay\Desktop\pima-indians-diabetes.data.csv'))
dataset = list(lines)
for i in range(len(dataset)):
dataset[i] = [float(x) for x in dataset[i]]
return dataset