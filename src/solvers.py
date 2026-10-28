import numpy as np
import copy
from src.config import Config
from src.geometry import squares_overlap, compute_bounding_box

def generate_initial_grid(n: int) -> np.ndarray:
    """Generates an unrotated square grid packing as a valid baseline."""
    grid_size = int(np.ceil(np.sqrt(n)))
    packing = []
    idx = 0
    for r in range(grid_size):
        for c in range(grid_size):
            if idx >= n:
                break
            # Centers separated by 1.0 unit length
            x = c * 1.0 + 0.5
            y = r * 1.0 + 0.5
            packing.append([x, y, 0.0]) # x, y, angle
            idx += 1
    return np.array(packing)

def optimize_packing_sa(n: int, config: Config) -> np.ndarray:
    """Optimizes packing using Simulated Annealing with spatial pertubations."""
    current_state = generate_initial_grid(n)
    current_energy = compute_bounding_box(current_state)
    
    best_state = copy.deepcopy(current_state)
    best_energy = current_energy
    
    temp = config.INITIAL_TEMP
    
    for iteration in range(config.MAX_ITER_PER_PUZZLE):
        if temp < config.MIN_TEMP:
            break
            
        # Select a random unit square to mutate
        target_idx = np.random.randint(0, n)
        old_square = current_state[target_idx].copy()
        
        # Apply random mutation step within step boundaries
        dx = np.random.uniform(-config.MAX_STEP_SIZE, config.MAX_STEP_SIZE)
        dy = np.random.uniform(-config.MAX_STEP_SIZE, config.MAX_STEP_SIZE)
        d_angle = np.random.uniform(-config.MAX_ANGLE_STEP, config.MAX_ANGLE_STEP)
        
        current_state[target_idx][0] += dx
        current_state[target_idx][1] += dy
        current_state[target_idx][2] = (current_state[target_idx][2] + d_angle) % (2 * np.pi)
        
        # Evaluate validity (Overlap checks)
        overlap = False
        for i in range(n):
            if i != target_idx:
                if squares_overlap(tuple(current_state[target_idx]), tuple(current_state[i])):
                    overlap = True
                    break
                    
        if overlap:
            # Revert step if it triggers overlaps
            current_state[target_idx] = old_square
            continue
            
        # Calculate new container requirement
        new_energy = compute_bounding_box(current_state)
        energy_delta = new_energy - current_energy
        
        # Acceptance Criteria (Metropolis-Hastings)
        if energy_delta < 0 or np.random.rand() < np.exp(-energy_delta / temp):
            current_energy = new_energy
            if current_energy < best_energy:
                best_energy = current_energy
                best_state = copy.deepcopy(current_state)
        else:
            # Revert mutation step if rejected
            current_state[target_idx] = old_square
            
        # Cool down the system parameters
        temp *= config.COOLING_RATE
        
    return best_state
  
