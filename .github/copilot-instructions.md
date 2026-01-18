# Tic-Tac-Toe Game - AI Agent Instructions

## Project Overview
A terminal-based Tic-Tac-Toe game built in Python with three core components: game board state management, player logic, and terminal UI. The game is still in early development (game loop logic incomplete, hardcoded demo only).

## Architecture & Data Flow

### Core Components
1. **[Player.py](Player.py)** - Encapsulates player identity (name, symbol) and win condition checking
   - `Player.check_win(area)` validates all 8 winning combinations (3 rows, 3 columns, 2 diagonals)
   - Note: Diagonal check has a bug at line 26: `area[0][2] == area[1][1] == area[1][2]` should be `area[0][2] == area[1][1] == area[2][0]`

2. **[game_area.py](game_area.py)** - Pure display function for the 3×3 board
   - Renders board state with grid formatting
   - Takes 3×3 list where `"#"` = empty, `"X"` or `"O"` = played move

3. **[terminal_screens.py](terminal_screens.py)** - Terminal UI with `blessed` library for styling
   - `title()` - ASCII art header (generated externally, don't edit manually)
   - `menu_options(option)` - Main menu with UP/DOWN navigation (returns cursor position)
   - `option_blink(position)` - Animated highlighting for selected menu option
   - `menu_main()` - Menu loop (exits on 'q' key, currently incomplete)

4. **[__init__.py](__init__.py)** - Entry point with hardcoded demo
   - Initializes empty board: 3×3 grid of `"#"` symbols
   - Creates two Player objects (X and O)
   - Currently just calls `menu_main()` (no game loop implemented)

### Data Flow
Board state is a simple 2D list: `area[row][col]` where row/col are 0-2. State flows:
```
menu_main() → [game logic needed] → game_area(area) [display] → Player.check_win(area) [validate]
```

## Key Patterns & Conventions

### Board State Representation
- Empty cells: `"#"` (not `None` or `" "`)
- Player symbols: `"X"` (Player 1) or `"O"` (Player 2)
- Always 3×3 list of strings for display simplicity

### Player Win Logic
Use `Player.check_win(area)` after moves. Returns boolean only—no move validation against occupied cells.

### Terminal UI
- Uses `blessed.Terminal()` for colors and movement (not raw ANSI codes)
- Styling: `term.bold_cyan()`, `term.bold_orange_reverse()` for highlights
- Navigation: `term.move_up(n)` / `term.move_down(n)` for cursor positioning

## Missing Implementation
The core game loop is absent. After menu selection, the game should:
1. Call `game_area(area)` to display board
2. Loop turn-by-turn: get move input → validate placement → update `area` → check win → swap players
3. Return to menu on game end

## External Dependencies
- `blessed` - Terminal styling and keyboard input
- Python stdlib only otherwise (no AI, no validation frameworks)

## Quick Wins for Enhancement
- Fix Player.check_win() diagonal bug (line 26)
- Implement input validation in game loop (reject occupied cells, invalid coordinates)
- Add draw/tie detection (all 9 cells filled, no winner)
- Store game state for "Load Game" menu option
