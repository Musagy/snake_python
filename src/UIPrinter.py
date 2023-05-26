import os

class UIPrinter:
  def printTopMargin():
    print("┌───────────────────────────┐")
    
  def printGameRow(segInRow):
    defaultRow = "│                           │"
    listRowChars = list(defaultRow)
    
    for segments in segInRow:
      x, _ = segments
      # listRowChars[x] = "■"
      listRowChars[x] = "█"
    newRow = "".join(listRowChars)
    
    print(newRow)
    
  def printBotMargin():
    print("└───────────────────────────┘")
    
  def printFrame(body, height):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    UIPrinter.printTopMargin()
    
    for row in range(height):
      rowData = list(filter(
        lambda segment: segment[1] == row + 1, body
      ))
      UIPrinter.printGameRow(rowData)
  
    UIPrinter.printBotMargin()