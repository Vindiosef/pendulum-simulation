from dataclasses import dataclass
import numpy as np

@dataclass
class PendulumConfig:
    #parameters
    length: float = 1.0 
    damping: float = 0.6
    mass: float = 10.0
    gravity: float = 9.81
     
    #initial conditions
    angle: float = np.deg2rad(80.0)
    angular_velocity: float = 0
    
    #sim parameters
    duration: float = 15
    dt: float = 1e-2

