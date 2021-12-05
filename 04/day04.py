
import numpy as np

class bingoBoard:

    def __init__(self, x):
        self.board = x
        self.marked = np.array([False for x in range(0, 25)])
        self.marked.shape = (5, 5) 
        self.last_mark = None
        self.isBingo = False

    def __repr__(self) -> str:
        return str(self.board)

    def __str__(self) -> str:
        return str(self.board) + "\n"        

    def mark(self, num):    
        idx = self.board[:,:] == num
        if idx.any():
            self.last_mark = num
            self.marked = self.marked + idx
            self.isBingo = self.marked.all(axis = 0).any() or self.marked.all(axis = 1).any()

    def score(self):
        tmp = self.board
        tmp[self.marked] = 0
        return tmp.sum() * self.last_mark

def load_input(file_name):

    f = open(file_name, "r")

    bingo_calls = list(map(int, f.readline().split(",")))
    bingo_boards = []
    line = f.readline()
    raw_board = []
    while line:
        new_info = line.split()
        #print("line: {}".format(new_info))
        if len(new_info) == 0:
            if len(raw_board) != 0:
        #        print("add a board")
                bingo_boards.append(bingoBoard(np.array(raw_board)))
        #        print(bingo_boards[-1])            
            raw_board = []
        else:
            raw_board.append(list(map(int, new_info)))
        
        #print("Raw board: {}\n".format(raw_board))
        line = f.readline()
    
    f.close()

    return {"calls": bingo_calls, "boards": bingo_boards}

def play_game(game):
    for idx in range(0, len(game["calls"])):
        num = game["calls"][idx]
        print("num: {}".format(num))
        for bdx in range(0, len(game["boards"])):
            game["boards"][bdx].mark(num)
            if game["boards"][bdx].isBingo:
                print("Game Board {} is a BINGO!\nYour score is: {}".format(bdx, game["boards"][bdx].score()))
                return

def play_game_to_lose(game):

    remaining_boards = [True for x in range(0, len(game["boards"]))]
    for idx in range(0, len(game["calls"])):
        num = game["calls"][idx]
        print("num: {}".format(num))
        for bdx in range(0, len(game["boards"])):
            if game["boards"][bdx].isBingo:
                continue

            game["boards"][bdx].mark(num)
            if game["boards"][bdx].isBingo:
                remaining_boards[bdx] = False
                print("Game Board {} is a BINGO!\nYour score is: {}".format(bdx, game["boards"][bdx].score()))
        print("remaing boards: {}".format(remaining_boards))
        if not any(remaining_boards):
            return        

if __name__ == "__main__":

    board_raw = np.random.choice(100, 25, replace = False)
    board_raw.shape = (5, 5)

    board = bingoBoard(board_raw)
    print(board)

    board.mark(board_raw[0,0])
    board.mark(board_raw[0,1])
    print(board)

    board.mark(board_raw[0, 2])
    board.mark(board_raw[0, 3])
    
    if not board.isBingo:
        print(board)
        print("Not a bingo yet")
    else:
        print("oops. This board is not yet a bingo but the method said it was")
        print(board)
    
    last_mark = board_raw[0, 4]
    board.mark(last_mark)

    if board.isBingo:
        print("Great job!. The score is: {}".format(board.score()))
        right_ans = board_raw[1:, :].sum() * last_mark 
        print("But did you get the right answer: {}".format(right_ans))
    else:
        print("Oops! That should have been a bingo =(")

    game = load_input("example_input")

    print(game)

    print("Let's play a game!")
    play_game(game)

    game2 = load_input("example_input")
    print("Let's play to lose")
    play_game_to_lose(game2)