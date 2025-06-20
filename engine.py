import math
import random


class ConnectNEngine:
    def __init__(self, board_size=5, win_length=3, max_depth=3, player='X', bot='O'):
        self.N = board_size
        self.WIN_LENGTH = win_length
        self.MAX_DEPTH = max_depth
        self.PLAYER = player
        self.BOT = bot
        self.board = [[" " for _ in range(self.N)] for _ in range(self.N)]

    def reset_board(self):
        self.board = [[" " for _ in range(self.N)] for _ in range(self.N)]

    def get_board(self):
        return self.board

    def get_available_moves(self):
        return [(r, c) for r in range(self.N) for c in range(self.N) if self.board[r][c] == " "]

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def check_win(self, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        def in_bounds(r, c):
            return 0 <= r < self.N and 0 <= c < self.N

        for r in range(self.N):
            for c in range(self.N):
                if self.board[r][c] != player:
                    continue
                for dr, dc in directions:
                    count = 0
                    for k in range(self.WIN_LENGTH):
                        nr, nc = r + dr * k, c + dc * k
                        if in_bounds(nr, nc) and self.board[nr][nc] == player:
                            count += 1
                        else:
                            break
                    if count == self.WIN_LENGTH:
                        return True
        return False

    def evaluate_board(self):
        score = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        center = self.N // 2

        def count_sequence(r, c, dr, dc):
            player_count = 0
            bot_count = 0
            empty_count = 0
            for k in range(self.WIN_LENGTH):
                nr, nc = r + dr * k, c + dc * k
                if 0 <= nr < self.N and 0 <= nc < self.N:
                    if self.board[nr][nc] == self.PLAYER:
                        player_count += 1
                    elif self.board[nr][nc] == self.BOT:
                        bot_count += 1
                    else:
                        empty_count += 1
                else:
                    return 0
            if player_count > 0 and bot_count > 0:
                return 0  # blocked
            if bot_count > 0:
                return 100 ** bot_count + (10 * empty_count)
            if player_count > 0:
                return -(150 ** player_count + (15 * empty_count))
            return 0

        for r in range(self.N):
            for c in range(self.N):
                # Center preference bonus
                if self.board[r][c] == self.BOT:
                    dist = abs(r - center) + abs(c - center)
                    score += max(5 - dist, 1) * 10
                elif self.board[r][c] == self.PLAYER:
                    dist = abs(r - center) + abs(c - center)
                    score -= max(5 - dist, 1) * 15
                for dr, dc in directions:
                    score += count_sequence(r, c, dr, dc)
        return score

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_win(self.BOT):
            return 10000 - depth
        if self.check_win(self.PLAYER):
            return -10000 + depth
        if self.is_board_full() or depth == self.MAX_DEPTH:
            return self.evaluate_board()

        if is_maximizing:
            max_eval = -math.inf
            for r, c in self.get_available_moves():
                self.board[r][c] = self.BOT
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.board[r][c] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for r, c in self.get_available_moves():
                self.board[r][c] = self.PLAYER
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.board[r][c] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self, for_bot=True):
        symbol = self.BOT if for_bot else self.PLAYER
        opponent = self.PLAYER if for_bot else self.BOT
        available = self.get_available_moves()
        move_count = len(available)

        # Check for immediate win
        for r, c in available:
            self.board[r][c] = symbol
            if self.check_win(symbol):
                self.board[r][c] = " "
                return (r, c)
            self.board[r][c] = " "

        # Check for immediate block
        for r, c in available:
            self.board[r][c] = opponent
            if self.check_win(opponent):
                self.board[r][c] = " "
                return (r, c)
            self.board[r][c] = " "

        # Adjust depth dynamically
        max_depth = self.MAX_DEPTH
        if move_count < 10:
            max_depth += 2
        elif move_count < 5:
            max_depth += 3

        best_score = -math.inf
        best_moves = []

        for r, c in available:
            self.board[r][c] = symbol
            # Temporarily increase MAX_DEPTH for this call
            original_depth = self.MAX_DEPTH
            self.MAX_DEPTH = max_depth
            score = self.minimax(0, not for_bot, -math.inf, math.inf)
            self.MAX_DEPTH = original_depth
            self.board[r][c] = " "

            if score > best_score:
                best_score = score
                best_moves = [(r, c)]
            elif score == best_score:
                best_moves.append((r, c))

        # Randomize among equally good moves, prefer center-ish
        center = self.N // 2
        random.shuffle(best_moves)
        best_moves.sort(key=lambda m: abs(m[0] - center) + abs(m[1] - center))

        return best_moves[0] if best_moves else None
