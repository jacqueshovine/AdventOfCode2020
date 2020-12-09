file = open("input.txt")

answers_raw = file.read().split("\n\n")
answers_per_group = []

#Creating a table in which each index is a table that represents each group answers.
for i in range(0, len(answers_raw)):
  answers_per_group.append(answers_raw[i].split("\n"))

def countYes(answers: list):

  count = 0
  
  #For each group
  for i in range(0, len(answers)):

    #Contains letters for questions which someone in a group already answered "yes"
    yes_letters = []

    #For each person in a group
    for j in range(0, len(answers[i])):

      #For each question the person answered "yes", we check if someone from the same group already answered "yes"
      for k in range(0, len(answers[i][j])):
        if answers[i][j][k] in yes_letters:
          continue
        else:
          yes_letters.append(answers[i][j][k])
    
    count += len(yes_letters)

  return count

print(countYes(answers_per_group))