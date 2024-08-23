# Tic-Tac-Toe-Minimax-Tree-Pruning

Implements the Minimizer and Mamizer concepts from Game Theory

We have the function check_max_has_won and check_min_has_won which acts as base conditions for winning and assign reward to Game states

play_turn_of_mac_maximizer - The functions has the Maximizer. This function  inturn calls the minimizer to understand the possible states and picks the state which gives him the best  state

play_turn_of_opponent_minimizer -  The functions has the Minimizer.  This function  inturn calls the Maximizer to understand the possible states and picks the state which gives him the best  state.

start_game - This function is where the Maximizer plays against the minimizer


start_game_with_human -  This function is where the Maximizer plays against the Human Input.
