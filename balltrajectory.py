import numpy as np
from numpy.linalg import norm
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ______________________________________________________
# _____________________ CONSTANTS ______________________

mi = 1.8*1e-5           # Dynamic viscosity         [kg/(m*s)]
g = 9.80329             # Gravitational acceleration[m/s^2]
rho = 1.225             # Air density               [kg/m^3]

# ________________________________________________________
# ______________ BALL PHYSICAL PARAMETERS ________________

c = 0.747               # Ball circumference        [m]
d = c/np.pi             # Ball diameter             [m]
S = np.pi*d**2/4        # Ball front area           [m^2]
m = 0.5                 # Ball mass                 [kg]
Cd = 0.54               # Drag coefficent
