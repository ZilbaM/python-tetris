import pygame

class Board:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(self.width)] for x in range(self.height)]
        self.tileSize = height*100
        self.score = 0

    def Draw(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(screen, (115,115,115), (j*100, i*100, 100, 100), 5)
                if self.board[i][j]==1:
                    pygame.draw.rect(screen, (150,0,0), (j*100, i*100, 100, 100))
                
    
    def updateBoard(self, newBoard):
        rowsCompleted = 0
        for row in range(len(newBoard)):
            complete = True
            for cell in newBoard[row]:
                if cell==0:
                    complete = False
            if complete:
                newBoard.pop(row)
                newRow = [0 for x in range(self.width)]
                newBoard.insert(0, newRow)
                rowsCompleted += 1
        if (rowsCompleted>0):
            self.UpdateScore(rowsCompleted)
        self.board = newBoard

    def UpdateScore(self, rowsCompleted):
            score = [0, 40, 100, 300, 1200]

            self.score += score[rowsCompleted]