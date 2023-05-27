from dataclasses import dataclass

@dataclass
class Player:
  height: int
  initHeight: int
  direction: str
  redirectionCD: bool
  life: bool
  body: list[tuple[int, int]]
    
  def __init__(self, height: int):
    self.height = height
    self.initHeight = int(height/2)
    self.direction = "right"
    self.redirectionCD = False
    self.life = True
    self.body = [
      (11, self.initHeight),
      (12, self.initHeight),
      (13, self.initHeight),
      (14, self.initHeight)
    ]
    
  def setDirection(self, newDirection: str):
      if not self.redirectionCD:
        self.direction = newDirection
        self.redirectionCD = True
        
  def getDirection(self):
      return self.direction
    
  def step(self):
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
        
    if newPosition[0] in [0, 28] or newPosition[1] in [0, self.height + 1] :
      self.life = False
    else:
      self.body.pop(0)
      self.body.append(tuple(newPosition))
      
  # def verifyNoCollapse():
    