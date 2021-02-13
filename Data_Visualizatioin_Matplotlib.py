# Data_Visualizatioin_Matplotlib
#!/bin/python3

# work with the data file 'Auto_Import_1985.csv'
# read the file into the data frame 'df_auto'
import pandas as pd
print("HELLO")


df_auto = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv' ,
                        usecols = ['Make' ,
                                    'Fuel Type' ,
                                    'Aspiration' ,
                                    'Num of Doors' , 
                                    'Body Style' , 
                                    'Drive Wheels' ,
                                    'Num of Cylinders' ,
                                    'Horsepower' ,
                                    'City mpg' ,
                                    'Highway mpg' ,
                                    'Curb Weight',
                                    'Price']
                        )
# print the first 5 rows of the file
print(df_auto.head())
print()
print()
# import Matplotlib library
import matplotlib.pyplot as plt
# 1) ----  Scatter Plot  ----
fig, ax = plt.subplots()

# scatter plot: the city mpg against highway mpg
ax.scatter(df_auto['City mpg'] , df_auto['Highway mpg'])

# set a title and labels
ax.set_title('Autos Import for 1985 year')
ax.set_xlabel('City miles per gallon')
ax.set_ylabel('Highway miles per gallon')
plt.show()
print()

# scatter plot:curb weight against city  miles per gallon
fig, ax = plt.subplots()
ax.scatter(df_auto['Curb Weight'] , df_auto['City mpg'] , color = 'green')
ax.set_title('Auto Weight and Speed')
ax.set_xlabel('Curb Weight')
ax.set_ylabel('City mpg')
plt.show()

# 2) ----  Line chart  ----
# x-axis 'Price', y-axis 'City mpg'
fig , ax = plt.subplots()
# group by number of cylinders , average city speed 
avg_city_mpg = df_auto.groupby(['Body Style'])['Price'].mean()
avg_price = round(avg_city_mpg,1)
print(avg_price)




