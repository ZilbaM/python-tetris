import random

class Bag:
    def __init__(self):
        self.index = 0
        self.sequence = ["I", "O", "T", "Z", "S", "J", "L"]
        self.nextSequence = ["I", "O", "T", "Z", "S", "J", "L"]
        random.shuffle(self.sequence)
        random.shuffle(self.nextSequence)

    def Draw(self):
        piece = ""
        nextPiece = ""
        match self.index:
            case 6:
                piece = self.sequence[self.index]
                nextPiece = self.nextSequence[0]
                self.Shuffle()
                self.index = 0
            case other:
                piece = self.sequence[self.index]
                nextPiece = self.sequence[self.index+1]
                self.index+=1

        return {
            'piece': piece,
            'nextPiece': nextPiece
        }


    def Shuffle(self):
        self.sequence = self.nextSequence
        random.shuffle(self.nextSequence)