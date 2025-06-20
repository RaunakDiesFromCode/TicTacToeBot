<div align="left">

# TIC-TAC-TOE BOT

A Python-based Connect-N game engine with support for:

- ✅ Human vs Bot (CLI)
- 🤖 Bot vs Bot Simulation
- 🔍 Minimax with Alpha-Beta Pruning
- ⚙️ Configurable board size and win condition

<p align="left">
    <img src="https://img.shields.io/github/license/RaunakDiesFromCode/TicTacToeBot?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff&label=License&labelColor=gray&message=MIT" alt="MIT License">
    <img src="https://img.shields.io/github/languages/top/RaunakDiesFromCode/TicTacToeBot?style=flat&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/RaunakDiesFromCode/TicTacToeBot?style=flat&color=0080ff" alt="repo-language-count">
</p>

<p align="left">Built with:</p>
<p align="left">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
</div>

<br clear="right">

---

## 🔍 Overview

This project is a **customizable Connect-N game engine** implemented in Python. It supports:

- 🧑‍💻 **Human vs Bot** gameplay via terminal (`cli.py`)
- 🤖 **Bot vs Bot** simulation (`bot_vs_bot.py`)
- 💡 An AI bot powered by **Minimax with Alpha-Beta Pruning**
- ⚙️ **Configurable rules**: board size, win condition, search depth

---

## 🔧 Core Components

- **`engine.py`**
    Self-contained class (`ConnectNEngine`) that handles:
    - Game board creation and reset
    - Move validation
    - Win detection (4 directions)
    - Board evaluation heuristic (favoring center control and winning lines)
    - Minimax algorithm with alpha-beta pruning
    - Move selection logic (winning/blocking/preferred)

- **`cli.py`**
    Text-based interface for a player to challenge the bot:
    - Prompts for moves
    - Handles input validation
    - Displays board with clear formatting
    - Uses the engine to process turns and determine game outcome

- **`bot_vs_bot.py`**
    Simulates a match between two bots:
    - Alternates moves between "X" and "O"
    - Shows board updates with a delay
    - Ends when win or draw is detected

---

## 🧠 AI Behavior

- Dynamically adjusts search depth based on board fullness
- Scores potential sequences:
    - More weight for longer chains
    - Penalizes opponent threats
    - Prioritizes center control
- Blocks immediate threats before computing deep moves

---

## ✅ Strengths

- Clean modular design (engine + interfaces)
- Readable and easy to extend
- No external dependencies
- Works on any terminal with Python 3.7+

---

## 👾 Features

### 🎮 Gameplay Modes

- **Player vs Bot** via CLI (`cli.py`)
- **Bot vs Bot Simulation** (`bot_vs_bot.py`)
- Interactive move prompts with input validation

### 🧠 AI Logic (Bot)

- **Minimax algorithm** with Alpha-Beta pruning
- **Dynamic search depth** adjustment (deeper analysis in late game)
- **Heuristic evaluation**:
    - Rewards chain-building
    - Penalizes threats
    - Prefers center control
- **Immediate threat blocking**
- Randomized move selection among equally good options (with center bias)

### 🛠️ Configuration

- Fully configurable engine:
    - `board_size` (e.g., 3x3, 5x5, etc.)
    - `win_length` (e.g., 3-in-a-row, 4-in-a-row)
    - `max_depth` for Minimax
    - Custom player symbols (`X`, `O`, etc.)

### 🧩 Engine Functionality (`ConnectNEngine`)

- Initialize/reset board
- Generate valid moves
- Detect win/draw states in all directions
- Evaluate board state numerically for AI decision-making

### 📦 Code Design

- **Modular and reusable** engine (`engine.py`)
- Interfaces separated from logic (CLI/simulation)
- No third-party dependencies
- Easy to expand or adapt to GUI, network play, or other games

---

## 📁 Project Structure

```sh
└── TicTacToeBot/
        ├── cli.py
        ├── bot_vs_bot.py
        └── engine.py
```

---

## ▶️ Getting Started

### 1. Clone or download the repo

Make sure all files are in the same folder:

- `engine.py`
- `cli.py`
- `bot_vs_bot.py`

### 2. Run Player vs Bot (CLI)

```bash
python cli.py
```

- You'll play as `X`, bot is `O`.
- Enter moves in the format: `row col` (e.g., `1 2`)

### 3. Run Bot vs Bot Simulation

```bash
python bot_vs_bot.py
```

- Bots alternate turns.
- Automatically prints the board and shows the result.

---

## 📝 Requirements

- Python 3.7 or higher
- No external libraries needed

---

1. **Fork the Repository**: Fork the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine.

    ```sh
        git clone https://github.com/RaunakDiesFromCode/TicTacToeBot
    ```

3. **Create a New Branch**: Work on a new branch with a descriptive name.

    ```sh
        git checkout -b new-feature-x
    ```

4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message.

    ```sh
        git commit -m 'Implemented new feature x.'
    ```

6. **Push to GitHub**: Push the changes to your forked repository.

    ```sh
        git push origin new-feature-x
    ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

<details>
<summary>Contributor Graph</summary>
<br>
<p align="left">
     <a href="https://github.com/RaunakDiesFromCode/TicTacToeBot/graphs/contributors">
            <img src="https://contrib.rocks/image?repo=RaunakDiesFromCode/TicTacToeBot" alt="Contributors">
     </a>
</p>
</details>

---

## 🎗 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). See the [LICENSE](https://github.com/RaunakDiesFromCode/TicTacToeBot/blob/main/LICENSE) file for details.

---

