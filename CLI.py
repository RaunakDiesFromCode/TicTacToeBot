from engine import ConnectNEngine


def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(cell if cell != " " else "." for cell in row))
    print()


def get_player_move(engine):
    while True:
        try:
            move = input("Enter your move (row col): ").strip().split()
            if len(move) != 2:
                raise ValueError
            r, c = map(int, move)
            if (r, c) in engine.get_available_moves():
                return r, c
            else:
                print("Invalid move. Cell is occupied or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")


def main():
    BOARD_SIZE = 5
    WIN_LENGTH = 3
    engine = ConnectNEngine(board_size=BOARD_SIZE, win_length=WIN_LENGTH)

    print("Welcome to Connect-N!")
    print_board(engine.get_board())

    while True:
        # Player move
        r, c = get_player_move(engine)
        engine.board[r][c] = engine.PLAYER
        print_board(engine.get_board())

        if engine.check_win(engine.PLAYER):
            print("You win!")
            break
        if engine.is_board_full():
            print("It's a draw.")
            break

        # Bot move
        print("Bot is thinking...")
        move = engine.best_move(for_bot=True)
        if move:
            engine.board[move[0]][move[1]] = engine.BOT
            print(f"Bot moves at: {move[0]} {move[1]}")
        else:
            print("Bot skips (no valid moves).")
        print_board(engine.get_board())

        if engine.check_win(engine.BOT):
            print("Bot wins!")
            break
        if engine.is_board_full():
            print("It's a draw.")
            break


if __name__ == "__main__":
    main()
