# Data_Visualizatioin_Matplotlib
#!/bin/python3

# work with the data file 'Auto_Import_1985.csv'
# read the file into the data frame 'df_auto'
import pandas as pandas

df_auto = pd.read_csv(r'E:\_Python_Projects_Data\Data_Visualization\Auto_Import_1985.csv')
print(df_auto.head())
print()