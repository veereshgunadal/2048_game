import random

class Game:
    def start_game(self):
        self.mat = []
        for i in range(4):
            self.mat.append([0]*4)
        
        for i in range(len(self.mat)):
            print(self.mat[i])
        
        a = ''' Movement key
             W or w - for up
             A or a - for left
             S or s - for down
             D or d - for right \n >>'''
    
        return self.mat
    
    def add_new_2(self):
        row = random.randint(0,3)
        column = random.randint(0,3)
        print('row - ',row)
        print('column - ',column)
        
        while self.mat[row][column] != 0:
            row = random.randint(0,3)
            column = random.randint(0,3)
        self.mat[row][column] = 2
        
    
    def get_current_state(self):
        for i in range(len(self.mat)):
            print(self.mat[i])

    def movement(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat)-1, 0, -1):
                if self.mat[i][j-1] == 0:
                    self.mat[i][j-1] = self.mat[i][j]
                    self.mat[i][j] = 0
        return self.mat

    def merge(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat)-1, 0, -1):
                if self.mat[i][j] == self.mat[i][j-1]:
                    self.mat[i][j-1] = self.mat[i][j-1] + self.mat[i][j]
                    self.mat[i][j] = 0
        return self.mat

    def left(self):
        self.movement()
        self.merge()
        self.add_new_2()

    def right(self):
        self.reverse()
        self.left()
        self.reverse()
        
game = Game()
game.start_game()

game.add_new_2()
game.add_new_2()
game.get_current_state()
print()