import pygame
from bag import Bag
from board import Board
from piece import Piece
module_charge = pygame.init()
print('module_chargés (5,0) si success : ', module_charge)

ecran = pygame.display.set_mode((1000,1000))

loop = True

# Création des différents éléments du jeu
board = Board(10, 10)
bag = Bag()

# Tirage du premier type de pièce
draw = bag.Draw()
piece = Piece(draw["piece"])


# Démarrage du timer
clock = pygame.time.Clock()
timer = 0.01
getTicksLastFrame = 0

while loop :

    # Vérification des conditions de victoires, et fin du script si atteintes
    if board.board[0][5] == 1:
        print('Game finished ! Final Score : {}'.format(board.score))
        pygame.quit()

    # Affichage du scoreboard de base (titre de la fenêtre)
    pygame.display.set_caption("Tetris by ZilbaM - Score : {} - Next Piece : {}".format(board.score, draw["nextPiece"]))
    
    # Gestion du timer. Si le timer atteint 0.8s, on fait tomber la pièce et on reset le timer
    t = pygame.time.get_ticks()
    deltat = (t - getTicksLastFrame) / 1000
    getTicksLastFrame = t
    timer+=deltat
    if timer>.8:
        res = piece.Fall(board)
        board.updateBoard(res["board"])
        if res["newPiece"]:
            draw = bag.Draw()
            piece = Piece(draw["piece"])
        timer = 0
    
    ecran.fill((0,0,0))
    board.Draw(ecran)
    piece.Draw(ecran)
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
            if event.key == pygame.K_RIGHT:
                piece.Move('right', board)
            if event.key == pygame.K_LEFT:
                piece.Move('left', board)
            if event.key == pygame.K_UP:
                piece.Rotate(board.board)
            if event.key == pygame.K_DOWN:
                if piece.y <9:
                    piece.Fall(board)
            
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.flip()
    

pygame.quit()