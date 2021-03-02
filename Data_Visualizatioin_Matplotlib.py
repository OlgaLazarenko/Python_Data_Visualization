# Data_Visualizatioin_Matplotlib
#!/bin/python3

# import Matplotlib library
import matplotlib.pyplot as plt
import pandas as pd

# work with the data file 'Auto_Import_1985.csv'
# read the file

auto = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv' ,
                        usecols = [ 'Symboling' ,
                                    'Make' ,
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
                                    'Engine Size' ,
                                    'Price']
                        )
# print the first 5 rows of the file
print(auto.head())
print()
print()

# 1) ----  Scatter Plot  ----
fig, ax = plt.subplots()

# scatter plot: the city mpg against highway mpg
ax.scatter(auto['City mpg'] , auto['Highway mpg'])

# set a title and labels
ax.set_title('Auto Imports for 1985 year')
ax.set_xlabel('City miles per gallon')
ax.set_ylabel('Highway miles per gallon')
ax.grid(True)
plt.show()
print()

# scatter plot:curb weight against city  miles per gallon
fig, ax = plt.subplots()
ax.scatter(auto['Curb Weight'] , auto['City mpg'] , color = 'green')
ax.set_title('Auto Weight and Speed')
ax.set_xlabel('Curb Weight')
ax.set_ylabel('City mpg')
plt.show()


# 2) ----  Histograms  ----
# plot the symboling/risk factor column
fig, ax = plt.subplots()
ax.hist(auto['Symboling'] , color = 'brown')
ax.set_title('Risk factor (-3 the most risky, 3 the safest)')
ax.set_xlabel('Risk factor')
ax.set_ylabel('Frequency')
plt.show()

# plot the frequency of the number of doors
fig, ax = plt.subplots()
ax.hist(auto['City mpg'] , color = 'grey')
ax.set_title('Frequency of the mileage')
ax.set_xlabel('City mileage, mpg')
ax.set_ylabel('Frequency')
plt.show()

# plot the frequency of the engine size
fig, ax = plt.subplots()

ax.hist(auto['Engine Size'], color = 'orange')
ax.set_title('Imported cars engine size')
ax.set_xlabel('Engine size')
ax.set_ylabel('Frequency')
plt.show()



# 3) ----  Bar chart   ----
# show the number of imported cars by the car's body style
auto['Body Style'].value_counts().plot(kind = 'bar', figsize = (10,8) , rot = 30 , color = 'purple')
plt.title('Number of imported cars by the body style')
plt.xlabel('Body style')
plt.ylabel('Number of imported cars')

'''

'''
numbers = auto['Body Style'].value_counts()
print(numbers)
print("***")
for num in numbers :
    print(num)
print()
for i in numbers:
    plt.text( x = i , y = data , s = f"{auto}")
plt.tight_layout()


plt.show()


# ) ----  Line chart  ----
# x-axis 'Price', y-axis 'City mpg'
fig , ax = plt.subplots()
# group by number of cylinders , average city speed 
avg_city_mpg = auto.groupby(['Num of Cylinders'])['City mpg'].mean()
avg_city_mpg = round(avg_city_mpg,1)
print(avg_city_mpg)





