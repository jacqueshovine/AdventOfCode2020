import string

def isBirthYearValid(date: str):
  return (len(date) == 4 
         and int(date) >= 1920
         and int(date) <= 2002)

def isIssueYearValid(date: str):
  return (len(date) == 4
         and int(date) >= 2010
         and int(date) <= 2020)

def isExpirationYearValid(date: str):
  return (len(date) == 4
         and int(date) >= 2020
         and int(date) <= 2030)

def isHeightValid(height: str):

  heightDigit = ''

  #Extracting numerical value from height
  for i in height:
    if i.isdigit():
      heightDigit += i

  #Checking the height unit
  if height.find("in") != -1:
    return (int(heightDigit) >= 59
            and int(heightDigit) <= 76)
  elif height.find("cm") != -1:
    return (int(heightDigit) >= 150
            and int(heightDigit) <= 193)
  else:
    return False

def isHairColorValid(color: str):

  #Color has to be an # followed by exactly 6 characters
  if len(color) != 7:
    return False

  hexa = '0123456789abcdef'

  for i in range(0, len(color)):
    if i == 0:
      if color[i] != '#':
        return False
    else:
      if hexa.find(color[i]) == -1:
        return False
  
  return True

def isEyeColorValid(color: str):

  validEyeColors = ['amb','blu','brn','gry','grn','hzl','oth']

  for i in validEyeColors:
    if color == i:
      return True

  return False

def isPassportIdValid(pid: str):
  
  return len(pid) == 9 and pid.isdigit()