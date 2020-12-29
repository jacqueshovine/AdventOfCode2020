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

def findWeakness(numbers: list):

  incorrectNumber = findNumber(numbers)

  #Initializing the range (a minimum of 2 numbers need to be added up)
  contiguous_range = 2

  #Increases the amount of numbers (range) that need to be added up each time we loop over the numbers list
  for i in range(0, len(numbers)):

    low_index = 0

    #The highest number is equal to the range : at first we take every 2 numbers in a row, then every 3, then 4...
    high_index = contiguous_range

    #Loops over list of numbers
    while high_index < len(numbers):

      numbers_to_sum = []

      #Adding numbers to be added up in a list
      for j in range(low_index, high_index):
        numbers_to_sum.append(numbers[j])
      
      #If the sum equals the number found for part 1, we return the sum of the smallest and the largest
      if sum(numbers_to_sum) == incorrectNumber:
        print("The numbers to sum are : " + str(numbers_to_sum))
        return min(numbers_to_sum) + max(numbers_to_sum)
      
      #Shifts the indexes to loop over different numbers every time
      low_index += 1
      high_index += 1

    #Increases the range at every go in the loop
    contiguous_range += 1


#Solution : 1492208709
incorrectNumber = findNumber(numbers)
print("The incorrect number is : " + str(incorrectNumber))

#Solution : 238243506
print("The encryption weakness is : " + str(findWeakness(numbers)))



