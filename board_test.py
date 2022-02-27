import chess

board = chess.Board()

for i in board.legal_moves:
	print(i)

board.push_san("d4")
board.push_san("d5")

print(board)

