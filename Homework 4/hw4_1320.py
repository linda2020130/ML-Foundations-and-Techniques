'''
Purpose: To solve question 13-20 of assignment 4 for Machine Learning Foundations on Coursera.
Description: Consider regularized linear regression (also called ridge regression) for classification.
Input: Training dataset is saved and named as 'hw4_dataset_train.csv';
        Testing dataset is saved and named as 'hw4_dataset_test.csv';
Output: Ein and Eout.
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

def ridge(X, Y, lam):
    s = np.dot(X.T, X) + lam*np.eye(len(X[0]))
    return np.dot(np.dot(np.linalg.pinv(s), X.T), Y)

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def errRate(X, Y, w):
    Y_hat = np.array([[sign(y)] for y in np.dot(X, w)])
    errNum = np.sum(Y_hat[:, 0] != Y[:, 0])
    return errNum / len(Y)

def q1318(lam, train, test):
    X_train, Y_train = getdata(train)
    X_test, Y_test = getdata(test)
    w_reg = ridge(X_train, Y_train, lam)
    ein = errRate(X_train, Y_train, w_reg)
    eout = errRate(X_test, Y_test, w_reg)
    print("Ein =", ein)
    print("Eout =", eout)

def q1415(train, test):
    X_train, Y_train = getdata(train)
    X_test, Y_test = getdata(test)
    for i in range(13):
        lam = pow(10, i-10)
        w_reg = ridge(X_train, Y_train, lam)
        ein = errRate(X_train, Y_train, w_reg)
        eout = errRate(X_test, Y_test, w_reg)
        print("log10 lambda =", i-10, "Ein =", ein, "Eout =", eout)

def q1617(train, test):
    X, Y = getdata(train)
    X_train = X[:120, :]
    X_val = X[120:, :]
    Y_train = Y[:120, :]
    Y_val = Y[120:, :]
    X_test, Y_test = getdata(test)
    for i in range(13):
        lam = pow(10, i-10)
        w_reg = ridge(X_train, Y_train, lam)
        etra = errRate(X_train, Y_train, w_reg)
        eval = errRate(X_val, Y_val, w_reg)
        eout = errRate(X_test, Y_test, w_reg)
        print("log10 lambda =", i-10, "Etrain =", etra, "Eval =", eval, "Eout =", eout)

def split_folds(n, X, Y):
    X_val = []
    Y_val = []
    X_train = []
    Y_train = []
    number = len(X) / n
    for i in range(n):
        start = int(number * i)
        end = int(number * (i + 1))
        X_val.append(X[start:end, :])
        Y_val.append(Y[start:end, :])
        X_train.append(np.delete(X, slice(start, end), axis=0))
        Y_train.append(np.delete(Y, slice(start, end), axis=0))
    return X_train, Y_train, X_val, Y_val

def q1920(n, train, test):
    X, Y = getdata(train)
    X_train, Y_train, X_val, Y_val = split_folds(n, X, Y)
    X_test, Y_test = getdata(test)
    for i in range(13):
        lam = pow(10, i-10)
        total = 0
        for j in range(n):
            w_reg = ridge(X_train[j], Y_train[j], lam)
            ein = errRate(X_val[j], Y_val[j], w_reg)
            total += ein
        print("log10 lambda =", i-10, "Ecv =", total/n)



if __name__=='__main__':
    q1318(10, 'hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    q1415('hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    q1617('hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    q1318(1, 'hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    q1920(5, 'hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    q1318(pow(10,-8), 'hw4_dataset_train.csv', 'hw4_dataset_test.csv')
    
    