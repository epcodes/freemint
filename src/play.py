crash = False
import tkinter
#just in case
gameEnd = False
from chesspiecesetup import *

PAWN = 100
ROOK = 480
KNIGHT = 330
BISHOP = 350
QUEEN = 955
KING = 20000

ply = 0


    
    PiecesToCheck = [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8, knight1, knight2, bishop1, bishop2, rook1, rook2, queen1, king1]
    
    piececheck1 = random.choice(PiecesToCheck)
    
    if piececheck1 = PiecesToCheck[0]:
        plus = random.choice(pawn1moves)
        coord = pawn1 + plus
        checkcoord = coord - 1
        if pawnevalWhite[checkcoord] > pawnevalWhite[pawn1]:
            pawn1 = pawn1 + plus - 1
        
