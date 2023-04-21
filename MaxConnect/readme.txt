Python is used to code for Part 2 and since it is in v3, it is not compatible with omega.

Following are the files used to execute Part 2:

1.input.txt - it contains input to initialize gameboard.

2.output.txt - it is used to save the output from gameboard after making a move in One-Move mode.

3.MaxConnect4Game.py - contains the class for whole game with instructions to play and score for AI. This file contains code for min-max, alpha-beta pruning and eval function.

4.MaxConnect4.py - contains the program for the game for different modes.

To run the program:

Interactive Mode:
    python maxconnect4.py interactive input.txt computer-next 7

One-Move Mode:
    python maxconnect4.py one-move input.txt output.txt 10
