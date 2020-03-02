'''
Purpose: To solve question 17 of assignment 1 for Machine Learning Foundations on Coursera.
Description: Implement a version of PLA by visiting examples in fixed, pre-determined random
        cycles throughout the algorithm, while changing the update rule to be wt+1 = wt + n*ynt*xnt
        with n=0.5. Please repeat your experiment for 2000 times, each with a different random seed.
Input: Data set was saved and named as 'hw1_dataset.csv'; each line of the data set contains
        one (xn, yn) with xn E R^4. The first 4 numbers of the line contains the components of xn 
        orderly, the last name is yn.
Output: The average number of updates before the algorithm halts.
'''

import numpy as np
import pandas as pd
import os
import random

# Import data from the csv file
# Split into columns by tab or space
dataset = pd.read_csv(r'hw1_dataset.csv', header=None, delim_whitespace=True)
dataset.columns=['x1', 'x2', 'x3', 'x4', 'y']

xn = dataset.iloc[:,:4]
Xn = np.array(xn)
y1 = dataset['y']
Y = np.array(y1)

# Add x0=1 to each Xn
X = np.insert(Xn, 0, 1, axis=1)

# Define sign function to take sign(0) as -1
def sign(n):
    if n <= 0:
        return -1
    else:
        return 1

# Generate empty list to store results
result = []

for i in range(2000):
    count = 0
    update = 0
    w = np.zeros(5)         # Initialize PLA with w=0
    random.seed(i)
    L = list(range(len(X)))
    L_random = random.sample(L, len(L))         # Generate random index list

    while count < len(X):
        for N in L_random:
            wx = np.sum(w * X[N])

            if sign(wx) == Y[N]:
                count += 1
                if count >= len(X):
                    break
            
            else:
                w += 0.5*Y[N]*X[N]
                update += 1
                count = 0
            
    else:
        result.append(update)
        print("i: ", i)
        print("update: ", update)
        print("count: ", count)

print(result)
print(sum(result)/2000)
