class Controller:
  @staticmethod
  def updateDirection(setDirection, getDirection):
    def kbListener(event):
      currentDir = getDirection()
      noVertical = currentDir in ["right", "left"]
      noHorizontal = currentDir in ["down", "up"]
      
      match event.scan_code:
        case 72: 
          if noVertical: setDirection("up")
        case 80: 
          if noVertical: setDirection("down")
        case 77: 
          if noHorizontal: setDirection("right")
        case 75: 
          if noHorizontal: setDirection("left")
      
    return kbListener