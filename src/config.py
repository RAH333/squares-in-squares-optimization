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
    
"""
# src/config.py (किस्म को अपडेट करें / Update these values)
@dataclass
class Config:
    # ... बाकी कोड समान रहेगा / other parameters stay the same
    
    # इटरेशन बढ़ाएं ताकि एल्गोरिद्म को बारीक स्पेस ढूंढने का मौका मिले
    MAX_ITER_PER_PUZZLE: int = 100000  # 5,000 से बढ़ाकर 100,000 करें
    INITIAL_TEMP: float = 25.0         # तापमान बढ़ाएं ताकि ज्यादा ओरिएंटेशन टेस्ट हों
    COOLING_RATE: float = 0.999        # कूलिंग धीमी करें (Slower cooling for precision)
"""
