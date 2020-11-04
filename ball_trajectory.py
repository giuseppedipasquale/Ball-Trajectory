import numpy as np
from numpy.linalg import norm
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from ball import Ball

# _______________________________________________________________________________
# _________________________________ CONSTANTS ___________________________________

mi  = 1.8*1e-5            # Dynamic viscosity           [kg/(m*s)]
g   = 9.80329             # Gravitational acceleration  [m/s^2]
rho = 1.225               # Air density                 [kg/m^3]
# _______________________________________________________________________________
# ___________________________ BALL PHYSICAL PARAMETERS __________________________

c  = 0.747                # Ball circumference          [m]
d  = c/np.pi              # Ball diameter               [m]
S  = np.pi*d**2/4         # Ball front area             [m^2]
m  = 0.5                  # Ball mass                   [kg]
Cd = 0.54                 # Drag coefficent
basketball = Ball(m,d,Cd)
# _______________________________________________________________________________
# _________________________________ FUNCTIONS ___________________________________

def ode(Y,T):
    """
        Ordinary differential equation system for a falling body, 
        in this case the ball.
    """
    x,y,u,v = Y
    V = norm([u,v])
    Dx = -0.5*rho*basketball.A*basketball.Cd/basketball.m*V*u
    Dy = -0.5*rho*basketball.A*basketball.Cd/basketball.m*V*v 
    return [u, v, Dx, -g+Dy]
  
# _______________________________________________________________________________
# __________________________________ DATA _______________________________________

# Open measurement file into a dataframe with pandas ____________________________
measurements = pd.read_csv("OUTPUT.csv")

# Calculate scale factor to transfrom [pixel] to [m] ____________________________
reference_pixel = (23.25+23.49)/2                   # [pixel]
reference_cm = 12                                   # [cm]
scale_factor = reference_cm/reference_pixel/100     # [m/pixel]

# Retrive x,y axis values from dataframe and convert using scale factor _________
XX = (measurements["x"].values)*scale_factor
YY = (measurements["y"].values)*scale_factor*1.04

# Define time vector using length of XX vector and FPS of camera ________________
FPS = 60
TT = np.arange(1,len(XX)+1,1)/FPS
DT = 1/FPS                                          # Delta-T between frames [s]

# Define initial and end index in order to trim motion to part of interest ______
init_index = 1#11
end_index = len(XX)-1

# Trim time, x and y vectors to the part of interest and 
# setting the (0,0,0) to the intial values ______________________________________
T = TT[init_index:end_index]-TT[init_index]
X = XX[init_index:end_index]-XX[init_index]
Y = YY[init_index:end_index]-YY[init_index]

# _______________________________________________________________________________
# _____________________________ VELOCITY DERIVATION _____________________________

VX = np.zeros(len(X)-1)
VY = np.zeros(len(X)-1)

for i in range(0,len(X)-1):
    VX[i] = (X[i+1]-X[i])/DT
    VY[i] = (Y[i+1]-Y[i])/DT

# _______________________________________________________________________________
# _____________________________ INTEGRATION SETUP _______________________________

# Creating time vector for integration result ___________________________________
t = np.arange(0,T[-1]+DT,DT)

# Creating vector of intial conditions __________________________________________
initialcondition = [0,
                    0,
                    VX[0], 
                    VY[0]]
# _______________________________________________________________________________
# _______________________________ INTEGRATING ___________________________________

# Solving ordinary differential equation using odeint ___________________________
sol = odeint(ode,initialcondition,t,atol=1e-12,rtol=1e-13)

# Obtaining position and velocity components ____________________________________
x = sol[:,0]
y = sol[:,1]
u = sol[:,2]
v = sol[:,3]

# _______________________________________________________________________________
# _________________________________ PLOTTING ____________________________________

plt.figure()
plt.grid()
plt.plot(x,y,'r.',label="Simulation")
plt.plot(X,Y,'b+',label="Experiment")

fig, (ax1, ax2) = plt.subplots(2)
ax1.grid()
ax1.plot(t,x,'r',label="Simulation")
ax1.plot(T,X,'b+',label="Experiment")
ax1.legend()
ax2.grid()
ax2.plot(t,y,'r',label="Simulation")
ax2.plot(T,Y,'b+',label="Experiment")
ax2.legend()

fig, (ax1, ax2) = plt.subplots(2)
ax1.grid()
ax1.plot(t,u,'r.',label="Simulation")
ax1.plot(T[0:-1],VX,'b+',label="Experiment")
ax1.legend()
ax2.grid()
ax2.plot(t,v,'r.',label="Simulation")
ax2.plot(T[0:-1],VY,'b+',label="Experiment")
ax2.legend()

plt.show()
