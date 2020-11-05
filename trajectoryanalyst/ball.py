import numpy as np

class Ball:
    """
    Class to represent a Ball
    """
    def __init__(self, m, d, C_d):
        """
        Constructor
        m: Mass of ball (kg)
        d: Diameter of ball (m)
        C_d: Drag coefficient
        """
        self._m = m
        self._d = d
        self._A = self._d**2/4*np.pi
        self._C_d = C_d

    @property
    def m(self):
        """Returns m, the mass of the ball"""
        return self._m
    
    @property
    def d(self):
        """Returns d, the diameter of the ball"""
        return self._d

    @property
    def A(self):
        """Returns A, the area of the ball"""
        return self._A
        
    @property
    def C_d(self):
        """Returns Cd, the drag coefficient of the ball"""
        return self._C_d
