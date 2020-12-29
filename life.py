import numpy as np
import math
import time
import os
#np.random.seed(0)

def randn_skewed(N, alpha=0.0, loc=0.0, scale=1.0):
    sigma = alpha / np.sqrt(1.0 + alpha**2) 
    u0 = np.random.randn(N)
    v = np.random.randn(N)
    u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
    u1[u0 < 0] *= -1
    u1 = u1 + loc
    return u1

class GameofLife(object):
    def __init__(self,n):
        self.grid=self.setupGrid(n)

    def setupGrid(self,n):
        temp_board = np.zeros((n,n))
        rand_lst= np.random.randint(2, size=(n*n,)) #randn_skewed(n*n,0,1,0.2)
        for i in range(1,len(temp_board)-1):
            for j in range(1,len(temp_board[0])-1):
                temp_board[i][j]= rand_lst[(i*n)+j] #abs(math.floor(rand_lst[(i*n)+j])) 
        
        return temp_board

    def printGrid(self):
        print(self.grid)

    def returnGrid(self):
        return self.grid

    def getNeighbours(self,i,j):
        return [self.grid[i-1][j-1],self.grid[i-1][j],self.grid[i-1][j+1],self.grid[i][j+1],self.grid[i+1][j+1],self.grid[i+1][j],self.grid[i+1][j-1],self.grid[i][j-1] ]
    
    def ruleEngine(self,i,j):
        neighbours = self.getNeighbours(i,j)
        neighboursum=sum(neighbours)
        if(self.grid[i][j]==1):
            if(neighboursum < 2 or neighboursum > 3 ):
                return 0
            else:
                return 1
        else:
            if(neighboursum==3):
                return 1
            else:
                return 0       

    
    def update(self):
        for i in range(1,len(self.grid)-1):
            for j in range(1,len(self.grid[0])-1):
                self.grid[i][j]=self.ruleEngine(i,j)
    

    def play(self,epochs=100):
        for _ in range(epochs):
            self.update()
            self.printGrid()
            time.sleep(2)
            os.system('cls')
            time.sleep(0.2)
        
        print("finished!")

if __name__ == "__main__":
    game = GameofLife(10)
    #game.printGrid()
    game.play(100)