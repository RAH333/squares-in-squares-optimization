import numpy as np

def get_square_vertices(x: float, y: float, angle: float) -> np.ndarray:
    """Computes the 4 corners of a rotated unit square given its center and angle."""
    # Local offsets for a unit square (side length = 1) from its center
    local_corners = np.array([
        [-0.5, -0.5],
        [ 0.5, -0.5],
        [ 0.5,  0.5],
        [-0.5,  0.5]
    ])
    
    # Rotation Matrix
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s], [s, c]])
    
    # Rotate and translate
    rotated_corners = np.dot(local_corners, R.T)
    return rotated_corners + np.array([x, y])

def squares_overlap(sq1_params: tuple, sq2_params: tuple) -> bool:
    """
    Checks if two rotated squares overlap using the Separating Axis Theorem (SAT).
    Params structure: (x, y, angle)
    """
    # Quick bounding circle heuristic to bypass heavy math
    dist_sq = (sq1_params[0] - sq2_params[0])**2 + (sq1_params[1] - sq2_params[1])**2
    if dist_sq >= 2.0:  # Maximum distance across diagonals of two touching unit squares is sqrt(2)
        return False
        
    v1 = get_square_vertices(*sq1_params)
    v2 = get_square_vertices(*sq2_params)
    
    # Collate axes to test (normals to the edges of both squares)
    axes = []
    for vertices in [v1, v2]:
        for i in range(4):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % 4]
            edge = p2 - p1
            normal = np.array([-edge[1], edge[0]])
            norm = np.linalg.norm(normal)
            if norm > 0:
                axes.append(normal / norm)
                
    # Project vertices onto axes to evaluate gaps
    for axis in axes:
        proj1 = np.dot(v1, axis)
        proj2 = np.dot(v2, axis)
        
        min1, max1 = np.min(proj1), np.max(proj1)
        min2, max2 = np.min(proj2), np.max(proj2)
        
        # If there is a separating axis gap, they do not overlap
        if max1 <= min2 or max2 <= min1:
            return False
            
    return True

def compute_bounding_box(packing_arr: np.ndarray) -> float:
    """
    Calculates the enclosing axis-aligned square box side length L.
    packing_arr: Array of shape (N, 3) containing rows of [x, y, angle]
    """
    all_vertices = []
    for row in packing_arr:
        all_vertices.append(get_square_vertices(row[0], row[1], row[2]))
    
    all_vertices = np.vstack(all_vertices)
    min_x, max_x = np.min(all_vertices[:, 0]), np.max(all_vertices[:, 0])
    min_y, max_y = np.min(all_vertices[:, 1]), np.max(all_vertices[:, 1])
    
    # Container must contain the spread, and be perfectly square
    L = max(max_x - min_x, max_y - min_y)
    return float(L)
  
