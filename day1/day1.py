import pandas as pd

#Type : DataFrame
numbers = pd.read_csv(r'input.csv')
total = numbers.count()
length = total['numbers']

for i in range(0,length):
  for j in range(i + 1, length):
    if numbers.iloc[i]['numbers'] + numbers.iloc[j]['numbers'] == 2020:
      result_1 = numbers.iloc[i]['numbers'] * numbers.iloc[j]['numbers']
      break
  else:
    continue
  break

for i in range(0,length):
  for j in range(i + 1, length):
    #Adding up first two numbers. The result must be lower than 2020
    step1 = (numbers.iloc[i]['numbers'] + numbers.iloc[j]['numbers'])
    if 2020 - step1 > 0:
      for k in range(j + 1, length):
        #Adding up the three numbers
        step2 = step1 + (numbers.iloc[k]['numbers'])
        if step2 == 2020:
          result_2 = (numbers.iloc[i]['numbers'] * numbers.iloc[j]['numbers'] * numbers.iloc[k]['numbers'])
          break
      else:
        continue
      break
  else:
    continue
  break



print('Product of the two numbers : ' + str(result_1) + '\n') #Product of the two numbers that sum to 2020
print('Product of the three numbers : ' + str(result_2) + '\n') #Product of the two numbers that sum to 2020
