import math

#Contents of the input file
file = open("input.txt")

boarding_passes = file.read().split("\n")

def findSeatRow(boarding_pass: str):

  rowMin = 0
  rowMax = 127

  #Characters 1 to 7 are used to find the seat row
  for i in range(0,6):

    if boarding_pass[i] == 'F':
      rowMax -= math.ceil((rowMax - rowMin) / 2)
    else:
      rowMin += math.ceil((rowMax - rowMin) / 2)


  if boarding_pass[6] == 'F':
    return rowMin
  else:
    return rowMax

def findSeatCol(boarding_pass: str):

  colMin = 0
  colMax = 7

  #Characters 8 to 10 are used to find the sead row
  for i in range(7,9):

    if boarding_pass[i] == 'L':
      colMax -= math.ceil((colMax - colMin) / 2)
    else:
      colMin += math.ceil((colMax - colMin) / 2)

  if boarding_pass[9] == 'L':
    return colMin
  else:
    return colMax


maxSeatId = 0

for i in range(0, len(boarding_passes)):
  seatId = 8 * findSeatRow(boarding_passes[i]) + findSeatCol(boarding_passes[i])
  if maxSeatId < seatId:
    maxSeatId = seatId

print(maxSeatId)