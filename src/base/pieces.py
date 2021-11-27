class Piece:

    def __init__(self,color):
        self.color = color # 0 for white 1 for black

    def get_pos(self):
        return self.pos

class Pawn(Piece):

    def get_type(self):
        if self.color==0:
            return 'w_pawn'
        else:
            return 'b_pawn'

class Knight(Piece):

    
    def get_type(self):
        if self.color==0:
            return 'w_knight'
        else:
            return 'b_knight'

class Rook(Piece):

    
    def get_type(self):
        if self.color==0:
            return 'w_rook'
        else:
            return 'b_rook'

class Bishop(Piece):

    
    def get_type(self):
        if self.color==0:
            return 'w_bishop'
        else:
            return 'b_bishop'

class Queen(Piece):

    
    def get_type(self):
        if self.color==0:
            return 'w_queen'
        else:
            return 'b_queen'

class King(Piece):

    
    def get_type(self):
        if self.color==0:
            return 'w_king'
        else:
            return 'b_king'


