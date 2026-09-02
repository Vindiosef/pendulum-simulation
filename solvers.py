from config import PendulumConfig as config
import numpy as np

w02 = config.gravity / config.length
dt = config.dt
d = config.damping
l = config.length

def time():
    t = np.arange(0, config.duration, config.dt)
    return t

#Euler Numerical Solution Function
def euler(phi, w, t):
    for i in range(len(t) - 1):
        phi[i+1] = phi[i] + w[i]*dt
        w[i+1] = w[i] - w02*np.sin(phi[i])*dt - d*w[i]*dt

    v = l * w
    x, y = l * np.sin(phi), -l * np.cos(phi)
    
    return x, y, v, phi, w

#linearised solution function from small angle formulae
def linearised(phi, w, t):
    for i in range(len(t) - 1):
        phi[i+1] = phi[i] + w[i]*dt
        w[i+1] = w[i] - w02*phi[i]*dt - d*w[i]*dt

    v = l * w
    x, y = l * np.sin(phi), -l * np.cos(phi)

    return x, y, v, phi, w
