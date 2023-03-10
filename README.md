# tic_tac_toe_w_ai, written by Zakaria Arshad
A tic-tac-toe Python script using an AI algorithm and Object-Oriented Programming 
Implements Python Classes, Methods, and three difficulty levels.
The hardest difficulty uses an algorithm to guarentee a win or draw for the computer each time.

Command parameters: start, quit, user, easy, medium, hard

Example: Input start user easy to have player as X, easy difficulty as O. Input start hard user to have hard difficulty as X, user as O. Input start medium medium to have medium difficulty play each other. Input quit to quit.

Type in coordinates on a 3x3 grid. 1 1 will put a symbol in the top right, 2 3 will put a symbol in the second row, third column

Changelog: 

12/27 - Uploaded v2 

12/27 - Uploaded v3. Added functionality for user to choose as player 1 or 2, or have computer play itself through game_initialization function. Fixed set_matrix and set_easy_computer_coordinate_and_matrix methods to actually determine whether turn is "X" player or "O" player. Added loop to allow user to play multiple games.

12/28 - Uploaded v4. Added medium difficulty, capable of looking one move ahead. Simplified and removed unncessary code in Class TicTacToe initialization method. Simplified methods in TicTacToe class to reduce code and make it easier to follow.

12/30 - Uploaded v5, final version. Added hard difficulty, capable of looking multiple moves ahead. Hard difficulty implements a "minimax" algorithm to guarantee a win or draw for the computer every game. 
