import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation




### Function that takes in a list of x-coordinates, the quantum number, and the length L
### and returns PIB energy eigenfunction
def PIB_Func(x, n, L):
    psi_n = np.sqrt(2./L)*np.sin(n*np.pi*x/L)
    return psi_n

### Function that takes in a list of x-coordinates, a central x value, and central momentum value, 
### and a standard deviation for the position and returns complex-valued Gaussian wavepacket
def Gauss_Packet(x, x0, sig, k0):
    ci = 0.+1j
    pre = 1./(sig*np.sqrt(2.*np.pi))
    psi_x = pre*np.exp(-0.5*( (x-x0)/sig )**2)*np.exp(ci*k0*x)
    return psi_x

### Given a complex-valued wavefunction (PsiX), list of x-coordinates (x) between 0 and L, 
### and list of quantum numbers, will return a list of complex expansion coefficients
### to expand PsiX in terms of PIB energy eigenfunctions
def FourierAnalysis(x, PsiX, n, L):
    cn = np.zeros(len(n),dtype=complex)
    dx = x[1]-x[0]
    for i in range (0,len(cn)):

      som = 0+0j
      psi_i = PIB_Func(x, n[i], L)

      ## Numerically integrate psi_n^* Psi dx from 0 to L
      for j in range (0, len(x)):
        som = som + psi_i[j]*PsiX[j]*dx

      cn[i] = som

    return cn

### Give a quantum number n and a length L, return the energy 
### of an electron in a box of length L in state n
def PIB_En(n, L):
    En = (n*n * np.pi*np.pi)/(2*L*L)
    return En


#### Initialize variables for Length of the box and the x-grid for the box here!
L = 500
x = np.linspace(0, L, 2000)
#### define properties of the initial Gaussian wavepacket, including
#### spread in space, sigma, mean position, x0, and mean momentum, k0
x0 = 200.
k0 = 0.4
sig = 15.

### Build the wavepacket!
Psi = Gauss_Packet(x, x0, sig, k0)

### Create a complex array that contains the Gaussian wavepacket
### values evaluated along the x-grid
psi_exp = np.zeros(len(x),dtype=complex)

### create an array of PIB quantum numbers... the
### length of this list will define the number of
### terms in the expansion of the Gaussian Wavepacket
### in the basis of PIB energy eigenfunctions
n = np.linspace(1, 100, 100)

### Determine the complex expansion coefficient for
### each PIB energy eigenfunction to approximate the Guassian Wavepacket
cn = FourierAnalysis(x, Psi, n, L)

### Build the expansion!
for i in range(0,len(cn)):
    psi_exp = psi_exp + cn[i]*PIB_Func(x, n[i], L)

### Plot the original wavepacket and the expansion 
plt.plot(x, np.real(Psi), 'b--', x, np.real(psi_exp), 'red')
plt.show()

