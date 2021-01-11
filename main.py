import chess
import chess.engine
import chess.pgn

pgn = open("") #path to pgn
first_game = chess.pgn.read_game(pgn)
engine = chess.engine.SimpleEngine.popen_uci("") #path to engine (lc0 in my case)
board = first_game.board()
i = 0
for move in first_game.mainline_moves():
    info = engine.analyse(board, chess.engine.Limit(time=5))
    print()
    print(str(i) + "th move, Score:", info["score"].wdl().white().expectation())
    i += 1
    board.push(move)

engine.quit()
