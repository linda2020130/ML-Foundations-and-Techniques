'''
Purpose: To solve question 14-15 of assignment 3 for Machine Learning Foundations on Coursera.
Description: Consider the target function: f(x1,x2)=sign(x2^1+x2^2−0.6)
             Transform the training data into nonlinear feature vector: (1, x1, x2, x1*x2, x1^2, x2^2). 
             Find the vector w that corresponds to the solution of Linear Regression and take it for classification.
Input: Generate a training set of N = 1000 points on X = [-1, 1]X[-1, 1] with uniform probability
        of picking each x∈X. Generate simulated noise by flipping the sign of the output in a random
        10% subset of the generated training set.
Output: 1. Find vector w that can minimize Ein.
        2. Find average over 1000 runs of Eout by generating a new set of 1000 points and adding noise as before.
'''

import numpy as np
import random

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def f(x1, x2):
    return sign(x1*x1+x2*x2-0.6)

def noise(x):
    prob = np.random.rand(1)
    if prob <= 0.1:
        x = -x
    return x

# 使用list包含式來產生隨機資料
def generate_data(N):
    # Nonlinear feature vector as (1, x1, x2, x1*x2, x1^2, x2^2)
    x0 = np.ones((N,1))
    x1 = np.random.uniform(-1,1,(N,1))
    x2 = np.random.uniform(-1,1,(N,1))
    x3 = x1*x2
    x4 = x1*x1
    x5 = x2*x2
    X = np.hstack((x0, x1, x2, x3, x4, x5))
    Y = np.array([[f(i,j)] for i, j in zip(X[:,1], X[:,2])])
    Y_noise = np.array([noise(y) for y in Y])
    return X, Y_noise

'''
# 使用for迴圈來產生隨機資料
# 迴圈速度會比list包含式(list comprehension)還慢
def generate_data(N):
    X=[]
    Y=[]
    for i in range(N):
        x1 = np.random.uniform(-1,1)
        x2 = np.random.uniform(-1,1)
        y = f(x1, x2)
        y = noise(y)
        X.append([1,x1,x2])
        Y.append([y])
    return np.array(X), np.array(Y)
'''

# Pseudo inverse of X = (X^T*X)^(-1)*X^T
def w_LinRrg(X, Y):
    pseudo_inverse=np.linalg.pinv(X)
    w_lin = np.dot(pseudo_inverse,Y)
    return np.array(w_lin)

def error(w, X, Y):
    Y_hat = np.array([[sign(y)] for y in np.dot(X,w)])
    err = np.sum(np.array(Y_hat[:,0])!=np.array(Y[:,0]))
    return err/len(Y)

def q14(n_runs, n_data):
    error_sum = 0
    err_bestrate = 1
    for i in range(n_runs):
        X, Y = generate_data(n_data)
        w = w_LinRrg(X, Y)
        err_rate =error(w, X, Y)
        error_sum += err_rate
        if err_rate < err_bestrate:
            err_bestrate = err_rate
            w_best = np.copy(w)

    #print(error_sum/n_runs)
    #print(err_bestrate)
    print(w_best)

def q15(n_runs, n_data):
    error_sum = 0
    for i in range(n_runs):
        X, Y = generate_data(n_data)
        w = np.array([[-1], [-0.05], [0.08], [0.13], [1.5], [1.5]])
        err_rate =error(w, X, Y)
        error_sum += err_rate

    print(error_sum/n_runs)


if __name__=='__main__':
    q14(1000, 1000)
    q15(1000, 1000)