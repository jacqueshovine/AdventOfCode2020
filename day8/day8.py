file = open("input.txt")

instructions_per_line = file.read().split("\n")

def processArgument(argument):

  argument_sign = argument[0]
  argument_value = int(argument.split(argument_sign)[1])

  if argument_sign == '+':
    return argument_value
  elif argument_sign == '-':
    return argument_value * -1


def processBootCode(instructions: list):

  #Instructions that have already been executed once
  executed = []
  accumulator = 0
  buffer = ""
  count = 0

  while True:

    #We added "end" at the last line of the input file to know when it terminates
    if instructions[count] == "end":
      success = True
      break

    if len(executed) != len(set(executed)):
      print("Last accumulator value : " + str(buffer))
      success = False
      break

    operation = instructions[count].split(" ")[0]
    argument = instructions[count].split(" ")[1]

    #Storing accumulator value before any changes
    buffer = accumulator

    if operation == "nop":
      count += 1
      continue
    elif operation == "acc":
      count += 1
      accumulator += processArgument(argument)
    elif operation == "jmp":
      count += processArgument(argument)

    executed.append(count)

  if success:
    return accumulator
  else:
    return -1

# !!! BRUTE FORCE !!! #
instructions_per_line_copy = instructions_per_line

for i in range(0, len(instructions_per_line_copy)):
  if instructions_per_line_copy[i].split(" ")[0] == "jmp":
    instructions_per_line_copy[i] = ("nop " + instructions_per_line_copy[i].split(" ")[1])
    test = processBootCode(instructions_per_line_copy)
    if test != -1:
      print("Accumulator value after program terminates: " + str(test))
      break
    else:
      #Reseting variable if the test failed
      instructions_per_line_copy[i] = ("jmp " + instructions_per_line_copy[i].split(" ")[1])
      continue
  elif instructions_per_line_copy[i].split(" ")[0] == "nop":
    instructions_per_line_copy[i] = ("jmp " + instructions_per_line_copy[i].split(" ")[1])
    test = processBootCode(instructions_per_line_copy)
    if test != -1:
      print("Accumulator value after program terminates: " + str(test))
      break
    else:
      #Reseting variable if the test failed
      instructions_per_line_copy[i] = ("nop " + instructions_per_line_copy[i].split(" ")[1])
      continue

print("Terminated")