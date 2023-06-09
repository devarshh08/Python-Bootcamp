while True:
  row1 = ["⬜", "⬜", "⬜"]
  row2 = ["⬜", "⬜", "⬜"]
  row3 = ["⬜", "⬜", "⬜"]
  map = [row1, row2, row3]
  print(f"{row1}\n{row2}\n{row3}")
  position = input("""Where do you want to put the treasure?\nEnter value in columnrow format(not seperated by a space) \n""")
  print(" ")
  #here first we assign the input to two different values representing rows and columns
  column = position[0]
  row = position[1]
  #we convert the rows and columns to integer type
  column = int(column)
  row = int(row)
  #since we have row and column number, but we have to convert it to an index that starts from 0, we minus 1 from each
  column -= 1
  row -= 1
  #we assign row number to the list index in map, for example if we have input of column 3 row 2, that will be replacing the element of index 2(third element) in list of index 1(second list)
  list_is = map[row]
  list_is[column] = "X"
  map[row] = list_is
  print(f"Hurray! You have put the treasure at {position}\n{row1}\n{row2}\n{row3}\n")
  print("-----------------------------------\n\n")