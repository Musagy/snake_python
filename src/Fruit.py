from typing import Callable
import random

class Fruit:
  hs: int # height screen
  ws: int # width screen
  currentFruit: tuple[int, int]
  
  def __init__(self, hs, ws, verifyNoCollapse: Callable[[], bool]):
    self.hs = hs
    self.ws = ws
    self.createNewFruit(verifyNoCollapse)
    
  def createNewFruit(
    self,
    verifyNoCollapse: Callable[[tuple[int, int]], bool],
  ):
    while True:
      x = random.randint(1, self.ws)
      y = random.randint(1, self.hs)
      point = (x, y)
      isNotCollapsed = verifyNoCollapse(point)
      if not isNotCollapsed:
        self.currentFruit = point
        break
      