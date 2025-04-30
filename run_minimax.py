import chess
from agents.minimax_agent import minimax

board = chess.Board()

while not board.is_game_over():
    print(board)
    if board.turn == chess.WHITE:
        _, move = minimax(board, 2, True)
    else:
        _, move = minimax(board, 2, False)
    board.push(move)

print("Game Over:", board.result())
