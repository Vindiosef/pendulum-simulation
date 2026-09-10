import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use("QtAgg")

def create_figure():
    fig = plt.figure(figsize=(16,9))

    gs = fig.add_gridspec(2,3)
    
    ax_pendulum = fig.add_subplot(gs[:,0])
    ax_phi = fig.add_subplot(gs[0,1])
    ax_omega = fig.add_subplot(gs[1,1])
    ax_potential_energy = fig.add_subplot(gs[0,2])
    ax_kinetic_energy = fig.add_subplot(gs[1,2])

    return fig, {
            "pendulum" : ax_pendulum,
            "phi"      : ax_phi,
            "omega"    : ax_omega, 
            "potential energy" : ax_potential_energy,
            "kinetic energy"   : ax_kinetic_energy 
            }

def plot_angle(t, state, ax):
    phi = state[:,0]
    ax.plot(t,phi)
    ax.set(xlabel = 'time(s)', ylabel = 'Angle (rad)')

def plot_angular_velocity(t, state, ax):
    omega = state[:,1]
    ax.plot(t,omega)
    ax.set(xlabel = 'time(s)', ylabel = 'Angular Velocity(rad/s)')

def plot_energy(t,energy, ax):
    ax.plot(t,energy)
    ax.set(xlabel = 'time(s)', ylabel = 'Energy(J)')

def animate_pendulum(result):
    t = result.t
    state = result.state
    pendulum = result.pendulum
    
    fig, axes = create_figure()

    plot_angle(t,state,axes["phi"])
    plot_angular_velocity(t,state,axes["omega"])
    plot_energy(t,pendulum.potential_energy(state),axes["potential energy"])
    plot_energy(t,pendulum.kinetic_energy(state),axes["kinetic energy"])
    
    ax = axes["pendulum"]

    ax.set_aspect("equal")
    ax.set_xlim(-1.1 * pendulum.length, 1.1 * pendulum.length)
    ax.set_ylim(-1.1 * pendulum.length, 1.1 * pendulum.length)

    ax.plot(0,0, "ko")

    rod, = ax.plot([],[], "b-")
    bob, = ax.plot([],[], "bo")

    def update(frame):

       x,y = pendulum.position(state[frame])

       rod.set_data([0,x],[0,y])
       bob.set_data([x],[y])

       return rod,bob

    animation = FuncAnimation(fig,update,frames=len(t),interval=10,blit=True)

    plt.show()
