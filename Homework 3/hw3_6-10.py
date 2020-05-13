'''
Purpose: To solve question 6 - 10 of assignment 3 for Machine Learning Foundations on Coursera.
Description: Consider a function E(u,v)=e^u+e^2v+e^uv+u^2−2uv+2v^2−3u−2v.
'''

import numpy as np

class GDA():
    def e(self, u, v):
        return np.exp(u)+np.exp(2*v)+np.exp(u*v)+u*u-2*u*v+2*v*v-3*u-2*v

    def gradu(self, u, v):
        return np.exp(u)+np.exp(u*v)*v+2*u-2*v-3

    def gradv(self, u, v):
        return np.exp(2*v)*2+np.exp(u*v)*u-2*u+4*v-2

    def guu(self, u, v):
        return np.exp(u)+v*v*np.exp(u*v)+2

    def gvv(self, u, v):
        return 4*np.exp(2*v)+u*u*np.exp(u*v)+4
    
    def guv(self, u, v):
        return u*v*np.exp(u*v)+np.exp(u*v)-2

    # Gradient of function E(u,v) around (u,v)
    def q6(self, u, v):
        print(self.gradu(u, v), self.gradv(u, v))

    # Update rule of gradient descent algorithm is (u_t+1,v_t+1)=(u_t,v_t)-η∇E(u_t,v_t)
    # Start from (u0,v0)=(0,0) and fix η=0.01, update n times
    def q7(self, u, v, n):
        for i in range(n):
            u = u - 0.01*self.gradu(u, v)
            v = v - 0.01*self.gradv(u, v)
        print(self.e(u, v))

    # Approximate E(u+Δu,v+Δv) by E2(Δu,Δv) 
    # where E2 is the second-order Taylor's expansion of E around (u,v)
    def q8(self, u, v):
        buu = self.guu(u,v)/2   # 泰勒展開式中的二次項有係數:1/2
        bvv = self.gvv(u,v)/2   # 泰勒展開式中的二次項有係數:1/2
        buv = self.guv(u,v)     # 泰勒展開式中的二次項中間項有係數:(1/2)*2
        bu = self.gradu(u,v)
        bv = self.gradv(u,v)
        b = self.e(u,v)
        print(buu, bvv, buv, bu, bv, b)

    # Use the Newton direction without η for updating and start from (u0,v0)=(0,0)
    # Hessian matrix = ∇^2E(u,v)
    # Newton Direction(Δu,Δv) = -(∇^2E(u,v))^(-1)*∇E(u,v)
    def q10(self, u, v, n):
        for i in range(n):
            hession = np.array([[self.guu(u,v), self.guv(u,v)],[self.guv(u,v), self.gvv(u,v)]])
            grad = np.array([[self.gradu(u,v)], [self.gradv(u,v)]])
            delta = np.dot(np.linalg.inv(hession),grad)
            u = u - delta[0][0]
            v = v - delta[1][0]
        print(self.e(u,v))


if __name__ == '__main__':
    m = GDA()
    m.q6(0,0)
    m.q7(0,0,5)
    m.q8(0,0)
    m.q10(0,0,5)