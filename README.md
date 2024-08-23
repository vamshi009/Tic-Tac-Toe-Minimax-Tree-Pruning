# Tic-Tac-Toe-Minimax-Algo-with-Alpha-beta-Tree-Pruning

# Game Theory Concepts: Minimizer and Maximizer

## Function Definitions

### 1. `check_max_has_won()`
- **Purpose**: Determines if the Maximizer has won the game.
- **Returns**: Boolean indicating if the Maximizer has won.

### 2. `check_min_has_won()`
- **Purpose**: Determines if the Minimizer has won the game.
- **Returns**: Boolean indicating if the Minimizer has won.

### 3. `play_turn_of_mac_maximizer()`
- **Purpose**: Executes the turn for the Maximizer.
- **Description**: This function explores possible states by invoking the Minimizer's function and selects the state that provides the best outcome for the Maximizer.
- **Flow**:
  1. Evaluate possible states.
  2. Call `play_turn_of_opponent_minimizer` to understand the outcomes of these states.
  3. Choose the state that maximizes the Maximizer's reward.

### 4. `play_turn_of_opponent_minimizer()`
- **Purpose**: Executes the turn for the Minimizer.
- **Description**: This function explores possible states by invoking the Maximizer's function and selects the state that minimizes the reward for the Maximizer (thus maximizing the Minimizer's advantage).
- **Flow**:
  1. Evaluate possible states.
  2. Call `play_turn_of_mac_maximizer` to understand the outcomes of these states.
  3. Choose the state that minimizes the Maximizer's reward.

### 5. `start_game()`
- **Purpose**: Starts a game between the Maximizer and the Minimizer.
- **Description**: Initializes the game and alternates turns between the Maximizer and Minimizer until a terminal condition is met (win/loss/draw).

### 6. `start_game_with_human()`
- **Purpose**: Starts a game between the Maximizer and a human player.
- **Description**: Allows a human player to compete against the Maximizer. The human inputs their moves, and the Maximizer plays its turn optimally.

## Summary
In this game setup, the **Maximizer** aims to achieve the highest reward possible, while the **Minimizer** aims to minimize the Maximizer's reward. The game alternates turns between these two agents, with the Maximizer always seeking to maximize the outcome and the Minimizer seeking to minimize it. The game can either be played against a computer-controlled Minimizer or a human player.

### Game Flow
1. **Maximizer's Turn**:
   - Call `play_turn_of_mac_maximizer()`.
2. **Minimizer's Turn**:
   - Call `play_turn_of_opponent_minimizer()`.
3. **End Game**:
   - Check game status using `check_max_has_won()` and `check_min_has_won()`.

Enjoy strategizing and playing the game!

