# IMPORT ---
import pandas as pd

# IMPORT DATA FILE ---
myfile = pd.read_csv("sheetdata.csv")
df = pd.DataFrame(myfile)

# TASK 1 ---
# PRINT NUMBER OF ROWS AND COLUMNS ---
print("TASK 1: Number of Rows & Columns:")
print(df)

print('\n')
# TASK 2 ---
# PRINT ROWS 3-8 USING ILOC/LOC ---
print("TASK 2: Rows 3-8:")
print(df.iloc[3:9])

print('\n')
# TASK 3 ---
# MEAN OF ALL INCLUSIVE HOTELS ACROSS ALL DESTINATIONS ---
print("TASK 3: Mean of All Inclusive Hotels across all Destinations:")
inclusive = df.iloc[0:14, 3]
incmean = inclusive.mean()
print(incmean)

print('\n')
# TASK 4 ---
# LOWEST SCORING DESTINATION ---
print("TASK 4: Lowest Scoring Destination(s):")
print(df[df['Feedback out of 10'] == df['Feedback out of 10'].min()])

print('\n')
# TASK 5 ---
# HIGHEST SCORING DESTINATION ---
print("TASK 5: Highest Scoring Destination(s):")
print(df[df['Feedback out of 10'] == df['Feedback out of 10'].max()])

print('\n')
# TASK 6 ---
# MORE THAN 9 INCLUSIVE HOTELS ---
print("TASK 6: More than 9 All Inclusive Hotels:")
print(df[df['No of All Inclusive hotels'] > 9])

print('\n')
# TASK 7 ---
# DESTINATION SCORE ABOVE 8 ---
print("TASK 7: Destination Score above 8:")
print(df[df["Feedback out of 10"] > 8])

print('\n')
# TASK 8 ---
# DESTINATION SCORE BELOW 2 ---
print("TASK 8: Destination Score below 2:")
print(df[df["Feedback out of 10"] < 2])
