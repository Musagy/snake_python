from dataclasses import dataclass
import random
import Player

@dataclass
class Fruit:
  hs: int # height screen
  ws: int # width screen
  playerRef: Player
    
  @staticmethod
  def locationGenerator(height: int, width: int):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return (x, y)
  
  currentFruit: tuple(int, int) = locationGenerator(hs, ws)
  