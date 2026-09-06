from dataclasses import dataclass

@dataclass
class PendulumConfig:
    length: float = 1.0
    angle: float = 120.0
    damping: float = 0.0
    mass: float = 10.0
    duration: float = 15
    gravity: float = 9.81
    dt: float = 1e-3

