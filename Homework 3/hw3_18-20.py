'''
Purpose: To solve question 18-20 of assignment 3 for Machine Learning Foundations on Coursera.
Description: Implement the fixed learning rate gradient descent algorithm for logistic regression.
            Run the algorithm with η = 0.001(Q18), 0.01(Q19) and T = 2000. Then, in Q20, implement 
            the fixed learning rate stochastic gradient descent algorithm for logistic regression. 
            Instead of randomly choosing n in each iteration, please simply pick the example with
            cyclic order n = 1,2,...,N,1,2,... and run the algorithm with η = 0.001 and T = 2000.
Input: Training dataset is saved and named as 'hw3_dataset_train.csv';
        Testing dataset is saved and named as 'hw3_dataset_test.csv';
Output: What is Eout(g) from your algorithm, evaluated using the 0/1 error on the test set.
'''


import numpy as np
import pandas as pd

def getdata(d_csv):
    data = np.array(pd.read_csv(d_csv, header=None, delim_whitespace=True))
    xn = data[:, :-1]
    x0 = np.ones((len(xn),1))
    X = np.hstack((x0, xn))
    Y = np.array(data[:, -1]).reshape(len(X), 1)
    return X, Y

def sigmoid(s):
    return 1/(1+np.exp(-s))

def grad(T, eta, X, Y):
    w = np.zeros((len(X[0, :]), 1))
    for i in range(T):
        s = -Y*(np.dot(X, w))
        gradEin = (np.sum(sigmoid(s)*-Y*X, axis=0).reshape(len(X[0, :]), 1))/len(Y)
        w -= eta*gradEin
    return w

def StocGradDesc(T, eta, X, Y):
    w = np.zeros((len(X[0, :]), 1))
    n = 0  # for cyclic order n = 1,2,...,N,1,2,...
    for i in range(T):
        s = -Y[n]*(np.dot(X[n, :], w))
        gradEin = (sigmoid(s) * -Y[n] * X[n, :]).reshape(len(X[0, :]), 1)
        w -= eta*gradEin
        n += 1
        n %= len(Y)
    return w

def sign(x):
    if x >= 0.5:
        return 1
    else:
        return -1

def errRate(w, X, Y):
    trans = list(map(sigmoid, np.dot(X, w)))
    Y_hat = np.array([[sign(y)] for y in trans])
    errNum = np.sum(Y_hat[:,0]!=Y[:,0])
    return errNum/len(Y)

def q1819(T, eta, train, test):
    X_train, Y_train = getdata(train)
    X_test, Y_test = getdata(test)
    w = grad(T, eta, X_train, Y_train)
    Eout = errRate(w, X_test, Y_test)
    print(Eout)

def q20(T, eta, train, test):
    X_train, Y_train = getdata(train)
    X_test, Y_test = getdata(test)
    w = StocGradDesc(T, eta, X_train, Y_train)
    Eout = errRate(w, X_test, Y_test)
    print(Eout)


if __name__=='__main__':
    q1819(2000, 0.001, 'hw3_dataset_train.csv', 'hw3_dataset_test.csv')
    q1819(2000, 0.01, 'hw3_dataset_train.csv', 'hw3_dataset_test.csv')
    q20(2000, 0.001, 'hw3_dataset_train.csv', 'hw3_dataset_test.csv')
