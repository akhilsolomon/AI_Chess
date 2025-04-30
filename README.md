# Chess AI with Minimax and Alpha-Beta Pruning

## Environment
Used `gym-chess` and `python-chess`.

## Evaluation Function
Material-based scoring:
- Pawn: 1
- Knight/Bishop: 3
- Rook: 5
- Queen: 9
- King: 1000

## Algorithms
1. **Minimax** – depth-limited.
2. **Alpha-Beta Pruning** – optimized minimax.

## Results
- Minimax: Slower, exhaustive.
- Alpha-Beta: Faster, same decision quality.

## Run
```bash
python3 run_minimax.py
python3 run_alphabeta.py
```

## Videos
See `videos/` folder.
