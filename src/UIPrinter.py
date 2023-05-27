import os
import random

class UIPrinter:
  def printTopMargin():
    print("┌───────────────────────────┐")
    
  def printGameRow(segInRow: list[tuple[int, int]]):
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
    
  def printFrame(body: list[tuple[int, int]], height: int):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    UIPrinter.printTopMargin()
    
    for row in range(height):
      rowData = list(filter(
        lambda segment: segment[1] == row + 1, body
      ))
      
      UIPrinter.printGameRow(rowData)
  
    UIPrinter.printBotMargin()
    
  def generateFruit(body: list[tuple[int, int]]):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        fruit = (x, y)

        if fruit not in body:
            return fruit