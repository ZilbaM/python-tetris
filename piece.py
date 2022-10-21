from tkinter import E
import pygame
import random

class Piece:

    def __init__(self, type):
        self.type = type
        self.x = 5
        self.y = 0
        self.rotate = 0

    def Fall(self, board):
        canFall = True
        match self.type:
            case "O":
                affectedcells = [[self.y+2, self.x], [self.y+2, self.x+1]]
                currentcells = [[self.y, self.x], [self.y+1, self.x], [self.y, self.x+1], [self.y+1, self.x+1]]

                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
            case "I":
                match self.rotate:
                    case 0|2:
                        currentcells = [
                            [self.y, self.x-1],
                            [self.y, self.x],
                            [self.y, self.x+1],
                            [self.y, self.x+2],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                            [self.y+1, self.x+2],
                        ]
                    case 1|3:
                        currentcells = [
                            [self.y-1, self.x],
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y+2, self.x],
                        ]
                        affectedcells = [
                            [self.y+3, self.x],
                        ]
                
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False            
            case "T":
                match self.rotate:
                    case 0:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y-1, self.x],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 1:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+2, self.x],
                        ]
                    case 2:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y+1, self.x],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+2, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 3:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x+1],
                            [self.y+2, self.x],
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
            case 'Z':
                match self.rotate:
                    case 0|2:
                        currentcells = [
                            [self.y, self.x-1],
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+2, self.x],
                            [self.y+2, self.x+1]
                        ]
                    case 1|3:
                        currentcells = [
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y-1, self.x+1],
                            [self.y, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+2, self.x],
                            [self.y+1, self.x+1]
                        ]
                
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
            case 'S':
                match self.rotate:
                    case 0|2:
                        currentcells = [
                            [self.y, self.x+1],
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x+1],
                            [self.y+2, self.x],
                            [self.y+2, self.x-1]
                        ]
                    case 1|3:
                        currentcells = [
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y-1, self.x-1],
                            [self.y, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+2, self.x],
                            [self.y+1, self.x-1]
                        ]

                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
            case 'J':
                match self.rotate:
                    case 0:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y-1, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 1:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y-1, self.x+1],
                        ]
                        affectedcells = [
                            [self.y, self.x+1],
                            [self.y+2, self.x],
                        ]
                    case 2:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y+1, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+1, self.x],
                            [self.y+2, self.x+1],
                        ]
                    case 3:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+2, self.x-1],
                            [self.y+2, self.x],
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
            case 'L':
                match self.rotate:
                    case 0:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y-1, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+1, self.x-1],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 1:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y-1, self.x-1],
                        ]
                        affectedcells = [
                            [self.y, self.x-1],
                            [self.y+2, self.x],
                        ]
                    case 2:
                        currentcells = [
                            [self.y, self.x],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y+1, self.x-1],
                        ]
                        affectedcells = [
                            [self.y+2, self.x-1],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 3:
                        currentcells = [
                            [self.y, self.x],
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                        affectedcells = [
                            [self.y+2, self.x+1],
                            [self.y+2, self.x],
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if celly == board.height:
                        canFall = False
                    elif board.board[celly][cellx] == 1:
                        canFall = False
        newBoard = board.board
        
        if canFall:
            self.y+=1
            newPiece = False
        else:
            for cell in currentcells:
                newBoard[cell[0]][cell[1]] = 1
            newPiece = True
        return {
            "newPiece": newPiece,
            "board": newBoard
        }
    
    def Draw(self, screen):
        match self.type:
            case 'O':
                pygame.draw.rect(screen, (200,0,0), (self.x*100, self.y*100, 200, 200), 200)
            case 'I':
                match self.rotate:
                    case 0|2:
                        pygame.draw.rect(screen, (0, 200, 0), ((self.x-1)*100, self.y*100, 400, 100), 100)
                    case 1|3:
                        pygame.draw.rect(screen, (0, 200, 0), (self.x*100, (self.y-1)*100, 100, 400), 100)
            case 'T':
                match self.rotate:
                    case 0:
                        pygame.draw.rect(screen, (0,0,200), ((self.x-1)*100, self.y*100, 300, 100), 100)
                        pygame.draw.rect(screen, (0,0,200), (self.x*100, (self.y-1)*100, 100, 100), 100)
                    case 1:
                        pygame.draw.rect(screen, (0,0,200), (self.x*100, (self.y-1)*100, 100, 300), 100)
                        pygame.draw.rect(screen, (0,0,200), ((self.x-1)*100, self.y*100, 100, 100), 100)
                    case 2:
                        pygame.draw.rect(screen, (0,0,200), ((self.x-1)*100, (self.y)*100, 300, 100), 100)
                        pygame.draw.rect(screen, (0,0,200), (self.x*100, (self.y+1)*100, 100, 100), 100)
                    case 3:
                        pygame.draw.rect(screen, (0,0,200), (self.x*100, (self.y-1)*100, 100, 300), 100)
                        pygame.draw.rect(screen, (0,0,200), ((self.x+1)*100, self.y*100, 100, 100), 100)
            case 'Z':
                match self.rotate:
                    case 0|2:
                        pygame.draw.rect(screen, (200,200,0), ((self.x-1)*100, self.y*100, 200, 100), 100)
                        pygame.draw.rect(screen, (200,200,0), (self.x*100, (self.y+1)*100, 200, 100), 100)
                    case 1|3:
                        pygame.draw.rect(screen, (200,200,0), (self.x*100, self.y*100, 100, 200), 100)
                        pygame.draw.rect(screen, (200,200,0), ((self.x+1)*100, (self.y-1)*100, 100, 200), 100)
            case 'S':
                match self.rotate:
                    case 0|2:
                        pygame.draw.rect(screen, (200,200,0), (self.x*100, self.y*100, 200, 100), 100)
                        pygame.draw.rect(screen, (200,200,0), ((self.x-1)*100, (self.y+1)*100, 200, 100), 100)
                    case 1|3:
                        pygame.draw.rect(screen, (200,200,0), (self.x*100, self.y*100, 100, 200), 100)
                        pygame.draw.rect(screen, (200,200,0), ((self.x-1)*100, (self.y-1)*100, 100, 200), 100)
            case 'J':
                match self.rotate:
                    case 0:
                        pygame.draw.rect(screen, (200,0,200), ((self.x-1)*100, (self.y-1)*100, 100, 100), 100)
                        pygame.draw.rect(screen, (200,0,200), ((self.x-1)*100, (self.y)*100, 300, 100), 100)
                    case 1:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x+1)*100, (self.y-1)*100, 100, 100))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x)*100, (self.y-1)*100, 100, 300))
                    case 2:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x-1)*100, (self.y)*100, 300, 100))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x+1)*100, (self.y+1)*100, 100, 100))  
                    case 3:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x)*100, (self.y-1)*100, 100, 300))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x-1)*100, (self.y+1)*100, 100, 100))
            case 'L':
                match self.rotate:
                    case 0:
                        pygame.draw.rect(screen, (200,0,200), ((self.x+1)*100, (self.y-1)*100, 100, 100), 100)
                        pygame.draw.rect(screen, (200,0,200), ((self.x-1)*100, (self.y)*100, 300, 100), 100)
                    case 1:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x-1)*100, (self.y-1)*100, 100, 100))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x)*100, (self.y-1)*100, 100, 300))
                    case 2:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x-1)*100, (self.y)*100, 300, 100))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x-1)*100, (self.y+1)*100, 100, 100))  
                    case 3:
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x)*100, (self.y-1)*100, 100, 300))
                        pygame.draw.rect(screen, (200, 0, 200), ((self.x+1)*100, (self.y+1)*100, 100, 100))
    def Move(self, direction, board):
        match self.type:
            case 'O':
                affectedcells = {
                    "left": [
                        [self.y, self.x-1],
                        [self.y+1, self.x-1],
                    ],
                    "right": [
                        [self.y, self.x+2],
                        [self.y+1, self.x+2]
                    ]
                }
            case 'I':
                match self.rotate:
                    case 0|2:
                        affectedcells = {
                            "left": [
                                [self.y, self.x-2]
                            ],
                            "right": [
                                [self.y, self.x+3]
                            ]
                        }
                    case 1|3:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                                [self.y+1, self.x+1],
                            ]
                        }
            case 'T':
                match self.rotate:
                    case 0:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+2],
                            ]
                        }
                    case 1:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-2],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                            ]
                        }
                    case 2:
                        affectedcells = {
                            "left": [
                                [self.y+1, self.x-1],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y+1, self.x+1],
                                [self.y, self.x+2],
                            ]
                        }
                    case 3:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+2],
                                [self.y+1, self.x+1],
                            ],
                        }
            case 'Z':
                match self.rotate:
                    case 0|2:
                        affectedcells= {
                            "left": [
                                [self.y, self.x-2],
                                [self.y+1, self.x-1]
                            ],
                            "right": [
                                [self.y, self.x+1],
                                [self.y+1, self.x+2],
                            ]
                        }
                    case 1|3:
                        affectedcells = {
                            "left": [
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                                [self.y-1, self.x],
                            ],
                            "right": [
                                [self.y-1, self.x+2],
                                [self.y, self.x+2],
                                [self.y+1, self.x+1],
                            ]
                        }
            case 'S':
                match self.rotate:
                    case 0|2:
                        affectedcells= {
                            "left": [
                                [self.y, self.x-1],
                                [self.y+1, self.x-2]
                            ],
                            "right": [
                                [self.y, self.x+2],
                                [self.y+1, self.x+1],
                            ]
                        }
                    case 1|3:
                        affectedcells = {
                            "left": [
                                [self.y, self.x-2],
                                [self.y+1, self.x-1],
                                [self.y-1, self.x-2],
                            ],
                            "right": [
                                [self.y-1, self.x],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                            ]
                        }
            case 'J':
                match self.rotate:
                    case 0:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-2],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y-1, self.x],
                                [self.y, self.x+2],
                            ]
                        }
                    case 1:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+2],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                            ]
                        }
                    case 2:
                        affectedcells = {
                            "left": [
                                [self.y+1, self.x],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y+1, self.x+2],
                                [self.y, self.x+2],
                            ]
                        }
                    case 3:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-1],
                                [self.y+1, self.x-2],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                            ],
                        }
            case 'L':
                match self.rotate:
                    case 0:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y-1, self.x+2],
                                [self.y, self.x+2],
                            ]
                        }
                    case 1:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-2],
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+1],
                                [self.y+1, self.x+1],
                            ]
                        }
                    case 2:
                        affectedcells = {
                            "left": [
                                [self.y+1, self.x-2],
                                [self.y, self.x-2],
                            ],
                            "right": [
                                [self.y+1, self.x],
                                [self.y, self.x+2],
                            ]
                        }
                    case 3:
                        affectedcells = {
                            "left": [
                                [self.y-1, self.x-1],
                                [self.y, self.x-1],
                                [self.y+1, self.x-1],
                            ],
                            "right": [
                                [self.y-1, self.x+1],
                                [self.y, self.x+1],
                                [self.y+1, self.x+2],
                            ],
                        }
        match direction:
            case 'right':
                for cell in affectedcells['right']:
                    if cell[1]>9:
                        return
                    
                    if (cell[0] >= 0):
                        if (board.board[cell[0]][cell[1]] == 1):
                            return 

                self.x += 1   
            case 'left':
                for cell in affectedcells['left']:
                    if cell[1]<0:
                        return
                    if (cell[0] >= 0):
                        if (board.board[cell[0]][cell[1]] == 1):
                            return
                self.x -= 1

    def Rotate(self, board):
        match self.type:
            case 'O':
                return
            case 'I':
                match self.rotate:
                    case 0|2:
                        affectedcells = [
                            [self.y-1, self.x],
                            [self.y, self.x],
                            [self.y+1, self.x],
                            [self.y+2, self.x],
                        ]
                    case 1|3:
                        affectedcells = [
                            [self.y, self.x-1],
                            [self.y, self.x],
                            [self.y, self.x+1],
                            [self.y, self.x+2],
                        ]
                
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
            case 'T':
                match self.rotate:
                    case 0:
                        affectedcells = [
                            [self.y+1, self.x]
                        ]
                    case 1:
                        affectedcells = [
                            [self.y, self.x+1]
                        ]
                    case 2:
                        affectedcells = [
                            [self.y-1, self.x]
                        ]
                    case 3:
                        affectedcells = [
                            [self.y, self.x-1]
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
            case 'Z':
                match self.rotate:
                    case 0|2:
                        affectedcells = [
                            [self.y-1, self.x+1],
                            [self.y, self.x+1],
                        ]
                    case 1|3:
                        affectedcells = [
                            [self.y, self.x-1],
                            [self.y+1, self.x+1],
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
            case 'S':
                match self.rotate:
                    case 0|2:
                        affectedcells = [
                            [self.y-1, self.x-1],
                            [self.y, self.x-1],
                        ]
                    case 1|3:
                        affectedcells = [
                            [self.y, self.x+1],
                            [self.y+1, self.x-1],
                        ]
                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
            case 'J':
                match self.rotate:
                    case 0:
                        affectedcells = [
                            [self.y-1, self.x],
                            [self.y-1, self.x+1],
                            [self.y+1, self.x],
                        ]
                    case 1:
                        affectedcells = [
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y+1, self.x+1],
                        ]
                    case 2:
                        affectedcells = [
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x-1],
                        ]
                    case 3:
                        affectedcells = [
                            [self.y-1, self.x-1],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                        ]

                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
            case 'L':
                match self.rotate:
                    case 0:
                        affectedcells = [
                            [self.y-1, self.x],
                            [self.y-1, self.x-1],
                            [self.y+1, self.x],
                        ]
                    case 1:
                        affectedcells = [
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                            [self.y+1, self.x-1],
                        ]
                    case 2:
                        affectedcells = [
                            [self.y-1, self.x],
                            [self.y+1, self.x],
                            [self.y+1, self.x+1],
                        ]
                    case 3:
                        affectedcells = [
                            [self.y-1, self.x+1],
                            [self.y, self.x-1],
                            [self.y, self.x+1],
                        ]

                for cell in affectedcells:
                    [celly, cellx] = cell
                    if cellx<0 or cellx>9 or celly<-1 or celly>9:
                        return
                    if (board[celly][cellx] == 1):
                        return
        
        if self.rotate == 3 :
            self.rotate = 0
        else:
            self.rotate += 1
                
