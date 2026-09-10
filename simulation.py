import numpy as np

from config import PendulumConfig
from physics import Single_Pendulum
import solvers

from dataclasses import dataclass

@dataclass
class SimulationResult:
    t: np.ndarray
    state: np.ndarray
    pendulum: object

def run():
    config = PendulumConfig()
    pendulum = Single_Pendulum(config)

    t = np.arange(0,config.duration,config.dt)

    initial_state = np.array([config.angle,config.angular_velocity])

    state = solvers.euler(pendulum.derivatives, initial_state, t)

    return SimulationResult(t=t, state=state, pendulum=pendulum)
