        __________________________________________________________________________________________                                                  
        _______ __                  _______                          ________                                                                     
       |       \  \                |       \                        |        \
        \▓▓▓▓▓▓▓▓\▓▓ _______        \▓▓▓▓▓▓▓▓ ______   _______        \▓▓▓▓▓▓▓▓ ______   ______
        | ▓▓  |  \/       \______   | ▓▓   |      \ /       \______   | ▓▓   /      \ /      \
        | ▓▓  | ▓▓  ▓▓▓▓▓▓▓      \  | ▓▓    \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓      \  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\
        | ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓   /      ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓
        | ▓▓  | ▓▓ ▓▓_____          | ▓▓  |  ▓▓▓▓▓▓▓ ▓▓_____          | ▓▓  | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓
        | ▓▓  | ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \
        \▓▓   \▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓▓  by BlessCoffee
        __________________________________________________________________________________________

A terminal-based Tic-Tac-Toe game built in Python. This is a learning project to practice Python fundamentals and create a simple interactive game.

> **"Tic Tac Toe is a 3×3 dopamine cage match. X vs O. Turn-based beef. First to stack three goes galaxy brain, loser stares at the grid like 'nah I had that.' Simple rules, unhinged mind games, infinite rematches. Small board, big ego."** — *GPT's Edgy Brain-Rot Take*

---

## Features

### Current (Implemented)
- ✅ Terminal UI with styled ASCII art header
- ✅ Main menu with UP/DOWN navigation
- ✅ Player class with win condition checking (8 win patterns: 3 rows, 3 columns, 2 diagonals)
- ✅ 3×3 board display with grid formatting

### Planned
- 🔄 Complete game loop (move input, turn-switching, win detection)
- 🔄 Input validation (reject occupied cells, invalid coordinates)
- 🔄 Draw/tie detection (all 9 cells filled, no winner)
- 🔄 Load/save game functionality
- 🔄 Multiplayer support

---

## Architecture

The game is structured into four core modules:

| File | Purpose |
|------|---------|
| `Player.py` | Encapsulates player identity and win-checking logic |
| `game_area.py` | Renders the 3×3 board to terminal |
| `terminal_screens.py` | Menu UI and terminal styling (uses `blessed` library) |
| `__init__.py` | Entry point; initializes game state and menu |

**Data Flow:**
```
menu_main() → game_loop (TODO) → game_area(area) [display] → Player.check_win(area) [validate]
```

---

## Installation

### Requirements
- Python 3.7+
- `blessed` library for terminal styling

### Setup
```bash
# Install dependencies
pip install blessed

# Run the game
python __init__.py
```

---

## How to Play

**Status:** Currently only the menu is implemented. Game loop is pending.

When complete, gameplay will work as follows:
1. Start from main menu
2. Enter moves by selecting row/column (0-2)
3. Game alternates between Player 1 (X) and Player 2 (O)
4. First to align 3 symbols wins
5. Return to menu on game end

---

## Known Issues

- **[Player.py line 26]** Diagonal win check has a bug: `area[0][2] == area[1][1] == area[1][2]` should be `area[0][2] == area[1][1] == area[2][0]`
- Menu navigation is incomplete (exits only on 'q' key, incomplete option handling)
- Game loop logic entirely missing (no move input, validation, or turn management)

---

## Development Notes

### Board State Representation
The board is a 3×3 list of strings:
- `"#"` = empty cell
- `"X"` = Player 1's move
- `"O"` = Player 2's move

Example:
```python
area = [["#", "X", "#"],
        ["O", "X", "#"],
        ["#", "#", "#"]]
```

### Terminal UI
Uses `blessed.Terminal()` for styling and cursor control:
- `term.bold_cyan()` - Cyan bold text
- `term.bold_orange_reverse()` - Orange reverse (highlight)
- `term.move_up(n)` / `term.move_down(n)` - Cursor movement
- ASCII art is auto-generated; don't edit manually

---

## Next Steps

1. Fix the diagonal win check bug in `Player.py`
2. Implement core game loop in `__init__.py`
3. Add move input validation
4. Add draw/tie detection
5. Enhance menu for multiplayer and load/save options

---

## License

Learning project. Use freely.
