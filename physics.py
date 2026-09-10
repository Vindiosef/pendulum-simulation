import numpy as np
from dataclasses import dataclass 

class Single_Pendulum():
    def __init__(self, config):
        self.mass = config.mass
        self.length = config.length
        self.damping = config.damping
        self.gravity = config.gravity
    
    #Uses state-space method returning a matrix of d/dt{x\dot}
    def derivatives(self, state):
        phi, omega = state

        dphi = omega
        domega = -(self.gravity/self.length) * np.sin(phi) - self.damping * omega   

        return np.array([dphi,domega])

    def position(self,state):
        phi = np.asarray(state)[...,0]

        x = self.length * np.sin(phi)
        y = -self.length * np.cos(phi)

        return x,y

    def potential_energy(self,state):
        x,y = self.position(state)

        height = self.length + y
        
        return self.mass * self.gravity * height

    def kinetic_energy(self,state):
        omega = np.asarray(state)[...,1]
        
        velocity = self.length * omega
        
        return 0.5 * self.mass * velocity**2





