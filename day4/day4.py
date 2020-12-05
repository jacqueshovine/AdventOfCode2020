import passportValidityFunctions as pv

#Contents of the input file
batch_file = open("input.txt")

#Input file split by passports
passports = batch_file.read().split("\n\n")

def hasRequiredFields (passport: str):
  
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
    #find() returns the index where the string was found. If not found, returns -1
    if passport.find(mandatoryFields[i]) != -1:
      fieldCount += 1
    else:
      continue

  return fieldCount == len(mandatoryFields)

def isPassportValid (passport: str):

  splitFields = passport.split()
  fields = {
    "byr": '',
    "iyr": '',
    "eyr": '',
    "hgt": '',
    "hcl": '',
    "ecl": '',
    "pid": ''
  }

  #Filling the fields object
  for i in range(0, len(splitFields)):
    for field in fields:
      #Comparing keys of the "fields" object to keys from the parameter "passport"
      if field == splitFields[i].split(":")[0]:
        fields[field] = splitFields[i].split(":")[1]
  
  return (pv.isBirthYearValid(fields["byr"])
          and pv.isIssueYearValid(fields["iyr"])
          and pv.isExpirationYearValid(fields["eyr"])
          and pv.isHeightValid(fields["hgt"])
          and pv.isHairColorValid(fields["hcl"])
          and pv.isEyeColorValid(fields["ecl"])
          and pv.isPassportIdValid(fields["pid"]))


requiredFieldsPassports = []

#Selecting passports that have required fields
for i in range(0, len(passports)):
  if hasRequiredFields(passports[i]):
    requiredFieldsPassports.append(passports[i])
  else:
    continue

print(str(len(requiredFieldsPassports)) + " passports meet the required fields criteria.\n")

validPassports = []

#Checking if passports are valid
for i in range(0, len(requiredFieldsPassports)):
  if isPassportValid(requiredFieldsPassports[i]):
    validPassports.append(requiredFieldsPassports[i])
  else:
    continue

print(str(len(validPassports)) + " passports are valid.\n")
