from random import random



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
        
    
    def makeRandomRect(self):
        upperconerx = int(random.uniform(0,self.mapw-self.obsDim))
        upperconery = int(random.uniform(0,self.mapw-self.obsDim))
        
        return(upperconerx, upperconery)
        
    def makeobs(self):
        obs =[]
        
        for i in range(0,self.obsNum)
            rectang = None
            startgoalcol = True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang=pygame.Rect(upper,(self.obsDim,self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol= True
                else:startgoalcol =False
            obs.append(rectang)
            self.obstacle= obs.copy()
            return obs
    
    def add_node(self):
        pass
    
    def remove_node(self):
        pass
    
    def add_edge(self):
            pass
        
    def remove_edge(self):
        pass
    
    def number_of_nodes (self):
        pass 
    def distance(self):
        pass
    
    def nearest(self):
        pass
    def isFree (self):
        pass
    def crossobstalce(self):
        pass
    
    def connect(self):
        pass
    
    def step(self):
        pass
    
    def path_to_goal(self):
        pass
    
    
    def getPathCoords(self):
        pass
    
    def expand(self):
        pass
    
    def cost(self):
        pass