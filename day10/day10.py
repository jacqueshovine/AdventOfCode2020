#------------------------------------------------------------------------
#PREPARING LIST

file = open("input.txt")

adapters = file.read().split("\n")

#Converting values to integers
for i in range(0, len(adapters)):
  adapters[i] = int(adapters[i])

#Adding charging outlet value (0)
adapters.insert(0, 0)

#Adding device built-in adapter value (max + 3)
adapters.append(max(adapters) + 3)

#Sorting the list
adapters.sort()

#------------------------------------------------------------------------

def calculateDifference(adapters: list):

  diff_1 = 0
  diff_3 = 0
  
  for i in range(0,len(adapters) - 1):
    if adapters[i + 1] - adapters[i] == 1:
      diff_1 += 1
    elif adapters[i + 1] - adapters[i] == 3:
      diff_3 += 1
    else:
      print(adapters[i + 1] - adapters[i])

  return diff_1 * diff_3

#Solution : 2590
print("1-jolt differences multiplied by 3-jolt differences : " + str(calculateDifference(adapters)))
