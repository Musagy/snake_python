import time
from src.UIPrinter import UIPrinter
from src.Controller import Controller
from src.Player import Player 
import keyboard as kb

class Main:
  height: int = 10
  
  def start():
    player = Player(Main.height)
    
    UIPrinter.printFrame(player.body, Main.height)
    
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
      
      player.step()
      UIPrinter.printFrame(player.body, Main.height)
      
      time.sleep(.5) 
      
      if kb.is_pressed("esc"):
        break 
    print("Fin  del juego" )
 
Main.start()  