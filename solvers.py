import numpy as np

#Euler Numerical Solution Function
def euler(derivatives, initial_state, t):
    #state = (t, [phi, omega])
    state = np.empty((len(t),len(initial_state)))
    
    state[0]=initial_state

    for i in range(len(t)-1):
        dt = t[i+1] - t[i]
        state[i+1] = state[i] + derivatives(state[i]) * dt

    return state

