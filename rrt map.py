import math
import pygame
import random


class RRTMAP:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        self.start = start
        self.goal = goal
        self.MapDimensions = MapDimensions
        self.Maph,self.Mapw= self.MapDimensions
        
        
        #windows settings
        self.MapwindowName ="My Amazon Path Finder"
        pygame.display.set_caption(self.MapwindowName)
        self.map= pygame.display.set_mode((self.Mapw,self.Maph))
        self.map.fill((0,0,255))
        self.nodeRad= 0
        self.nodeThickness=0
        self.edgeThickness = 1
        
        self.obstacle=[]
        self.obsdim=obsdim
        self.obsNumber = obsnum
        
        #colors
        
        self.grey =(70, 70,70)
        self.Blue=(0,0,255)
        self.Green = (0, 255,0)
        self.Red =(255,0,0)
        self.white =(255,255,255)
        
        
        
        def drawMap(self):
            pass
            
        def drawPath(self):
            pass 
        def drawObs(self):
            
        
        
class RRTGraph:
      def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
            (x,y) =start
        self.start =start
        self.goal =goal
        self.goalFlag = False
        self.maph,self.mapw=MapDimensions
        self.x = []
        self.y = []
        # initialize the tree        
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
        #the obstacles
        obstacles = []
        self.obsDim =obsdim
        self.obsNum = obsnum
        
        #path 
        self.goalstate = None
        self.path =[]
        