file = open("input.txt")

numbers = file.read().split("\n")

for i in range(0, len(numbers)):
  numbers[i] = int(numbers[i])

def findNumber(numbers: list):

  low_index = 0
  high_index = 25

  current_number = 0
  valid = False
 
  #For each number in the file (starting after the preamble)
  for i in range(25, len(numbers)):
    #We try adding up each number with each other number (excluding itself)
    for j in range(low_index, high_index):
      for k in range(low_index, high_index):
        if numbers[j] != numbers[k] and numbers[j] + numbers[k] == numbers[high_index]:
          valid = True
          break
        else:
          current_number = numbers[high_index]
    
    #If one number fails the test, we return it
    if not valid:
      return current_number

    #We shift the indexes for the next run in the loop
    low_index += 1
    high_index += 1

    #We set the flag back to false for the next test
    valid = False

  return -1

print(findNumber(numbers))

