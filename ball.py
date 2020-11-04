import numpy as np

class Ball:
    """
    Class to represent a Ball
    """
    def __init__(self, m, d, Cd):
        """
        Constructor
        m: Mass of ball (kg)
        d: Diameter of ball (m)
        """
        self._m = m
        self._d = d
        self._A = self._d**2/4*np.pi
        self._Cd = Cd

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
    def Cd(self):
        """Returns Cd, the drag coefficient of the ball"""
        return self._Cd
