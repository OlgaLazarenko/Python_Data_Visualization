# Data_Visualizatioin_Pandas
#!/bin/python3

# import Pandas library
import pandas as pd
import matplotlib.pyplot as plt

# work with the data file 'Adults.csv' from the folder 'Adults_Data_Set'
# read the file into the data frame 'adults_df'

adults_df = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Adults_Data_Set\Adults.csv" ,
                        usecols  = ['Age' ,
                                  'Work Class' ,    
                                  'Education' , 
                                  'Marital Status' ,
                                  'Occupation' , 
                                  'Relationship' ,
                                  'Race' ,
                                  'Sex' , 
                                  'Hours per Week' , 
                                  'Country']
                        )
print(adults_df)
print()
# display the first 5 rows of the data
print('the first five rows')
print(adults_df.head())
print()

# display the last 5 elements of the data
print('the last five rows')
print(adults_df.tail())
print()

# check the data type of the columns at the dataframe 'adults_df' and if there are null values
print('check the data types of the columns at the dataframe "adults_df"')
adults_df.info()
print()
# 1) ----  Scatter Plot  ----

# scatter plot: 'Age' vs 'Hours per Week'
adults_df.plot.scatter( x = 'Age' , y = 'Hours per Week' , title = 'Work hours and age')
# to see the plot, add the Matplot syntax to show the plot
plt.show()
print()
# _______________________________________________________________________________________________________________________________________________



# 2) ----  Line Chart  ----
# read the file 'Chargeable Income.csv'
income_df = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Company_Income\Chargeable_Income.csv" ,
                        usecols = ['year_of_assessment' ,
                                  'no_of_companies_assessed' ,
                                  'chargeable_income' ,
                                  'total_income' ,
                                  'donations']
                        )
# show the first 5 rows of the data frame
print('Chargeable Income data set')
print(income_df.head())

# create a line chart plot
income_df.plot.line( x = 'year_of_assessment' , y = 'no_of_companies_assessed', title = 'Number of asssesed companies')
plt.show()

income_df.plot.line( x = 'year_of_assessment' , y = 'donations' , title = 'Donations made by the companies')
plt.show()

income_df.plot.line ( x = 'year_of_assessment' , y = 'total_income' , title = 'Total income of the companies')
plt.show()

income_df.plot.line ( x = 'year_of_assessment' , y = 'chargeable_income' , title = 'Chargeable income')
plt.show()

# put multiple line charts at the same figure
income_df.drop(['no_of_companies_assessed' ], axis = 1).plot.line(x = 'year_of_assessment', 
                title = 'Total income, chargeable income and donations made by the companies')
plt.show()
print()
# ___________________________________________________________________________________________________________________________________________________________

# 3) ----  Histogram  ----
# plot the occurences of the hours per week
adults_df['Hours per Week'].plot.hist()
plt.show()

# plot the frequencies of the age
adults_df['Age'].plot.hist()
plt.show()

# multiple histograms



