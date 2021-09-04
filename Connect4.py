class Connect_Four():
    """
    Connect4Board initializes a 7x6 board with which to play a game of connect 4

    Methods:
        print_board:
            Print the board in stdout
        drop(n, team):
            Drop a piece into the nth column of the board for red or blue team
        check(team): (static)?
            checks the board to determine if the team has won
    """

    COL_COUNT = 7
    ROW_COUNT = 6

    def __init__(self):
        self.board = [[' ' for i in range(Connect_Four.COL_COUNT)] for j in range(Connect_Four.ROW_COUNT)]


    def print_board(self):
        '''
        Prints the current connect4 board, complete with placed pieces
        '''
        result = ''
        for i in self.board:
            result += '-' * 15 + '\n'
            for j in i:
                result += f'|{j}'
            result += '|\n'
        result += '-' * 15
        print(result)



    def drop(self, col: int, team: str):
        '''
        Drops a piece into the connect4 board at the selected column and fills the position with the team string

        col -> must be an integer between 1 - 7
        team -> must be a string
        '''
        col -= 1
        if col < 7 and col > -1:
            if self.board[0][col] == ' ':
                for i in range(5, -1, -1):
                    if self.board[i][col] == ' ':
                        self.board[i][col] = team
                        break
            else:
                print('That column is full dill weed.  Look much?  You\'ve lost your turn')
        else:
            print('1... to... 7... dumbass...  You lose your turn')

    def check(self, team: str):
        '''
        check the cross section for each point, this is definitely the most inefficient way to do this though
        each check 'section' only checks a portion of the board where the starting point of that winning line is possible
        ex/ a horizontal winning connect 4 cannot begin in column 5, because there are only 2 more columns for pieces to be placed
        The horizontal check starts on the left side and checks right, vertial starts at the top and checks down, diagonal checks down and left/right
        depending on which code block is running

        team -> checks the board to see if the 'team' token has completed a connect 4
        '''
        # check horizontal wins
        for i in range(Connect_Four.COL_COUNT - 3):
            for j in range(Connect_Four.ROW_COUNT):
                if self.board[j][i] == team and self.board[j][i + 1] == team and self.board[j][i + 2] == team and \
                        self.board[j][i + 3] == team:
                    return True

        # check for vertical wins
        for c in range(Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT - 3):
                if self.board[r][c] == team and self.board[r + 1][c] == team and self.board[r + 2][c] == team and \
                        self.board[r + 3][c] == team:
                    return True

        # check for diagonal right wins (works)
        for c in range(Connect_Four.COL_COUNT-3):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c+1] == team and self.board[r+2][c+2] == team and self.board[r+3][c+3] == team:
                    return True

        # check for diagonal left wins (works)
        for c in range(Connect_Four.COL_COUNT-4, Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c-1] == team and self.board[r+2][c-2] == team and self.board[r+3][c-3] == team:
                    return True


if __name__ == '__main__':
    board = Connect_Four()
    board.print_board()
    team1 = input('Enter a single character to use as your token player 1: ')
    team2 = input('Enter a single character to use as your token player 2: ')

    while not board.check(team1) and not board.check(team2):
        col = int(input('Player 1 insert piece in col (1-7): '))
        board.drop(col, team1)
        board.print_board()

        if board.check(team1):
            print('PLAYER 1 WINS!')
            quit()

        col = int(input('Player 2 insert piece in col (1-7): '))
        board.drop(col, team2)
        board.print_board()

        if board.check(team2):
            print('PLAYER 2 WINS!')
            quit()
