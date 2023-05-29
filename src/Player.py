from .Fruit import Fruit 

class Player:
  hs: int
  initHeight: int
  body: list[tuple[int, int]]
  direction: str
  redirectionCD: bool
  life: bool
  
  def __init__(self, heightScreen = int):
    self.hs = heightScreen
    self.initHeight = int(self.hs/2)
    self.body= [
      (10, self.initHeight),
      (11, self.initHeight),
      (12, self.initHeight),
      (13, self.initHeight),
      (14, self.initHeight)
    ]
    self.direction: str = "right"
    self.redirectionCD: bool = False
    self.life: bool = True
    
  def setDirection(self, newDirection: str):
      if not self.redirectionCD:
        self.direction = newDirection
        self.redirectionCD = True
        
  def getDirection(self):
      return self.direction
    
  def step(self, fruit: Fruit):
    newPosition = list(self.body[-1])
    self.redirectionCD = False
    
    match self.direction:
      case "right":
        newPosition[0] += 1
      case "left":
        newPosition[0] -= 1 
      case "up":
        newPosition[1] -= 1
      case "down":
        newPosition[1] += 1 
        
    if (
      newPosition[0] in [0, 28]
      or newPosition[1] in [0, self.hs + 1]
      or self.verifyNoCollapse(newPosition, True)
    ) :
      self.life = False
      return
      
    if (
      fruit.currentFruit[0] != newPosition[0]
      or fruit.currentFruit[1] != newPosition[1]
    ) :
      self.body.pop(0)
      self.body.append(tuple(newPosition))
    else:
      self.body.append(tuple(newPosition))
      fruit.createNewFruit(self.verifyNoCollapse)
      
      
  def verifyNoCollapse(self, point: tuple[int, int], noTail: bool = False) -> bool:
    bodyCopy = self.body.copy()
    
    if noTail: bodyCopy.pop(0)
    bodyCopy.append(point)
    
    bodyTuple = tuple(tuple(segment) for segment in bodyCopy)
    bodySet = set(bodyTuple)
    
    return len(bodyCopy) != len(bodySet)
    