import time
import random
import numpy as np

def InputEmelMatrix(rows, columns):
    MyMatrix=[]
    for i in range(rows):
        MyMatrix.append([])
        for j in range(columns):
             MyMatrix[i].append(random.randint(-20, 20))                
    return MyMatrix

MyMatrix1 = InputEmelMatrix(666, 666)
MyMatrix1NumPy = np.array(MyMatrix1)

MyMatrix2 = InputEmelMatrix(666, 666)
MyMatrix2NumPy = np.array(MyMatrix2)

# Numpy method
sratTimeNumMethod = time.time()
results = np.dot(MyMatrix1NumPy, MyMatrix2NumPy)
timeNumpy = time.time() - sratTimeNumMethod

# My mult method
ResultMatrix = InputEmelMatrix(666, 666)
sratTimeMyMethod = time.time()
for i in range(len(MyMatrix1)):
   for j in range(len(MyMatrix2[0])):
       for k in range(len(MyMatrix2)):
           ResultMatrix[i][j] += MyMatrix1[i][k] * MyMatrix2[k][j]
timeLoop = time.time() - sratTimeMyMethod


print("Time my method: {:.5f}s ".format(timeLoop))
print("Time Numpy method: {:.5f}s ".format(timeNumpy))