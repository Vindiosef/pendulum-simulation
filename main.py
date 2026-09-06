#animated thread pendulum
import matplotlib
matplotlib.use("QtAgg")

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import solvers
from config import PendulumConfig as config

tmax = config.duration
t = solvers.time()
angle = config.angle

#Angle graph list set ups
phi_linear, w_linear = np.empty((len(t))), np.empty((len(t)))
phi_euler, w_euler = np.empty((len(t))), np.empty((len(t)))
phi_linear[0], w_linear[0] = np.radians(angle), 0.0     #initial values
phi_euler[0], w_euler[0] = np.radians(angle), 0.0     #initial values

#Pendulum Simulation list set ups
x_linear, y_linear = np.empty((len(t))), np.empty((len(t)))
v_linear = np.empty((len(t)))
x_linear[0] = y_linear[0] = 0

x_euler, y_euler = np.empty((len(t))), np.empty((len(t)))
v_euler = np.empty((len(t)))
x_euler[0] = y_euler[0] = 0

#Energy list and calc setups
e_pot_linear, e_pot_euler = np.empty((len(t))),np.empty((len(t)))
e_kin_linear, e_kin_euler = np.empty((len(t))),np.empty((len(t)))

#Populate list set ups for animation
x_euler, y_euler, v_euler, phi_euler, w_euler, e_pot_euler, e_kin_euler= solvers.euler(phi_euler, w_euler, t)
x_linear, y_linear, v_linear, phi_linear, w_linear, e_pot_linear, e_kin_linear = solvers.linearised(phi_linear, w_linear, t)

def pendulum(j):
    phi_euler_line.set_data(t[:j], phi_euler[:j])
    phi_linear_line.set_data(t[:j], phi_linear[:j])

    w_euler_line.set_data(t[:j], w_euler[:j])
    w_linear_line.set_data(t[:j], w_linear[:j])

    rod_euler.set_data([0,x_euler[j]],[0,y_euler[j]])
    rod_linear.set_data([0,x_linear[j]],[0,y_linear[j]])

    sphere_euler.set_data([x_euler[j]],[y_euler[j]])
    sphere_linear.set_data([x_linear[j]],[y_linear[j]])
    
    e_pot_euler_line.set_data(t[:j], e_pot_euler[:j])
    e_pot_linear_line.set_data(t[:j], e_pot_linear[:j])

    e_kin_euler_line.set_data(t[:j], e_kin_euler[:j])
    e_kin_linear_line.set_data(t[:j], e_kin_linear[:j])
    return {
        rod_euler,
        sphere_euler,

        rod_linear,
        sphere_linear,

        phi_euler_line,
        w_euler_line,

        phi_linear_line,
        w_linear_line,

        e_pot_euler_line,
        e_kin_euler_line,

        e_pot_linear_line,
        e_kin_linear_line
            }
#Graphics area
fig = plt.figure(figsize = (16,9))

#multiple graphs to show other values
gs = fig.add_gridspec(
        2,3, 
       # width_ratios=[2,1,1]
        )
ax_pendulum = fig.add_subplot(gs[:,0])
ax_phi = fig.add_subplot(gs[0, 1])
ax_omega = fig.add_subplot(gs[1,1])
ax_e_pot = fig.add_subplot(gs[0,2])
ax_e_kin = fig.add_subplot(gs[1,2])

#add buffer to line graphs
ax_phi.set_xlim(0,tmax)
ax_phi.set_ylim(1.1 * phi_linear.min(), 1.1 * phi_linear.max())

ax_omega.set_xlim(0,tmax)
ax_omega.set_ylim(1.1 * w_linear.min(), 1.1 * w_linear.max())

ax_e_pot.set_xlim(0, tmax)
ax_e_pot.set_ylim(1.1 * e_pot_linear.min(), 1.1 * e_pot_linear.max())

ax_e_kin.set_xlim(0, tmax)
ax_e_kin.set_ylim(1.1 * e_kin_linear.min(), 1.1 * e_kin_linear.max())

#quantity graphics
ax_phi.set(xlabel = 't', ylabel ='phi')
ax_omega.set(xlabel='t',ylabel='omega')
ax_e_pot.set(xlabel='t',ylabel='Potential Energy')
ax_e_kin.set(xlabel='t',ylabel='Kinetic Energy')

phi_linear_line, = ax_phi.plot([],[], 'r-', lw=1, label = 'linearised')
phi_euler_line, = ax_phi.plot([],[], 'b-', lw=1, label = 'numerically solved: Euler')
w_linear_line, = ax_omega.plot([],[], 'r-', lw=1, label = 'linearised')
w_euler_line, = ax_omega.plot([],[], 'b-', lw=1, label = 'numerically solved: Euler')
e_pot_linear_line, = ax_e_pot.plot([],[], 'r-', lw=1, label = 'linearised')
e_pot_euler_line, = ax_e_pot.plot([],[], 'b-', lw=1, label = 'numerically solved: Euler')
e_kin_linear_line, = ax_e_kin.plot([],[], 'r-', lw=1, label = 'linearised')
e_kin_euler_line, = ax_e_kin.plot([],[], 'b-', lw=1, label = 'numerically solved: Euler')

#pendulum graphics
width = 1.1*1
ax_pendulum.axis([-width,width,-width,width])
ax_pendulum.set(xlabel='x',ylabel='y')
ax_pendulum.set_aspect('equal')
ax_pendulum.plot(0,0,'ko') #bearing

rod_euler, = ax_pendulum.plot([],[], 'b-', lw=1) #rod
sphere_euler, = ax_pendulum.plot([],[], 'bo', markersize = '15', label = 'numerically solved: Euler') #sphere

rod_linear, = ax_pendulum.plot([],[], 'r-', lw=1) #rod
sphere_linear, = ax_pendulum.plot([],[], 'ro', markersize = '15', label = 'linearised') #sphere

frame_step = 10

ax_pendulum.legend(loc='best')
ax_phi.legend(loc='best')
ax_omega.legend(loc='best')
ax_e_pot.legend(loc='best')
ax_e_kin.legend(loc='best')

ani = FuncAnimation(fig, pendulum, frames = range(0, len(t), frame_step), interval = 10, blit = True)
plt.show()

