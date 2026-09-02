#animated thread pendulum
import matplotlib
matplotlib.use("QtAgg")

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Data
l = 1.0         #pendulum length in m
angle = 30      #deflection angle
d = 0.0         #damping
m = 10          #mass in kg
tmax = 15       #simulation duration
g = 9.81        #m/s^2
w02 = g/l       #square of the circular frequency

#solution of the differential equation using the Euler Method
dt = 1e-3       #increment

t = np.arange(0, tmax, dt)

phi_linear, w_linear = np.empty((len(t))), np.empty((len(t)))
phi_euler, w_euler = np.empty((len(t))), np.empty((len(t)))
phi_linear[0], w_linear[0] = np.radians(angle), 0.0     #initial values
phi_euler[0], w_euler[0] = np.radians(angle), 0.0     #initial values

x_linear, y_linear = np.empty((len(t))), np.empty((len(t)))
v_linear = np.empty((len(t)))
x_linear[0] = y_linear[0] = 0

x_euler, y_euler = np.empty((len(t))), np.empty((len(t)))
v_euler = np.empty((len(t)))
x_euler[0] = y_euler[0] = 0


#Euler Numerical Solution Function
def euler(phi, w):
    for i in range(len(t) - 1):
        phi[i+1] = phi[i] + w[i]*dt
        w[i+1] = w[i] - w02*np.sin(phi[i])*dt - d*w[i]*dt

    v = l * w
    x, y = l * np.sin(phi), -l * np.cos(phi)
    
    return x, y, v, phi, w

def linearised(phi, w):
    for i in range(len(t) - 1):
        phi[i+1] = phi[i] + w[i]*dt
        w[i+1] = w[i] - w02*phi[i]*dt - d*w[i]*dt

    v = l * w
    x, y = l * np.sin(phi), -l * np.cos(phi)

    return x, y, v, phi, w

x_euler, y_euler, v_euler, phi_euler, w_euler = euler(phi_euler, w_euler)
x_linear, y_linear, v_linear, phi_linear, w_linear = linearised(phi_linear, w_linear)

def pendulum(j):
#    h = l+y[j]
#
#    Epot = m * h
#    Ekin = m * v[j]**2/2.0
#        
#    txtEpot.set_text(f'$E_{{pot}}$={Epot:3.1f} J')
#    txtEkin.set_text(f'$E_{{kin}}$={Ekin:3.1f} J')

    phi_euler_line.set_data(t[:j], phi_euler[:j])
    phi_linear_line.set_data(t[:j], phi_linear[:j])

    w_euler_line.set_data(t[:j], w_euler[:j])
    w_linear_line.set_data(t[:j], w_linear[:j])

    rod_euler.set_data([0,x_euler[j]],[0,y_euler[j]])
    rod_linear.set_data([0,x_linear[j]],[0,y_linear[j]])

    sphere_euler.set_data([x_euler[j]],[y_euler[j]])
    sphere_linear.set_data([x_linear[j]],[y_linear[j]])

    return {
        rod_euler,
        sphere_euler,

        rod_linear,
        sphere_linear,

        phi_euler_line,
        w_euler_line,

        phi_linear_line,
        w_linear_line,
            }
#Graphics area
fig = plt.figure(figsize = (10,6))

#multiple graphs to show other values
gs = fig.add_gridspec(2,2)
ax_pendulum = fig.add_subplot(gs[:,0])
ax_phi = fig.add_subplot(gs[0, 1])
ax_omega = fig.add_subplot(gs[1,1])

ax_phi.set_xlim(0,tmax)
ax_phi.set_ylim(1.1 * phi_euler.min(), 1.1 * phi_euler.max())

ax_omega.set_xlim(0,tmax)
ax_omega.set_ylim(1.1 * w_euler.min(), 1.1 * w_euler.max())

#quantity graphics
ax_phi.set(xlabel = 't', ylabel ='phi')
ax_omega.set(xlabel='t',ylabel='omega')

phi_linear_line, = ax_phi.plot([],[], 'r--', lw=1, label = 'linearised')
phi_euler_line, = ax_phi.plot([],[], 'r-', lw=1, label = 'numerically solved: Euler')
w_euler_line, = ax_omega.plot([],[], 'b-', lw=1, label = 'numerically solved: Euler')
w_linear_line, = ax_omega.plot([],[], 'b--', lw=1, label = 'linearised')

#pendulum graphics
#txtEpot = ax_pendulum.text(-1,1,'', fontsize = 12)
#txtEkin = ax_pendulum.text(-1,0.85,'',fontsize = 12)

#ival = 1e3*dt

##n = len(y) - 1
width = 1.1*1
ax_pendulum.axis([-width,width,-width,width])
ax_pendulum.set(xlabel='x',ylabel='y')
ax_pendulum.set_aspect('equal')
ax_pendulum.plot(0,0,'ko') #bearing

rod_euler, = ax_pendulum.plot([],[], 'r-', lw=1) #rod
sphere_euler, = ax_pendulum.plot([],[], 'ro', markersize = '15', label = 'numerically solved: Euler') #sphere

rod_linear, = ax_pendulum.plot([],[], 'b-', lw=1) #rod
sphere_linear, = ax_pendulum.plot([],[], 'bo', markersize = '15', label = 'linearised') #sphere

frame_step = 10

ax_pendulum.legend(loc='best')
ax_phi.legend(loc='best')
ax_omega.legend(loc='best')

ani = FuncAnimation(fig, pendulum, frames = range(0, len(t), frame_step), interval = 10, blit = True)
plt.show()

