import os
class UIPrinter:
  def printTopMargin():
    print("┌───────────────────────────┐")
    
  def printGameRow(
    segInRow: list[tuple[int, int]],
    fruit: tuple[int, int] = None
  ):
    defaultRow = "│                           │"
    listRowChars = list(defaultRow)
    
    if fruit is not None:
      listRowChars[fruit[0]] = "*"
    for segments in segInRow:
      x, _ = segments
      # listRowChars[x] = "■"
      listRowChars[x] = "█"
    newRow = "".join(listRowChars)
    
    print(newRow)
    
  def printBotMargin():
    print("└───────────────────────────┘")
    
  def printFrame(
    body: list[tuple[int, int]],
    height: int,
    fruit: tuple[int, int]
  ) :
    os.system('cls' if os.name == 'nt' else 'clear')
    
    UIPrinter.printTopMargin()
    
    for row in range(1, height + 1):
      rowData = list(filter(
        lambda segment: segment[1] == row, body
      ))
      if row == fruit[1]:
        UIPrinter.printGameRow(rowData, fruit)
      else:
        UIPrinter.printGameRow(rowData)
  
    UIPrinter.printBotMargin()