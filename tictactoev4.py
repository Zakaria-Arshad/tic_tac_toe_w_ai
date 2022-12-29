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

    def __init__(self):
        self.list_of_symbols = []
        first_row, second_row, third_row = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
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
        TicTacToe.set_matrix(self, int_coordinate_list[0], int_coordinate_list[1])

    '''The set_easy_computer_coordinate_and_matrix randomizes coordinates until it finds an empty spot, 
    and changes the matrix attribute accordingly'''

    def set_easy_computer_coordinate(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if self.matrix[x - 1][y - 1] != " ":
            TicTacToe.set_easy_computer_coordinate(self)
        else:
            TicTacToe.set_matrix(self, x, y)
            print('Making move level "easy"')

    '''The get_list_of_symbols method returns a list of all symbols on the current grid in one list'''

    def get_list_of_symbols(self):
        list_of_symbols = []
        for row in self.matrix:
            for item in row:
                if item == " ":
                    list_of_symbols.append("-")
                else:
                    list_of_symbols.append(item)
        return list_of_symbols

    '''The set_matrix method uses the get_coordinate method and sets the matrix spot to X or O accordingly'''

    def set_matrix(self, x, y):
        current_symbols = TicTacToe.get_list_of_symbols(self)
        number_of_xs = current_symbols.count('X')
        number_of_os = current_symbols.count('O')

        if number_of_xs == number_of_os:
            self.matrix[x - 1][y - 1] = "X"
        else:
            self.matrix[x - 1][y - 1] = "O"

    '''The check_for_win method checks all possibilities for a win, draw, or if the game should continue.
       The script returns 1 in case of a win or draw, so the main script can stop the game.'''

    def check_for_win(self):
        # check rows for win
        if ["X", "X", "X"] in self.matrix:
            print("X wins")
            return 1
        elif ["O", "O", "O"] in self.matrix:
            print("O wins")
            return 1
        # check columns for wins
        if self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0]:
            if self.matrix[0][0] == "X":
                print("X wins")
                return 1
            elif self.matrix[0][0] == "O":
                print("O wins")
                return 1
            else:
                pass
        if self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1]:
            if self.matrix[0][1] == "X":
                print("X wins")
                return 1
            elif self.matrix[0][1] == "O":
                print("O wins")
                return 1
            else:
                pass
        if self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2]:
            if self.matrix[0][2] == "X":
                print("X wins")
                return 1
            elif self.matrix[0][2] == "O":
                print("O wins")
                return 1
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

        # check for draw or continue game
        if " " not in self.matrix[0] and " " not in self.matrix[1] and " " not in self.matrix[2]:
            print("Draw")
            return 1
        else:
            return 0

    '''The string method prints out the tic-tac-toe grid'''

    def __str__(self):
        return f"---------\n" \
               f"| {self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]} |\n" \
               f"| {self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]} |\n" \
               f"| {self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]} |\n" \
               f"---------"


class MediumDifficulty(TicTacToe):
    '''The MediumDifficulty class uses an algorithm that can win or block one move ahead, otherwise playing random moves'''

    '''The init is the same as class TicTacToe, but has attribute icon to set which player is "X" or "O"'''
    def __init__(self):
        super().__init__()
        self.icon = " "

    '''The method set_medium_coordinates_and_matrix sets random coordinates unless an immediate win or winning block exists, and sets the matrix accordingly'''
    def set_medium_coordinates_and_matrix(self):
        list_of_symbols = super().get_list_of_symbols()
        column1 = [self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]]
        column2 = [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]]
        column3 = [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]]
        diagonal1 = [self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]]
        diagonal2 = [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]]
        column_matrix = [column1, column2, column3]

        if list_of_symbols.count("X") == list_of_symbols.count("O"):
            self.icon = "X"
        else:
            self.icon = "O"

        for count, row in enumerate(self.matrix):
            if row.count("X") == 2 or row.count("O") == 2:
                try:
                    index = row.index(" ")
                    self.matrix[count][index] = self.icon
                    print('Making move level "medium"')
                    return
                except ValueError:
                    pass

        for count, column in enumerate(column_matrix):
            if column.count("X") == 2 or column.count("O") == 2:
                try:
                    index = column.index(" ")
                    self.matrix[index][count] = self.icon
                    print('Making move level "medium"')
                    return
                except ValueError:
                    pass

        if diagonal1.count("X") == 2 or diagonal1.count("O") == 2:
            try:
                index = diagonal1.index(" ")
                if index == 0:
                    self.matrix[0][0] = self.icon
                elif index == 1:
                    self.matrix[1][1] = self.icon
                elif index == 2:
                    self.matrix[2][2] = self.icon
                print('Making move level "medium"')
                return
            except ValueError:
                pass

        if diagonal2.count("X") == 2 or diagonal2.count("O") == 2:
            try:
                index = diagonal2.index(" ")
                if index == 0:
                    self.matrix[0][2] = self.icon
                if index == 1:
                    self.matrix[1][1] = self.icon
                if index == 2:
                    self.matrix[2][0] = self.icon
                print('Making move level "medium"')
                return
            except ValueError:
                pass

        # if there are no immediate wins or blocks
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if self.matrix[x - 1][y - 1] != " ":
            MediumDifficulty.set_medium_coordinates_and_matrix(self)
        else:
            self.matrix[x - 1][y - 1] = self.icon
            print('Making move level "medium"')


'''Allows user to pick which player is first and second, start or end a match, and returns the users'''
def game_initialization(game_string):
    user_list = game_string.split()
    if user_list[0] == "exit":
        exit()
    difficulty_tuple = ("user", "easy", "medium", "hard")
    while True:
        if len(user_list) < 3 or user_list[1] not in difficulty_tuple or user_list[2] not in difficulty_tuple:
            print("Bad parameters!")
            return False
        else:
            return user_list[1], user_list[2]


'''Main script'''
if __name__ == "__main__":
    '''Initializes empty grid'''
    while True:
        win_checker = 0
        while True:
            start = input("Input command: ")
            if not game_initialization(start):
                pass
            else:
                user1, user2 = game_initialization(start)
                break
        if user1 == "medium" or user2 == "medium":
            grid = MediumDifficulty()
        else:
            grid = TicTacToe()
        print(grid)

        while True:
            '''Script checks if the user goes first, second, or if both players are AI.
               It then runs the player/computer script first and/or second correspondingly.'''
            if user1 == "user" and user2 == "easy":
                grid.set_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
                # now computer move
                grid.set_easy_computer_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
            elif user1 == "easy" and user2 == "user":
                grid.set_easy_computer_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
                # now user move
                grid.set_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                print(win_checker)
                if win_checker == 1:
                    break
            elif user1 == "easy" and user2 == "easy":
                grid.set_easy_computer_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
            elif user1 == "user" and user2 == "medium":
                grid.set_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
                # now computer move
                grid.set_medium_coordinates_and_matrix()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
            elif user1 == "medium" and user2 == "user":
                grid.set_medium_coordinates_and_matrix()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
                print(grid)
                grid.set_coordinate()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break
            elif user1 == "medium" and user2 == "medium":
                grid.set_medium_coordinates_and_matrix()
                print(grid)
                win_checker = grid.check_for_win()
                if win_checker == 1:
                    break

