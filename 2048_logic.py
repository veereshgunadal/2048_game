import random

class Game:
    def start_game(self):
        mat = []
        for i in range(4):
            mat.append([0]*4)
        
        for i in range(len(mat)):
            print(mat[i])
        
        a = ''' Movement key
             W or w - for up
             A or a - for left
             S or s - for down
             D or d - for right \n >>'''
    
        return mat
    
    def add_new_2(self, mat):
        row = random.randint(0,3)
        column = random.randint(0,3)
        print('row - ',row)
        print('column - ',column)
        
        while mat[row][column] != 0:
            row = random.randint(0,3)
            column = random.randint(0,3)
        mat[row][column] = 2
        return mat
    
    def get_current_state(self, mat):
        for i in range(len(mat)):
            print(mat[i])

    def movement(self, mat):
        new_mat = [] 
        for i in range(4):
            new_mat.append([0]*4)
            
        for i in range(4):
            temp = 0
            for j in range(4):
                flag = False
                if mat[i][j] != 0:
                    new_mat[i][temp] = mat[i][j]
                    flag = True
                if flag == True:
                    temp = temp + 1
                    
        return new_mat

    def merge(self, mat):
        for i in range(4):
            for j in range(3):
                if mat[i][j] == mat[i][j+1]:
                    mat[i][j] = mat[i][j] + mat[i][j+1]
                    mat[i][j+1] = 0
        return mat

    def reverse(self, mat):
        reverse_mat = []
        for i in mat:
            reverse_mat.append(i[::-1])
        return reverse_mat

    def left(self, mat):
        mat = self.movement(mat)
        mat = self.merge(mat)
        mat = self.movement(mat)
        self.get_current_state(mat)
        return mat

    def right(self, mat):
        mat = self.reverse(mat)
        mat = self.left(mat)
        mat = self.reverse(mat)
        self.get_current_state(mat)
        return mat

    def transpose(self, mat):
        trans_mat = []
        for i in range(4):
            trans_mat.append([0]*4)

        for i in range(4):
            for j in range(4):
                trans_mat[j][i] = mat[i][j]
        return trans_mat

    def up(self, mat):
        mat = self.transpose(mat)
        mat = self.left(mat)
        mat = self.transpose(mat)
        self.get_current_state(mat)
        return mat

    def down(self, mat):
        mat = self.transpose(mat)
        mat = self.right(mat)
        mat = self.transpose(mat)
        self.get_current_state(mat)
        return mat

    def is_game_over(self,mat):
        for i in range(4):
            for j in range(4):
                if mat[i][j] != 0:
                    return True

