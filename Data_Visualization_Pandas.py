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



'''
# ___________________________________________________________________________________________________________________________________________

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
print('Chargeable Income data set; first 5 rows')
print(income_df.head())
print()
# display the last 5 rows of the dataframe 'income_df'
print('Chargeable Income data set; last 5 rows')
print(income_df.tail())
print()

# check the data types of the columns and the presence of null values
print('dataframe "income_df" information:')
income_df.info()



# create a line chart plot
income_df.plot.line( x = 'year_of_assessment' , y = 'no_of_companies_assessed',
                    title = 'Number of asssesed companies')
plt.xlabel('Year')
plt.ylabel('Number of companies assessed')
plt.show()

income_df.plot.line( x = 'year_of_assessment' , y = 'donations' , color = 'orange' , title = 'Donations made by the companies')
plt.xlabel('Year')
plt.ylabel('Donations, $ thoudand * 10^6')
plt.show()

income_df.plot.line ( x = 'year_of_assessment' , y = 'total_income' , title = 'Total income of the companies')
plt.xlabel('Year')
plt.ylabel('Total income, $ thousand * 10^7')
plt.show()

income_df.plot.line ( x = 'year_of_assessment' , y = 'chargeable_income' , color = 'green', title = 'Chargeable income')
plt.xlabel('Year')
plt.ylabel('Chargeable income, $ thousand * 10^8')
plt.show()

# put multiple line charts at the same figure
income_df.drop(['no_of_companies_assessed' ], axis = 1).plot.line(x = 'year_of_assessment' ,
                title = 'Total income, chargeable income and donations made by the companies')
plt.xlabel('Year')
plt.ylabel('Amount, $ thousand * 10^8')
plt.show()
print()

# multiple subplots line charts
fig , ax = plt.subplots(2, figsize = (7,12))
income_df.plot.line( x = 'year_of_assessment' , y = 'total_income' , ax = ax[0])
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Total Income')


income_df.plot.line( x = 'year_of_assessment' , y = 'chargeable_income' , ax = ax[1])
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Chargeable Income')

plt.show()
# ___________________________________________________________________________________________________________________________________________________________
'''



# 3) ----  Histogram  ----
# 3.1) plot the occurences of the work hours per week
adults_df['Hours per Week'].plot.hist(color = 'grey' )
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Hours/week')
plt.title('Work Hours by Age')
plt.show()

# plot the frequencies of the age
adults_df['Age'].plot.hist( color = 'green')
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# 3.2) multiple histograms

#   --- horizontal order of the subplots

plt.figure(figsize = (10,5))

plt.subplot(121)
adults_df['Hours per Week'].plot.hist(color = 'grey' )
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Hours/week')
plt.title('Work Hours by Age')

plt.subplot(122)
adults_df['Age'].plot.hist( color = 'green')
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Frequency')
plt.title('Age Distribution')

plt.show()


#    --- vertical order of the subplots

plt.figure(figsize = (5,10))

plt.subplot(211)
adults_df['Hours per Week'].plot.hist(color = 'grey' )
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Hours/week')
plt.title('Work Hours by Age')

plt.subplot(212)
adults_df['Age'].plot.hist( color = 'green')
plt.grid()
plt.xlabel('Age, years')
plt.ylabel('Frequency')
plt.title('Age Distribution')

plt.show()


