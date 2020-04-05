'''
Purpose: To solve question 4 & 5 of assignment 2 for Machine Learning Foundations on Coursera.
Description: There are a number of bounds on the generalization error ε, all holding with probability at least 1-δ.
            Fix d_vc=50, δ=0.05, and plot these bounds as function of N. Which bound is the tightest (smallest)?
Input: d_vc=50, δ=0.05; Try N=10,000 and N=5.
Output: five types of bound.
'''

import sympy
import numpy as np


class Bounds():
    def __init__(self, d_vc, delta, n):
        self.d_vc = d_vc
        self.delta = delta
        self.n = n

    # Original VC Bound
    def originalvc(self):
        return np.sqrt(8/self.n*np.log(4*pow(2*self.n,self.d_vc)/self.delta))

    # Rademacher Penalty Bound
    def rpbound(self):
        N = self.n
        a = np.sqrt(2*np.log(2*N*pow(N,self.d_vc))/N)
        b = np.sqrt(2/N*np.log(1/self.delta))
        c = 1/N
        return a+b+c


    # Parrondo and Van den Broek
    def pavdbbound(self):
        epsilon = sympy.symbols('epsilon')
        a = sympy.solve(epsilon-sympy.sqrt(1/self.n*(2*epsilon+np.log(6*pow(2*self.n,self.d_vc)/self.delta))),epsilon)
        return a[0]


    # Devroye
    def dbound(self):
        epsilon = sympy.symbols('epsilon')
        a = sympy.solve(epsilon-sympy.sqrt(1/(2*self.n)*(4*epsilon*(1+epsilon)+np.log(4)+self.d_vc*sympy.log(self.n**2)-np.log(self.delta))),epsilon)
        return a[0]


    # Varlant VC bound
    def vvcbound(self):
        return np.sqrt(16/self.n*np.log(2*pow(self.n,self.d_vc)/np.sqrt(self.delta)))


    # Output function
    def output(self):
        print("Original VC Bound: ", self.originalvc())
        print("Rademacher Penalty Bound: ", self.rpbound())
        print("Parrondo and Van den Broek: ", self.pavdbbound())
        print("Devroye: ", self.dbound())
        print("Varlant VC bound: ", self.vvcbound())



if __name__ == '__main__':        
    m = Bounds(50, 0.05, 10000.0)
    print("d_vc = {d_vc}, delta = {delta}, N = {N}".format(d_vc=m.d_vc, delta=m.delta, N=m.n))
    m.output()
    print("---------------------------------------------------------")
    m = Bounds(50, 0.05, 5.0)
    print("d_vc = {d_vc}, delta = {delta}, N = {N}".format(d_vc=m.d_vc, delta=m.delta, N=m.n))
    m.output()