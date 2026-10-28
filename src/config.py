import os
from dataclasses import dataclass

@dataclass
class Config:
    # Directories
    DATA_DIR: str = "data"
    SUBMISSION_DIR: str = "submissions"
    
    # Competition constraints
    TOTAL_PUZZLES: int = 1000
    
    # Simulated Annealing Hyperparameters
    INITIAL_TEMP: float = 10.0
    COOLING_RATE: float = 0.995
    MIN_TEMP: float = 1e-5
    MAX_ITER_PER_PUZZLE: int = 5000
    MAX_STEP_SIZE: float = 0.2
    MAX_ANGLE_STEP: float = 0.15  # In Radians
