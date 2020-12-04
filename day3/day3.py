import pandas as pd

grid = pd.read_csv(r'input.csv')
total = grid.count()
grid_length = total['rows']

#Each row has 31 characters (from 0 to 30)
row_length = len(grid.iloc[0]['rows'])

def countTrees(right, down):
  #Total of trees encountered
  tree_count = 0

  #Used in the for loop to iterate over each character of the current row. Starts at the value of "right" for the first line.
  row_counter = right

  for i in range(0, grid_length - down, down):
    #If row_counter exceeds row_length - 1 (starts from 0 to row_length - 1), we need to set it back to loop over the next row.
    if row_counter > row_length - 1:
      row_counter -= row_length
    #Checking if there is a tree at the next row. Adds +3 to the row_counter for the next row check.
    if grid.iloc[i + down]['rows'][row_counter] == '#':
      tree_count += 1
      row_counter += right
    else:
      row_counter += right

  return tree_count

print("Right 1, down 1 : " + str(countTrees(1,1)) + " trees\n")
print("Right 3, down 1 : " + str(countTrees(3,1)) + " trees\n")
print("Right 5 down 1 : " + str(countTrees(5,1)) + " trees\n")
print("Right 7, down 1 : " + str(countTrees(7,1)) + " trees\n")
print("Right 1, down 2 : " + str(countTrees(1,2)) + " trees\n")

print("Answer : " + str(countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2)))

