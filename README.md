# Zoyos Lantons Ant Simulator
 A simple Landon ant simulator written in Python with customizable parameters.
---
The following parameters are described:

- **board_size:** the size of the board (default is (100, 100))
- **ant_position:** the initial position of the ant (default is (50, 50))
- **ant_direction:** the initial direction of the ant (default is "up")
- **move_rules:** the ant's move rules (default is "rl", which means turn right on white squares, turn left on black squares)
- **initial_state:** the initial state of the board, supported "white", "black" and "checkerboard"
- **iterations:** number of iterations (default is 1000)
- **show_animation:** if or not to output the animation via matplotlib.pyplot (default is True)
