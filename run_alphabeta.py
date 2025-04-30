import chess
from agents.alphabeta_agent import alphabeta

board = chess.Board()

while not board.is_game_over():
    print(board)
    if board.turn == chess.WHITE:
        _, move = alphabeta(board, 2, float('-inf'), float('inf'), True)
    else:
        _, move = alphabeta(board, 2, float('-inf'), float('inf'), False)
    board.push(move)

print("Game Over:", board.result())
