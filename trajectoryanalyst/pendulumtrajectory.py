import numpy as np
from numpy.linalg import norm
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ______________________________________________________
# _____________________ CONSTANTS ______________________

mi = 1.8*1e-5           # Dynamic viscosity             [kg/(m*s)]
g = 9.80329             # Gravitational acceleration    [m/s^2]
rho = 1.225             # Air density                   [kg/m^3]

# ______________________________________________________
# ____________ PENDULUM PHYSICAL PARAMETERS ____________


l = 0.076               # Pendulum length               [m]
K = 0.05                # Friction coefficient          [1/s]
# Assumed joint friction is linear with angular velocity, K is coefficient

# _________________________________________________________
# ______________________ FUNCTIONS ________________________


def ode(Y,T,K):
    """
        Ordinary differential equation system for a pendulum.
    """
    th, om = Y
    DYDT = [om, -g/l*np.sin(th)-K*(om)]
    return DYDT

# _________________________________________________________
# _________________________ DATA __________________________

# Open measurement file with pandas into a dataframe
measurements = pd.read_csv("PENDULUM.csv")

# Calculate scale factor to transfrom [pixel] to [m]
reference_pixel = (23.25+23.49)/2                   # [pixel]
reference_cm = 12                                   # [cm]
scale_factor = reference_cm/reference_pixel/100     # [m/pixel]

# Retrive x,y axis values from dataframe and convert using scale factor
XX = (measurements["x"].values)*scale_factor
YY = (measurements["y"].values)*scale_factor

# Define time vector using length of XX vector and FPS of camera
FPS = 60
TT = np.arange(1,len(XX)+1,1)/FPS
DT = 1/FPS                                          # Delta-T between frames [s]

# Define initial and end index in order to trim motion to part of interest
init_index = 6#11
end_index = len(XX)-600
A = (max(XX)-min(XX))/2

# Trim time, x and y vectors to the part of interest and setting the (0,0,0) to the intial values
T = TT[init_index:end_index]-TT[init_index]
X = XX[init_index:end_index]-max(XX)+A
Y = YY[init_index:end_index]


# _________________________________________________________
# _________________ VELOCITY DERIVATION ___________________

VX = np.zeros(len(X)-1)
VY = np.zeros(len(X)-1)

for i in range(0,len(X)-1):
    VX[i] = (X[i+1]-X[i])/DT
    VY[i] = (Y[i+1]-Y[i])/DT

AX = np.zeros(len(X)-1)
AY = np.zeros(len(X)-1)

for i in range(0,len(VX)-1):
    AX[i] = (VX[i+1]-VX[i])/DT
    AY[i] = (VY[i+1]-VY[i])/DT


# _________________________________________________________
# __________________ ANGLE CALCULATION ____________________

L = np.zeros(len(X))
TH = np.zeros(len(X))

for i in range(0,len(X)):
    L[i] = norm([X[i],Y[i]])
    TH[i] = np.arctan(X[i]/Y[i])
 

# _________________________________________________________
# _____________________ INTEGRATING _______________________

t = np.arange(0,T[-1]+DT,DT)
y0 = [28.5*np.pi/180,
     -0.5]


sol = odeint(ode,y0,t,atol=1e-12,rtol=1e-13,args=(K,))
th = sol[:,0]
om = sol[:,1]

# No Friction solution
sol_NF = odeint(ode,y0,t,atol=1e-12,rtol=1e-13,args=(0,))
th_NF = sol_NF[:,0]
om_NF = sol_NF[:,1]


# _________________________________________________________
# ______________________ PLOTTING _________________________


plt.figure()
plt.title("Pendulum Angle: Simulation vs. Measurement")
#plt.plot(t,th_NF*180/np.pi,'y',label="Simulation No Friction")
plt.plot(t,th*180/np.pi,'r',label="Simulation")
plt.ylabel('θ [deg]')
plt.xlabel('time [s]')
plt.grid()
plt.plot(T,TH*180/np.pi,'b--',label="Measurement")
plt.legend()
plt.xlim(0,5)


plt.figure()
plt.title("Simulation results")
plt.plot(t,th*180/np.pi,'b',label="Angle")
plt.plot(t,om*180/np.pi,'r--',label="Speed")
plt.grid()
plt.legend()
plt.xlim(0,3)
plt.show()
