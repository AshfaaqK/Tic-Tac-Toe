print("Welcome to Tic Tac Toe!\n\n")

# Explanation of grid system used to play the game
print('How to play: Enter the number where you want your X or O to go based on the grid below.\n')
print(f'''1 | 2 | 3\n---------
4 | 5 | 6\n---------
7 | 8 | 9\n\n''')

# 9 Positions of blank tiles to be turned into 'X' or 'O'
p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Turn system going from 0 to 9
turn = 0
should_end = False

# Win constant to check against
WIN_X = 'X X X'
WIN_O = 'O O O'


class DuplicateEntry(Exception):
    """Raised when entered position has been already played."""
    pass


# Core game mechanic takes the number from the user input
def game(number):
    # Terminal Stying as it is text based
    print('\n' * 20)

    # Checks which players turn it is (0 for Player 1, 1 for Player 2)
    if turn % 2 == 0:

        # Replaces blank tile in list with played turn
        p[number - 1] = 'X'

        # As the turns alternate the next turn after player 1 will be player 2
        print("Turn: Player 2 - O \n")

    else:
        p[number - 1] = 'O'
        print("Turn: Player 1 - X \n")

    # ASCII Grid with players turns updating the grid
    print(f'''{p[0]} | {p[1]} | {p[2]}\n---------
{p[3]} | {p[4]} | {p[5]}\n---------
{p[6]} | {p[7]} | {p[8]}\n\n''')


# Checks if a player has triggered a win condition or draw condition
def check_win():
    # All win possibilites turned into static strings
    row_1 = f'{p[0]} {p[1]} {p[2]}'
    row_2 = f'{p[3]} {p[4]} {p[5]}'
    row_3 = f'{p[6]} {p[7]} {p[8]}'

    column_1 = f'{p[0]} {p[3]} {p[6]}'
    column_2 = f'{p[1]} {p[4]} {p[7]}'
    column_3 = f'{p[2]} {p[5]} {p[8]}'

    diagonal_1 = f'{p[0]} {p[4]} {p[8]}'
    diagonal_2 = f'{p[2]} {p[4]} {p[6]}'

    # Uses win constant to check whether a win condition has been met
    if WIN_X in (row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2):

        # Player has won and game will be ended with the returned True
        print('Player 1 (X) Wins!')
        return True

    elif WIN_O in (row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2):
        print('Player 2 (O) Wins!')
        return True

    # If no win condition has been met by turn 9 then game will be declared a draw and will be ended
    elif turn == 9:
        print('Draw!')
        return True

    # If no win condition has been met, and it is not turn 9 then the game will continue
    else:
        return False


# Initial Player turn
print("Turn: Player 1 - X \n")

while not should_end:
    # If it is turn 9 then the game will end at the end of this turn
    if turn == 9:
        should_end = True

    # Game continues while not at turn 9
    else:

        # User entry check for invalid inputs
        try:
            place = int(input('Enter the number where you want to play (1-9): '))

            # If the user input is out of bounds
            if place < 1 or place > 9:
                raise IndexError

            # User input will be declared invalid if that spot has been played already
            elif p[place - 1] in ('X', 'O'):
                raise DuplicateEntry

        # Duplicate Entry Exception
        except DuplicateEntry:
            print('Spot has already been played, enter another number.\n')

        # Out of Bounds Exception
        except IndexError:
            print('Please enter a number within the range.\n\n')

        # Invalid Character Exception
        except ValueError:
            print('Please only enter a number within the range.\n\n')

        # When user input is valid
        else:
            # User input passed through to core game function
            game(place)

            # Increments turn after every turn played
            turn += 1

            # Checks for a win condition after every turn
            should_end = check_win()
