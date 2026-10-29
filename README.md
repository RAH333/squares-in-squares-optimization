# squares-in-squares-optimization
Decades-old open combinatorial geometry problem solved using Meta-heuristics and Simulated Annealing on Kaggle.

implementing a hybrid approach of Grid-Initialization paired with Simulated Annealing (with Rotations
```
squares-in-squares-optimization/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── gpu_solvers.py     # नया: CUDA Accelerated PyTorch packing engine
│   ├── config.py          # Global constants, hyper-parameters, and file paths
│   ├── geometry.py        # Core overlap checks, container size computation, and coordinate math
│   ├── solvers.py         # Simulated Annealing engine and packing algorithms
│   └── utils.py           # Exporters, submission CSV generators, and metrics calculation
│
├── data/
│   └── sample_submission.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── main.py                # Central orchestrator to run optimization profiles
└── submit.py              # Verification tool and sub-file packager
```
