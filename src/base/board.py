from math import floor
from pieces import Pawn,Knight,Rook,King,Queen,Bishop
WHITE = 0
BLACK = 1


class Board:
    def __init__(self):
        self.t = []

        self.board = [[None for _ in range(9)] for _ in range(9)]
        self.pieces = []
        self.inputs = []
        
        
        
        for i in range(1,9):
            self.board[i][2] = Pawn(BLACK)
            self.board[i][7] = Pawn(WHITE)
        self.board[5][1] = King(BLACK)
        self.board[5][8] = King(WHITE)
        self.board[4][1] = Queen(BLACK)
        self.board[4][8] = Queen(WHITE)
        self.board[1][1] = Rook(BLACK)
        self.board[8][1] = Rook(BLACK)
        self.board[1][8] = Rook(WHITE)
        self.board[8][8] = Rook(WHITE)
        self.board[2][1] = Knight(BLACK)
        self.board[7][1] = Knight(BLACK)
        self.board[2][8] = Knight(WHITE)
        self.board[7][8] = Knight(WHITE)
        self.board[3][1] = Bishop(BLACK)
        self.board[6][1] = Bishop(BLACK)
        self.board[3][8] = Bishop(WHITE)
        self.board[6][8] = Bishop(WHITE)

    def get_pieces(self):
        return self.pieces

    def input_handler(self,pos):
        if self.inputs == []:
            self.inputs.append(pos)
        else:
            self.inputs.append(pos)
            self.move_piece()
            self.inputs.clear()

    def move_piece(self):
        x1,y1 = self.inputs[0]
        x2,y2 = self.inputs[1]
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = None

def get_piece_drawbox(box_dim,pos):
    x,y = pos
    offset = box_dim/10
    return (((x-1)*box_dim+offset,((y-1)*box_dim)+offset))

def map_coord_to_pos(coord,box_dim):
    x,y = coord
    return ((floor(x/box_dim)+1),(floor(y/box_dim+1)))




        