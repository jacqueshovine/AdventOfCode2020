#Contents of the input file
batch_file = open("input.txt")

#Input file split by passports
passports = batch_file.read().split("\n\n")

def isPassportValid (passport):
  
  mandatoryFields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
  ]

  fieldCount = 0

  for i in range(0, len(mandatoryFields)):
    if passport.find(mandatoryFields[i]) != -1:
      fieldCount += 1
    else:
      continue

  return fieldCount == len(mandatoryFields)


validPassportCount = 0

for i in range(0, len(passports)):
  if isPassportValid(passports[i]):
    validPassportCount += 1
  else:
    continue

print(validPassportCount)
