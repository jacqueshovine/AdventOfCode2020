file = open("input.txt")

instructions_per_line = file.read().split("\n")

def processArgument(argument):

  argument_sign = argument[0]
  argument_value = int(argument.split(argument_sign)[1])

  if argument_sign == '+':
    return argument_value
  elif argument_sign == '-':
    return argument_value * -1


#Instructions that have already been executed once
executed = []
accumulator = 0
buffer = ""
count = 0

while True:

  if len(executed) != len(set(executed)):
    print("Last accumulator value : " + str(buffer))
    break

  operation = instructions_per_line[count].split(" ")[0]
  argument = instructions_per_line[count].split(" ")[1]

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