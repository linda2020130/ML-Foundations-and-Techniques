'''
Purpose: To solve question 20 of assignment 1 for Machine Learning Foundations on Coursera.
Description: Modify the PLA in question 18 to run for 100 updates instead of 50.
         Run the pocket algorithm with a total of 50 updates on D, and verify the performance 
         of w_pocket using the testing dataset. Please repeat your experiment for 2000 times, 
         each with a different random seed.
Input: Training dataset was saved and named as 'hw1_dataset_train.csv'; 
        Testing dataset was saved and named as 'hw1_dataset_test.csv';
        each line of the dataset contains one (xn, yn) with xn E R^4. 
        The first 4 numbers of the line contains the components of xn orderly, the last name is yn.
Output: The average error rate on the test set.
'''

import numpy as np
import pandas as pd
import os
import random

# Import training and testing dataset from the csv file
# Split into columns by tab or space
dataset_train = pd.read_csv(r'hw1_dataset_train.csv', header=None, delim_whitespace=True)
dataset_test = pd.read_csv(r'hw1_dataset_test.csv', header=None, delim_whitespace=True)
dataset_train.columns=['x1', 'x2', 'x3', 'x4', 'y']
dataset_test.columns=['x1', 'x2', 'x3', 'x4', 'y']

# Split dataset to X and Y
xn_train = dataset_train.iloc[:,:4]
xn_test = dataset_test.iloc[:,:4]
Xn_train = np.array(xn_train)
Xn_test = np.array(xn_test)
y1_train = dataset_train['y']
y1_test = dataset_test['y']
Y_train = np.array(y1_train)
Y_test = np.array(y1_test)

# Add x0=1 to each row of Xn_train and Xn_test
X_train = np.insert(Xn_train, 0, 1, axis=1)
X_test = np.insert(Xn_test, 0, 1, axis=1)

# Define sign function to take sign(0) as -1
def sign(n):
    if n <= 0:
        return -1
    else:
        return 1

# Define mistake function to return mistake number and mistake list
def mistake(w, L, X, Y):
    mistake = 0
    L_mistake = []
    for N in L:
        wx = np.sum(w * X[N])
        if sign(wx) != Y[N]:
            mistake += 1
            L_mistake.append(N)
    return mistake, L_mistake

# Generate empty list to store results
result = []

for i in range(2000):
    update = 0

    # Generate random index list
    random.seed(i)
    L = list(range(len(X_train)))
    L_random = random.sample(L, len(L))

    # Initialize PLA with w=0 and its number of mistakes and list of mistakes
    w = np.zeros(5)
    w_best = np.zeros(5)
    mistake_1, L_mistake_1 = mistake(w, L_random, X_train, Y_train)
    mistake_best = mistake_1
    L_mistake_best = L_mistake_1

    while update < 100:
        for k in L_mistake_1:
            w += Y_train[k]*X_train[k]
            mistake_1, L_mistake_1 = mistake(w, L_random, X_train, Y_train)
            update += 1

            # Pocket Algorithm - choose w with less mistakes
            if mistake_1 < mistake_best:
                w_best = np.copy(w)
                mistake_best = mistake_1
                L_mistake_best = np.copy(L_mistake_1)
                break
            else:
                break
            
    else:
        mistake_test, L_mistake_test = mistake(w_best, L_random, X_test, Y_test)
        error_rate = mistake_test / len(X_test)
        result.append(error_rate)
        print("i: ", i)
        print("mistake_best: ", mistake_best)
        print("mistake_test: ", mistake_test)
        print("error_rate: ", error_rate)

print(result)
print(sum(result)/2000)