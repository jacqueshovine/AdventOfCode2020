#Contents of the input file
file = open("input.txt")

boarding_passes = file.read().split("\n")

print(boarding_passes)

def findSeatRow(boarding_pass: str):
