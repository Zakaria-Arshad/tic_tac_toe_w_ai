'''
Written by Zakaria Arshad
Tic Tac Toe game where a user can play against a computer.
The script randomly generates moves to play against the user.
When a win is detected, the script reports who won and ends.
'''

import random
class TicTacToe:
    '''The class TicTacToe contains all relevant methods for the tic-tac-toe script.'''

    '''The init method takes a string of symbols to fill the initial grid, and initializes a matrix attribute.'''
    def __init__(self, symbols):
        self.string_of_symbols = symbols
        first_row, second_row, third_row = [], [], []
        for count, coordinate in enumerate(symbols):
            if count <= 2:
                if coordinate == "_":
                    first_row.append(" ")
                else:
                    first_row.append(coordinate)
            elif 2 < count <= 5:
                if coordinate == "_":
                    second_row.append(" ")
                else:
                    second_row.append(coordinate)
            else:
                if coordinate == "_":
                    third_row.append(" ")
                else:
                    third_row.append(coordinate)
        self.matrix = [first_row, second_row, third_row]

    '''The set_coordinate method checks for valid coordinates and sets an attribute input_coordinates to them'''
    def set_coordinate(self):
        coordinate = input("Enter the coordinates: ")
        coordinate_list = coordinate.split()
        try:
            int_coordinate_list = [int(coordinate) for coordinate in coordinate_list]
        except ValueError:
            print("You should enter numbers!")
            return TicTacToe.set_coordinate(self)
        for coordinate in int_coordinate_list:
            if coordinate not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
                return TicTacToe.set_coordinate(self)
        if self.matrix[int_coordinate_list[0] - 1][int_coordinate_list[1] - 1] != " ":
            print("This cell is occupied! Choose another one!")
            return TicTacToe.set_coordinate(self)
        self.input_coordinates = int_coordinate_list

    '''The set_easy_computer_coordinate_and_matrix randomizes coordinates until it finds an empty spot, 
    and changes the matrix attribute accordingly'''
    def set_easy_computer_coordinate_and_matrix(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if self.matrix[x - 1][y - 1] != " ":
            return TicTacToe.set_easy_computer_coordinate_and_matrix(self)
        else:
            self.matrix[x - 1][y - 1] = "O"

    '''The get_coordinate method returns the input_coordinates attribute'''
    def get_coordinate(self):
        return self.input_coordinates

    '''The set_matrix method uses the get_coordinate method and sets the matrix spot to X or O accordingly'''
    def set_matrix(self):
        coordinates = TicTacToe.get_coordinate(self)
        x = coordinates[0] - 1
        y = coordinates[1] - 1
        number_of_xs = self.string_of_symbols.count('X')
        number_of_os = self.string_of_symbols.count('O')
        if number_of_xs == number_of_os:
            self.matrix[x][y] = "X"
        else:
            self.matrix[x][y] = "O"

    '''The check_for_win method checks all possibilities for a win, draw, or if the game should continue.'''
    def check_for_win(self):
        # check rows for win
        if ["X", "X", "X"] in self.matrix:
            print("X wins")
            return
        elif ["O", "O", "O"] in self.matrix:
            print("O wins")
            return
        # check columns for wins
        if self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0]:
            if self.matrix[0][0] == "X":
                print("X wins")
                return
            elif self.matrix[0][0] == "O":
                print("O wins")
                return
            else:
                pass
        if self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1]:
            if self.matrix[0][1] == "X":
                print("X wins")
                return
            elif self.matrix[0][1] == "O":
                print("O wins")
                return
            else:
                pass
        if self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2]:
            if self.matrix[0][2] == "X":
                print("X wins")
                return
            elif self.matrix[0][2] == "O":
                print("O wins")
                return
            else:
                pass
        # set spaces
        top_left, middle, bottom_right = self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]
        top_right, bottom_left = self.matrix[0][2], self.matrix[2][0]
        # check for diagonal wins
        if top_left == middle == bottom_right:
            if top_left == "X":
                print("X wins")
                return 1
            elif top_left == "O":
                print("O wins")
                return 1
            else:
                pass
        if top_right == middle == bottom_left:
            if top_right == "X":
                print("X wins")
                return 1
            elif top_right == "O":
                print("O wins")
                return 1
            else:
                pass
        if " " not in self.matrix[0] and " " not in self.matrix[1] and " " not in self.matrix[2]:
            print("Draw")
            return 1
        else:
            print('Making move level "easy"')
            return 0

    '''The string method prints out the tic-tac-toe grid'''
    def __str__(self):
        return f"---------\n" \
               f"| {self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]} |\n" \
               f"| {self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]} |\n" \
               f"| {self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]} |\n" \
               f"---------"

if __name__ == "__main__":
    '''Initializes empty grid'''
    start_symbols = "         "
    win_checker = 0
    grid = TicTacToe(start_symbols)
    print(grid)
    while True:
        '''Game alternates between player and computer, looping until a win_checker variable is changed.'''
        grid.set_coordinate()
        grid.set_matrix()
        print(grid)
        win_checker = grid.check_for_win()
        if win_checker == 1:
            break
        # now computer move
        grid.set_easy_computer_coordinate_and_matrix()
        print(grid)
        win_checker = grid.check_for_win()
        if win_checker == 1:
            break