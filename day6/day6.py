file = open("input.txt")

answers_raw = file.read().split("\n\n")
answers_per_group = []

#Creating a table in which each index is a table that represents each group answers.
for i in range(0, len(answers_raw)):
  answers_per_group.append(answers_raw[i].split("\n"))

#PART 1 (counting questions to which anyone answered "yes")
def countAnyoneYes(answers: list):

  count = 0
  
  #For each group (one group = answers[i])
  for i in range(0, len(answers)):

    #Contains letters for questions which someone in a group already answered "yes"
    yes_letters = []

    #For each person in a group (one person = answers[i][j])
    for j in range(0, len(answers[i])):

      #For each question the person answered "yes", we check if someone from the same group already answered "yes". 
      #(one question that was answered with "yes" = answers[i][j][k])
      #If it isn't the case, we add the letter to yes_letters
      for k in range(0, len(answers[i][j])):
        if answers[i][j][k] in yes_letters:
          continue
        else:
          yes_letters.append(answers[i][j][k])
    
    count += len(yes_letters)

  return count

#PART 2 (counting questions to which everyone answered "yes")
def countEveryoneYes(answers: list):

  #Initialize an empty list that will contain all the lowercase alphabets (this will help to check answers)
  letters=[]
  for i in range(97,123):
      letters.append(chr(i))

  count = 0

  #For each group (one group = answers[i])
  for i in range(0, len(answers)):

    yes_letters = []

    #For each person in a group (one person = answers[i][j])
    for j in range(0, len(answers[i])):

      #Appending all questions where the person said "yes" to yes_letters (one question that was answered with "yes" = answers[i][j][k])
      for k in range(0, len(answers[i][j])):

        yes_letters.append(answers[i][j][k])

    #For each letter that can possibly exist, we check if it appears len(answers[i]) times. (This means that everyone in a given group answered "yes")
    for l in range(0, len(letters)):
      if yes_letters.count(letters[l]) == len(answers[i]):
        count += 1
    
  return count

print("With part 1 instructions, the sum of questions is : " + str(countAnyoneYes(answers_per_group)) + "\n")
print("With part 2 instructions, the sum of questions is : " + str(countEveryoneYes(answers_per_group)) + "\n")