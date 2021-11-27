import pygame
from pygame.constants import MOUSEBUTTONUP, QUIT
from board import map_coord_to_pos
from board import get_piece_drawbox
from pygame.transform import scale
from pygame.image import load
from os.path import join
from os import getcwd

PATH = join(getcwd(), 'img\\pieces')

color = {
    "WHITE" : (220, 220, 230),
    "GREY" : (128, 128, 128),
    "YELLOW" : (204, 204, 0),
    "BLUE" : (50, 255, 255),
    "BLACK" : (0, 0, 0)

}

class Render:
    def __init__(self,board,width=480,framerate=60):
        self.board = board
        self.fps = int(framerate)
        self.width = int(width)
        self.box_width = self.width/8
        self.img_width = (self.box_width/5)*4
        self.boxes = self.getBoxes() # boxes = [ (x,y,width,width)]


        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width,self.width), vsync=1)
        self.load_img()
        pygame.display.set_caption('Chess')
        

        self.log()
    
    
    #umm it works but rectangles are better cause i gotta keep track of them    
    '''
    def draw_lines(self):
        for i in range(8):
            pygame.draw.lines(self.screen,0,False,[(0,self.box_width*i),(self.width,self.box_width*i)],1)
            pygame.draw.lines(self.screen,0,False,[(self.box_width*i,0),(self.box_width*i,self.width)],1)
    '''
    def load_img(self):
        dim = (self.img_width,self.img_width)
        self.w_pawn = scale(load(join(PATH,'w_pawn.png')),dim)
        self.b_pawn = scale(load(join(PATH,'b_pawn.png')),dim)
        self.w_knight = scale(load(join(PATH,'w_knight.png')),dim)
        self.b_knight = scale(load(join(PATH,'b_knight.png')),dim)
        self.w_rook = scale(load(join(PATH,'w_rook.png')),dim)
        self.b_rook = scale(load(join(PATH,'b_rook.png')),dim)
        self.w_queen = scale(load(join(PATH,'w_queen.png')),dim)
        self.b_queen = scale(load(join(PATH,'b_queen.png')),dim)
        self.w_bishop = scale(load(join(PATH,'w_bishop.png')),dim)
        self.b_bishop = scale(load(join(PATH,'b_bishop.png')),dim)
        self.w_king = scale(load(join(PATH,'w_king.png')),dim)
        self.b_king = scale(load(join(PATH,'b_king.png')),dim)

    def getBoxes(self):
        return [[pygame.Rect(self.box_width*i , self.box_width*j,self.box_width,self.box_width) for j in range(8)] for i in range(8)]
        
        '''
        for i in range(8):
            for j in range(8):
                boxes.append(pygame.Rect(self.box_width*i , self.box_width*j,self.box_width,self.box_width))
        return boxes
        # return [(x,y,width,height)]
        '''
    def drawBoxes(self):
        color = 0#(80,90,70)
        color_normal = [(200,220,210), (190,200,240)]
        
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,color_normal[(i+j)%2],self.boxes[i][j],0)
                pygame.draw.rect(self.screen,color,self.boxes[i][j],1)
        for (x,y) in self.board.inputs:
            pygame.draw.rect(self.screen,(200,190,180),self.boxes[x-1][y-1],0)
            pygame.draw.rect(self.screen,0,self.boxes[x-1][y-1],1)

    def drawPieces(self):
        for i in range(1,9):
            for j in range(1,9):
                if(self.board.board[i][j] != None):
                    self.drawSprite((i,j),self.board.board[i][j].get_type())

    def drawSprite(self,pos,type):
        draw_pos = get_piece_drawbox(self.box_width,pos)
        if type=='w_pawn':
            self.screen.blit(self.w_pawn,draw_pos)
        elif type == 'b_pawn':
            self.screen.blit(self.b_pawn,draw_pos)
        elif type=='w_knight':
            self.screen.blit(self.w_knight,draw_pos)
        elif type=='b_knight':
            self.screen.blit(self.b_knight,draw_pos)
        elif type=='w_rook':
            self.screen.blit(self.w_rook,draw_pos)
        elif type=='b_rook':
            self.screen.blit(self.b_rook,draw_pos)
        elif type=='w_bishop':
            self.screen.blit(self.w_bishop,draw_pos)
        elif type=='b_bishop':
            self.screen.blit(self.b_bishop,draw_pos)
        elif type=='w_queen':
            self.screen.blit(self.w_queen,draw_pos)
        elif type=='b_queen':
            self.screen.blit(self.b_queen,draw_pos)
        elif type=='w_king':
            self.screen.blit(self.w_king,draw_pos)
        elif type=='b_king':
            self.screen.blit(self.b_king,draw_pos)


    def update(self):
        self.screen.fill(color["WHITE"])
        self.drawBoard()
        #pygame.draw.lines(self.screen,0,False,[(0,60),(480,60)],1)
        #self.draw_lines()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 'quit'
            elif event.type == MOUSEBUTTONUP:
                self.board.input_handler(map_coord_to_pos(pygame.mouse.get_pos(),self.box_width))
                assert 1==1
            
        pygame.display.flip()
        self.clock.tick(self.fps)
        print('FPS:%s'%str(int(self.clock.get_fps())))

    def drawBoard(self):
        self.drawBoxes()
        self.drawPieces()

    def updateScreen(self):
        for x,y in self.board.inputs:
            pygame.display.update(self.boxes[x-1][y-1])
    

    def log(self):
        print(getcwd())