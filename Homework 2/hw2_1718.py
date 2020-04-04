'''
Purpose: To solve question 17 & 18 of assignment 2 for Machine Learning Foundations on Coursera.
Description: Implement the one-dimensional decision stump algorithm on the data set of size 20.
            The model contains hypotheses of the form: h_s,θ(x) = s*sign(x-θ). The chosen dichotomy stands for
            a combination of some "spot"(range of θ) and s, and commonly the median of the range is chosen as
            the θ that realizes the dichotomy.
            Record Ein and compute Eout with the formula 0.5+0.3*s*(|θ|-1). Repeat the experiment 5,000 times
            (including data generation, running the decision stump algorithm, and computing Ein and Eout).
Input: Generate x of size 20 by a uniform distribution in [-1, 1]. Generate y by f(x)=s(x)+noise where s(x)=sign(x) 
        and the noise flips the result with 20% probability. Repeat the experiment 5,000 times.
Output: Average of Ein and average of Eout.
'''

import random
import numpy as np


class DecisionStumpOneDimension():
    def __init__(self, data_size, x_lb, x_ub, noise, run_times):
        self.data_size = data_size
        self.x_lb = x_lb
        self.x_ub = x_ub
        self.noise = noise
        self.run_times = run_times
    
    # Define generate_dataset function to generate random x and y with noise
    def generate_dataset(self):
        dataset = np.empty((self.data_size, 2))
        for i in range(self.data_size):
            x = random.uniform(self.x_lb, self.x_ub)
            y = np.sign(x)*np.sign(random.uniform(0,1)-self.noise)
            data_row = [x, y]
            dataset[i] = data_row
        return dataset

    # Define compute_theta function to compute theta based on given dataset
    def compute_theta(self, dataset):
        X = np.sort(dataset[:,0])
        theta = np.empty((self.data_size, 1))
        for i in range(self.data_size-1):
            theta[i]=(X[i]+X[i+1])/2
        theta[-1] = 1
        return theta

    # Define h function of the hypothesis set
    def h_s_theta(self, s, theta, x):
        return s*np.sign(x-theta)

    # Define model function to run Decision Stump Algorithm 
    def model(self):
        e_in = []
        e_out = []
        for i in range(self.run_times):
            dataset = self.generate_dataset()
            theta = self.compute_theta(dataset)
            error_best = len(dataset)
            theta_best = 0
            s_best = 0

            for j in range(len(theta)):
                a = dataset[:, 1]*self.h_s_theta(-1, theta[j], dataset[:, 0])
                error_0 = (self.data_size - np.sum(a)) / 2
                error_1 = (self.data_size - np.sum(-a)) / 2
                if error_0 < error_best:
                    error_best = error_0
                    theta_best = theta[j]
                    s_best = -1
                elif error_1 < error_best:
                    error_best = error_1
                    theta_best = theta[j]
                    s_best = 1
            
            error_rate_in = error_best / self.data_size
            error_rate_out = 0.5+0.3*s_best*(np.abs(theta_best)-1)
            e_in.append(error_rate_in)
            e_out.append(error_rate_out[0])

        #print(e_in)
        print("Average of Ein: ", sum(e_in)/self.run_times)
        #print(e_out)
        print("Average of Eout: ", sum(e_out)/self.run_times)
            

a = DecisionStumpOneDimension(20, -1, 1, 0.2, 5000)
a.model()