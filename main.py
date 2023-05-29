import time
from src.UIPrinter import UIPrinter
from src.Controller import Controller
from src.Player import Player 
from src.Fruit import Fruit
import keyboard as kb

class Main:
  height: int = 10
  
  def start(self):
    player = Player(self.height)
    point = 0
    fruit = Fruit(
      hs = self.height,
      ws = 27,
      verifyNoCollapse = player.verifyNoCollapse
    )
    
    UIPrinter.printFrame(player.body, self.height, fruit.currentFruit)
    
    print("Presiona ESPACIO para EMPEZAR!")
    kb.wait("space")
    
    controller = Controller()
    directionListener = controller.updateDirection(
      player.setDirection,
      player.getDirection
    )
    
    kb.on_press(directionListener)
    
    while True:
      if not player.life: 
        break
      
      player.step(fruit)
      UIPrinter.printFrame(player.body, self.height, fruit.currentFruit)
      # print(f"head: {player.body[-1]}, fruit: {fruit.currentFruit}")
      print(f"Score: {len(player.body) - 5}")
      
      time.sleep(.3) 
      
      if kb.is_pressed("esc"):
        break 
    print("Fin  del juego" )
 
Main().start()