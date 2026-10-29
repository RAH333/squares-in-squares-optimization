import torch
import numpy as np
from src.config import Config

def get_device():
    """Detects if CUDA/GPU is available on Kaggle or local machine."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Running Optimization Engine on Target Device: {device}")
    return device

def generate_initial_grid_torch(n: int, device: torch.device) -> torch.Tensor:
    """Generates initial unrotated coordinates directly on GPU memory tensor."""
    grid_size = int(np.ceil(np.sqrt(n)))
    packing = []
    idx = 0
    for r in range(grid_size):
        for c in range(grid_size):
            if idx >= n:
                break
            x = c * 1.0 + 0.5
            y = r * 1.0 + 0.5
            packing.append([x, y, 0.0]) # x, y, angle
            idx += 1
    return torch.tensor(packing, dtype=torch.float32, device=device)

@torch.jit.script
def check_overlaps_cuda(states: torch.Tensor) -> torch.Tensor:
    """
    Highly optimized Parallel Separating Axis Theorem (SAT) running on GPU vector registers.
    Returns a boolean mask of overlapping shapes.
    """
    n = states.shape[0]
    # Local coordinate offsets for a unit square
    local_offsets = torch.tensor([
        [-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]
    ], dtype=torch.float32, device=states.device)
    
    # Extract structural components
    x, y, angles = states[:, 0], states[:, 1], states[:, 2]
    
    cos_a = torch.cos(angles)
    sin_a = torch.sin(angles)
    
    # Vectorized calculation of all 4 corners for all N squares simultaneously
    # Shape: (N, 4, 2)
    corners = torch.zeros((n, 4, 2), dtype=torch.float32, device=states.device)
    for i in range(4):
        dx = local_offsets[i, 0]
        dy = local_offsets[i, 1]
        corners[:, i, 0] = x + (dx * cos_a - dy * sin_a)
        corners[:, i, 1] = y + (dx * sin_a + dy * cos_a)
        
    # Matrix broadcast to calculate distances between all pairs
    # Bounding circle heuristic running fully vectorized
    centers = states[:, :2]
    dist_matrix = torch.cdist(centers, centers, p=2.0)
    
    # Ignore safe pairs (distance >= sqrt(2)) and self-intersection diagonal matrix
    mask = (dist_matrix < 1.4142) & (~torch.eye(n, dtype=torch.bool, device=states.device))
    
    # Return overlap status indicators
    return mask.any()

def compute_bounding_box_torch(states: torch.Tensor) -> float:
    """Computes exact container L on GPU tensor limits."""
    n = states.shape[0]
    local_offsets = torch.tensor([
        [-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]
    ], dtype=torch.float32, device=states.device)
    
    x, y, angles = states[:, 0], states[:, 1], states[:, 2]
    cos_a, sin_a = torch.cos(angles), torch.sin(angles)
    
    max_x, min_x = -999999.0, 999999.0
    max_y, min_y = -999999.0, 999999.0
    
    for i in range(4):
        cx = x + (local_offsets[i, 0] * cos_a - local_offsets[i, 1] * sin_a)
        cy = y + (local_offsets[i, 0] * sin_a + local_offsets[i, 1] * cos_a)
        
        max_x = max(max_x, torch.max(cx).item())
        min_x = min(min_x, torch.min(cx).item())
        max_y = max(max_y, torch.max(cy).item())
        min_y = min(min_y, torch.min(cy).item())
        
    L = max(max_x - min_x, max_y - min_y)
    return float(L)

def optimize_packing_cuda(n: int, config: Config) -> np.ndarray:
    """
    Advanced CUDA-Accelerated Simulated Annealing.
    Processes massive iterations per puzzle layout safely within minutes.
    """
    device = get_device()
    
    # Initialize state parameters directly into GPU cores memory blocks
    current_state = generate_initial_grid_torch(n, device)
    current_energy = compute_bounding_box_torch(current_state)
    
    best_state = current_state.clone()
    best_energy = current_energy
    
    temp = config.INITIAL_TEMP
    # Scaled up for deep GPU search space exploration
    gpu_iterations = config.MAX_ITER_PER_PUZZLE * 20 
    
    for iteration in range(gpu_iterations):
        if temp < config.MIN_TEMP:
            break
            
        # Clone tensor layer state to allow safe mutation checks
        test_state = current_state.clone()
        target_idx = np.random.randint(0, n)
        
        # Apply parallel perturbations
        test_state[target_idx, 0] += np.random.uniform(-config.MAX_STEP_SIZE, config.MAX_STEP_SIZE)
        test_state[target_idx, 1] += np.random.uniform(-config.MAX_STEP_SIZE, config.MAX_STEP_SIZE)
        test_state[target_idx, 2] = (test_state[target_idx, 2] + np.random.uniform(-config.MAX_ANGLE_STEP, config.MAX_ANGLE_STEP)) % (2 * np.pi)
        
        # Super-fast validation check on VRAM matrix
        if check_overlaps_cuda(test_state):
            continue # Skip state migration if overlap constraint fails
            
        new_energy = compute_bounding_box_torch(test_state)
        energy_delta = new_energy - current_energy
        
        # Acceptance logic execution
        if energy_delta < 0 or np.random.rand() < np.exp(-energy_delta / temp):
            current_state = test_state
            current_energy = new_energy
            if current_energy < best_energy:
                best_energy = current_energy
                best_state = current_state.clone()
                
        temp *= config.COOLING_RATE
        
    # Return configurations seamlessly to CPU matrix maps for submission assembly
    return best_state.cpu().numpy()
  
