from pygame import math
import parameters
from pheremoneSquareList import addBlueAlpha, addRedAlpha

class pheromoneMap:
    def __init__(self, GridSizeX, GridSizeY):
        self.GRIDSIZEX = GridSizeX
        self.GRIDSIZEY = GridSizeY
        self.GRID = []
        for i in range(self.GRIDSIZEX * self.GRIDSIZEY):
            self.GRID.append([None, None])


    def setPheromone(self, theAnt):
        index_y : int = int(theAnt.position[1] / (parameters.height / self.GRIDSIZEY))
        if(index_y < 0 or index_y >= self.GRIDSIZEY - 1):
            return
        index_x : int = int((theAnt.position[0] / (parameters.width / self.GRIDSIZEX)))
        if(index_x < 0 or index_x >= self.GRIDSIZEX - 1):
            return
        
        index : int = int((index_y * self.GRIDSIZEX) + index_x)
        if(theAnt.state==2):
            self.GRID[index][1] = theAnt.remembered_food
            addRedAlpha(index, len(self.GRID))
        if(theAnt.state==1):
            self.GRID[index][0] = theAnt.remembered_nest
            addBlueAlpha(index, len(self.GRID))

    def getClosestPheromone(self, is_searching_for_food, AntPos, return_obj) -> bool:
        #pheromonetype : int = 0
        if(is_searching_for_food): 
            pheromonetype = 1
        else:
            pheromonetype = 0


        index_y : int = int(AntPos[1] / (parameters.height / self.GRIDSIZEY))
        if(index_y < 0 or index_y >= self.GRIDSIZEY):
            return_obj = None
            return False
        index_x : int = int((AntPos[0] / (parameters.width / self.GRIDSIZEX)))
        if(index_x < 0 or index_x >= self.GRIDSIZEX):
            return_obj = None
            return False
        index : int = int((index_y * self.GRIDSIZEX) + index_x)
        return_obj = self.GRID[index][pheromonetype]
        if(return_obj == None):
            return False
        else:
            return True
    
    def Update():
        pass