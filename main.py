import os
from tqdm import tqdm
from src.config import Config
from src.solvers import optimize_packing_sa
# from src.gpu_solvers import optimize_packing_cuda
from src.geometry import compute_bounding_box
from src.utils import calculate_competition_score, generate_submission_csv

def main():
    cfg = Config()
    results = {}
    total_metric_score = 0.0
    
    print("====== Launching Packing Framework Solver ======")
    
    # Optimize configuration iteratively for all 1000 puzzles
    # (For staging tests change range boundaries to shorter loops like range(1, 5))
    for n in tqdm(range(1, cfg.TOTAL_PUZZLES + 1), desc="Optimizing Packing Sets"):
        optimized_packing = optimize_packing_sa(n, cfg)
        results[n] = optimized_packing
        
        # Calculate scores metrics
        L = compute_bounding_box(optimized_packing)
        puzzle_score = calculate_competition_score(L, n)
        total_metric_score += puzzle_score
        
    print(f"\nOptimization Finished. Collective Cumulative Score Tracker: {total_metric_score:.6f}")
    
    # Build export delivery path
    out_file = os.path.join(cfg.SUBMISSION_DIR, "submission_sa_optimized.csv")
    generate_submission_csv(results, out_file)

if __name__ == "__main__":
    main()
  
