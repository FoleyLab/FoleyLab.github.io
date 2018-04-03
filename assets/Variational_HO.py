import numpy as np
from matplotlib import pyplot as plt

### Define constants in natural units
hbar = 1
k = 1
mu = 1
alpha0 = np.sqrt(k*mu/(hbar*hbar))
omega = np.sqrt(k/mu)


x = np.linspace(-20, 20, 500)

def Trial_Wave(alpha, xt):
    return np.exp(-alpha*xt*xt)


def dfdx(ft, xt):
    dx = x[1]-x[0]
    ftp = np.zeros_like(ft)
    for i in range(0,len(ft)):
      if (i<(len(ft)-1)):
        rise = ft[i+1]-ft[i]
        ftp[i] = rise/dx
      else:
        rise = ft[i]-ft[i-1]
        ftp[i] = rise/dx

    return ftp

### given an array of function values ft
### evaluated at values of array xt, find
### the zero in the derivative and return
### the x-value that minimizes ft, the minimum
### in ft, the gradient at min(ft), and the index
### corresponding to the minimum value of the array ft
def FindMin(ft, xt):
    minresults = np.zeros(4)
    ftp = dfdx(ft,xt)
    mingrad = 1000
    minpos = 0
    minidx = 0
    minval = 0
    for i in range(0,len(ftp)):
        if (abs(ftp[i])<mingrad):
            mingrad = abs(ftp[i])
            minpos = xt[i]
            minval = ft[i]
            minidx = i
            
    minresults[0] = mingrad
    minresults[1] = minpos
    minresults[2] = minval
    minresults[3] = minidx
    return minresults

### returns T-hat operator acting upon
### a trial wavefunction (called ft within the function)
def TPhi(ft, xt):
    ftp = dfdx(ft, xt)
    ftpp = dfdx(ftp, xt)
    return -0.5*ftpp

### returns the kinetic energy functional of a trial
### wavefunction (called ft within the function)
def T_Functional(ft, xt):
    tphi = TPhi(ft, xt)
    dx = x[1] - x[0]
    num = 0
    denom = 0
    for i in range(0, len(ft)):
        num = num + ft[i]*tphi[i]*dx
        denom = denom + ft[i]*ft[i]*dx

    return num/denom

### returns the V-hat operator acting upon
### a trial wavefunction (called ft within the function)
def VPhi(ft, xt):
    return 0.5*xt*xt*ft


### returns the potential energy functional of a trial
### wavefunction (called ft within the function)
def V_Functional(ft, xt):
    vphi = VPhi(ft, xt)
    dx = x[1] - x[0]
    num = 0
    denom = 0
    for i in range(0, len(ft)):
       num = num + ft[i]*vphi[i]*dx
       denom = denom + ft[i]*ft[i]*dx

    return num/denom


### create arrays for alpha values 
### T_functional values, V_functional values
### and E_functional values along with true Eg
alpha =  np.zeros(20)
Evals = np.zeros(20)
Tvals = np.zeros(20)
Vvals = np.zeros(20)
Eg    = np.zeros(20)

### loop over various alphas 
for da in range(0,20):

  alpha[da] = 0.05*(da+3)    
  
  ### evaluate trial wavefunction
  Phi_Trial = Trial_Wave(alpha[da], x)
  ### evaluate T_functional
  Tvals[da] = T_Functional(Phi_Trial, x)
  ### evaluate V_functional
  Vvals[da] = V_Functional(Phi_Trial, x)
  ### compute E_Functional
  Evals[da] = Tvals[da] + Vvals[da]
  ### store true ground state energy for validation
  Eg[da] = np.sqrt(k/mu)*0.5


### plot T, V, E, Eg vs alpha
plt.plot(alpha, Evals, 'red', alpha, Tvals, 'blue', alpha, Vvals, 'purple', alpha, Eg, 'black')
plt.show()

### find minimum in E
minimum_array = FindMin(Evals, alpha)
print("Min Gradient", minimum_array[0])
print("Alpha that minimizes Evals is ", minimum_array[1])
print("Minimum Eval is ", minimum_array[1])
print("True Ground State Energy is ",Eg[0])


#Phi_Trial_LA = Trial_Wave(3, x)
#Phi_Trial_SA = Trial_Wave(0.1, x)


#plt.plot(x, Phi_Trial_LA, 'red', x, Phi_Trial_SA, 'blue')
#plt.show()

