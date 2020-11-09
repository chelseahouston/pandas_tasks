# IMPORT ---
import pandas as pd

# IMPORT DATA FILE ---
myfile = pd.read_csv("sheetdata.csv")

# TASK 1 ---
# PRINT NUMBER OF ROWS AND COLUMNS ---
print(myfile)

print('\n')
# TASK 2 ---
# PRINT ROWS 3-8 USING ILOC/LOC ---
print(myfile.iloc[3:9])

print('\n')
# TASK 3 ---
