import os
import pandas as pd
import numpy as np

def calculate_competition_score(L: float, n: int) -> float:
    """Calculates official competition score formula: L / sqrt(n) - 1"""
    return (L / np.sqrt(n)) - 1.0

def generate_submission_csv(all_results: dict, output_path: str):
    """Parses results library and builds structured dataframe matching target columns."""
    rows = []
    global_id = 0
    
    # Sort keys sequentially to group metrics correctly
    for n in sorted(all_results.keys()):
        packing_arr = all_results[n]
        for square_id, data in enumerate(packing_arr):
            rows.append({
                "id": global_id,
                "n": n,
                "square_id": square_id,
                "x": data[0],
                "y": data[1],
                "angle": data[2]
            })
            global_id += 1
            
    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Submission file written securely to: {output_path}")
  
