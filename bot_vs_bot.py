from engine import ConnectNEngine
import time


def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(cell if cell != " " else "." for cell in row))
    print()



def bot_vs_bot_simulation():
    game = ConnectNEngine(board_size=5, win_length=3, max_depth=3)
    turn = 0

    while True:
        print_board(game.get_board())
        time.sleep(0.5)  # slow down for visibility

        current_bot = game.BOT if turn % 2 == 0 else game.PLAYER
        is_bot_turn = (turn % 2 == 0)
        print(f"{'Bot' if is_bot_turn else 'Player'} ({current_bot}) is thinking...")
        move = game.best_move(for_bot=is_bot_turn)
        if move:
            r, c = move
            game.board[r][c] = current_bot
            print(f"{current_bot} moves at {r},{c}")
        else:
            print(f"{current_bot} has no valid moves!")

        if game.check_win(current_bot):
            print_board(game.get_board())
            print(f"{current_bot} wins!")
            break
        if game.is_board_full():
            print_board(game.get_board())
            print("It's a draw.")
            break

        turn += 1


if __name__ == "__main__":
    bot_vs_bot_simulation()
