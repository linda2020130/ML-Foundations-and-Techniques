'''
Purpose: To solve question 13 of assignment 3 for Machine Learning Foundations on Coursera.
Description: Consider the target function: f(x1,x2)=sign(x2^1+x2^2−0.6)
             Carry out Linear Regression without transformation,i.e., with feature vector: (1, x1, x2), 
             to find the weight w_lin, and use w_lin directly for classification.
Input: Generate a training set of N = 1000 points on X = [-1, 1]X[-1, 1] with uniform probability
        of picking each x∈X. Generate simulated noise by flipping the sign of the output in a random
        10% subset of the generated training set.
Output: average Ein of running experiments for 1000 times.
'''

import numpy as np
import random
import time

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
    x = np.random.uniform(-1,1,(N,2))
    x0 = np.ones((N,1))
    X = np.hstack((x0, x))
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

def q13(n_runs, n_data):
    #time1 = time.time()
    error_sum = 0
    for i in range(n_runs):
        X, Y = generate_data(n_data)
        w = w_LinRrg(X, Y)
        error_sum += error(w, X, Y)
    print(error_sum/n_runs)
    #time2 = time.time()-time1
    #print(time2)

if __name__=='__main__':
    q13(1000, 1000)
    