'''
Purpose: To solve question 19 & 20 of assignment 2 for Machine Learning Foundations on Coursera.
Description: Decision stumps can also work for multi-dimensional data. Each decision stump now deals with a
            specific dimension i, as shown below.
            h_s,i,θ(x) = s*sign(xi-θ).
            Implement the following decision stump algorithm for multi-dimensional data:
            a) for each dimension i=1, 2, ..., d, find the best decision stump h_s,i,θ using the one-dimensional
            decision stump algorithm that you have just implemented.
            b) return the "best of best" decission stump in terms of Ein. If there is a tie, please randomly
            choose among the lowest-Ein ones
Input: Training dataset was saved and named as 'hw2_dataset_train.csv';
        Testing dataset was saved and named as 'hw2_dataset_test.csv';
Output: Ein of the optimal decision stump running on D_train and use the returned decision stump to predict the 
        label of each example within D_test and report an estimate of Eout by E_test.
'''

import random
import numpy as np
import pandas as pd


class DecisionStumpMultiDimension():
    def __init__(self, train_path, test_path):
        self.train_path = train_path
        self.test_path = test_path

    

    # Define compute_theta function to compute theta based on given dataset
    def compute_theta(self, dataset, d):
        X = np.sort(dataset[:,d])
        theta = np.empty((len(dataset), 1))
        for i in range(len(dataset)-1):
            theta[i]=(X[i]+X[i+1])/2
        theta[-1] = 1
        return theta

    # Define h function of the hypothesis set
    def h_s_theta(self, s, theta, x):
        return s*np.sign(x-theta)

    def test(self, dataset, theta, s):
        e_out = []
        for i in range(len(dataset[0])-1):
            a = dataset[:, -1]*self.h_s_theta(s, theta, dataset[:, i])
            error = (len(dataset)-np.sum(a)) / 2
            error_rate_out = error / len(dataset)
            e_out.append(error_rate_out)
        return e_out

    # Define model function to run Decision Stump Algorithm 
    def model(self):
        dataset_train = np.array(pd.read_csv(self.train_path, header=None, delim_whitespace=True))
        dataset_test = np.array(pd.read_csv(self.test_path, header=None, delim_whitespace=True))
        e_in = []
        theta_list = []
        s_list = []

        for i in range(len(dataset_train[0])-1):
            theta = self.compute_theta(dataset_train, i)
            error_best = len(dataset_train)
            theta_best = 0
            s_best = 0

            for j in range(len(theta)):
                a = dataset_train[:, -1]*self.h_s_theta(-1, theta[j], dataset_train[:, i])
                error_0 = (len(dataset_train) - np.sum(a)) / 2
                error_1 = (len(dataset_train) - np.sum(-a)) / 2
                if error_0 < error_best:
                    error_best = error_0
                    theta_best = theta[j]
                    s_best = -1
                elif error_1 < error_best:
                    error_best = error_1
                    theta_best = theta[j]
                    s_best = 1
            
            error_rate_in = error_best / len(dataset_train)
            e_in.append(error_rate_in)
            theta_list.append(theta_best[0])
            s_list.append(s_best)

        theta_best = theta_list[np.argmin(e_in)]
        s_best = s_list[np.argmin(e_in)]
        e_out = self.test(dataset_test, theta_best, s_best)

        print(e_in)
        print("Min of Ein: ", np.min(e_in))
        print("Best theta: ", theta_best)
        print("Best s: ", s_best)
        print(e_out)
        print("Eout by formula: ", 0.5+0.3*s_best*(np.abs(theta_best)-1))
        print("Eout by test data: ", np.min(e_out))
            

m = DecisionStumpMultiDimension('hw2_dataset_train.csv', 'hw2_dataset_test.csv')
m.model()
