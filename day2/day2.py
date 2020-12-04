import pandas as pd

def splitPolicy (policy):

  policy_range = policy.split()[0]
  policy_letter = policy.split()[1]

  lowest = policy_range.split("-")[0]
  highest = policy_range.split("-")[1]

  splitted = {
    "lowest" : int(lowest),
    "highest": int(highest),
    "letter": policy_letter
  }

  return splitted

# Part 1
def isOldPolicyValid (policy, password):

  splitted_policy = splitPolicy(policy)
  letter_count = 0

  for i in range(len(password)):
    if password[i] == splitted_policy['letter']:
      letter_count += 1
  
  return letter_count >= splitted_policy['lowest'] and letter_count <= splitted_policy['highest']

# Part 2
def isCurrentPolicyValid (policy, password):

  splitted_policy = splitPolicy(policy)

  # ^ is the Python XOR operator
  return (password[splitted_policy['lowest']] == splitted_policy['letter']) ^ (password[splitted_policy['highest']] == splitted_policy['letter'])

passwords = pd.read_csv(r'input.csv',sep=':')
total = passwords.count()
length = total['password']

valid_passwords_old = 0
valid_passwords_current = 0

for i in range(0,length):
  if isOldPolicyValid(passwords.iloc[i]['policy'], passwords.iloc[i]['password']):
    valid_passwords_old += 1
  if isCurrentPolicyValid(passwords.iloc[i]['policy'], passwords.iloc[i]['password']):
    valid_passwords_current += 1

print("According to the old policy, "+ str(valid_passwords_old) + " are valid." + "\n")
print("According to the current policy, "+ str(valid_passwords_current) + " are valid." + "\n")

