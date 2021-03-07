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
                                    'Engine Type' ,
                                    'Price']
                        )
# print the first 5 rows of the file
print(auto.head())
print()
print()

# _____________________________________________________________________________________

# 1) ----  Scatter Plot  ----
fig, ax = plt.subplots()

# 1.1) scatter plot: the city mpg against highway mpg
ax.scatter(auto['City mpg'] , auto['Highway mpg'])

# set a title and labels
ax.set_title('Auto Imports, 1985 year')
ax.set_xlabel('City miles per gallon')
ax.set_ylabel('Highway miles per gallon')
ax.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True) # do not show the grid lines on the graph/the data points
ax.set_facecolor('aliceblue')
plt.show()
print()

# 1.2) scatter plot:curb weight against city  miles per gallon
fig, ax = plt.subplots()
ax.scatter(auto['Curb Weight'] , auto['City mpg'] , color = 'green')
ax.set_title('Auto Weight and Speed')
ax.set_xlabel('Curb Weight')
ax.set_ylabel('City mpg')
ax.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('lavender')
plt.show()

# 1.3) subplots of the scatter graphs, vertical order
fig1, (ax1 , ax2 ) = plt.subplots(nrows = 2 , ncols = 1 , figsize = (5, 10))

ax1.scatter(auto['City mpg'] , auto['Highway mpg'])
ax1.set_title('Auto Imports, 1985 year')
ax1.set_xlabel('City miles per gallon')
ax1.set_ylabel('Highway miles per gallon')
ax1.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax1.set_axisbelow(True)
ax1.set_facecolor('azure')


ax2.scatter(auto['Curb Weight'] , auto['City mpg'] , color = 'green')
ax2.set_title('Auto Weight and Speed')
ax2.set_xlabel('Curb Weight')
ax2.set_ylabel('City mpg')
ax2.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax2.set_axisbelow(True)
ax2.set_facecolor('azure')

plt.show()


# 1.4) subplots of the scatter graphs, horizontal order
fig1, (ax1 , ax2 ) = plt.subplots(nrows = 1 , ncols = 2 , figsize = (10, 5))

ax1.scatter(auto['City mpg'] , auto['Highway mpg'])
ax1.set_title('Auto Imports, 1985 year')
ax1.set_xlabel('City miles per gallon')
ax1.set_ylabel('Highway miles per gallon')
ax1.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax1.set_axisbelow(True)
ax1.set_facecolor('beige')

ax2.scatter(auto['Curb Weight'] , auto['City mpg'] , color = 'green')
ax2.set_title('Auto Weight and Speed')
ax2.set_xlabel('Curb Weight')
ax2.set_ylabel('City mpg')
ax2.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax2.set_axisbelow(True)
ax2.set_facecolor('beige')

plt.show()

# _______________________________________________________________________________________________________

# 2) ----  Histograms  ----
# 2.1) plot the symboling/risk factor column
fig, ax = plt.subplots()
ax.hist(auto['Symboling'] , color = 'brown')
ax.set_title('Risk factor (-3 the most risky, 3 the safest)')
ax.set_xlabel('Risk factor')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
plt.show()

# 2.2) plot the frequency of the mileage
fig, ax = plt.subplots()
ax.hist(auto['City mpg'] , color = 'grey')
ax.set_title('Frequency of the mileage')
ax.set_xlabel('City mileage, mpg')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('lightcyan')
plt.show()

# 2.3) plot the frequency of the engine size
fig, ax = plt.subplots()
ax.hist(auto['Engine Size'], color = 'orange')
ax.set_title('Imported cars engine size')
ax.set_xlabel('Engine size')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('cornsilk')
plt.show()

# 2.3) subplot the historams at the vertical order
fig , (ax1,ax2,ax3,ax4) = plt.subplots(nrows = 4 , ncols = 1, figsize = (5,17))

ax1.hist(auto['Num of Doors'] , color = 'brown')
ax1.set_title('Risk factor (-3 is the most risky, 3 is the safest)')
ax1.set_xlabel('Risk factor')
ax1.set_ylabel('Frequency')
ax1.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax1.set_axisbelow(True)
ax1.set_facecolor('seashell')


ax2.hist(auto['City mpg'] , color = 'indigo')
ax2.set_title('Frequency of the mileage')
ax2.set_xlabel('City mileage, mpg')
ax2.set_ylabel('Frequency')
ax2.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax2.set_axisbelow(True)
ax2.set_facecolor('seashell')


ax3.hist(auto['Engine Type'], color = 'green')
ax3.set_title('')
ax3.set_xlabel('Engine Type')
ax3.set_ylabel('Frequency')
ax3.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax3.set_axisbelow(True)
ax3.set_facecolor('seashell')

ax4.hist(auto['Num of Cylinders'], color = 'purple')
ax4.set_title('')
ax4.set_xlabel('Num of Cylinders')
ax4.set_ylabel('Frequency')
ax4.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax4.set_axisbelow(True)
ax4.set_facecolor('seashell')


fig.savefig('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Histograms_RiskFactor_Mileage_EngineType_NumCylinders.png')
plt.show()

# 2.4) subplot the histograms at the horizontal order 
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (15,5))
ax1.hist(auto['Fuel Type'] , color = 'blue')
ax1.set_title('Fuel type of the imported cars')
ax1.set_xlabel('Fuel Type')
ax1.set_ylabel('Frequency')
ax1.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax1.set_axisbelow(True)
ax1.set_facecolor('linen')

ax2.hist(auto['Num of Doors'] , color = 'brown')
ax2.set_title('Autos Number of Doors')
ax2.set_xlabel('Number of Doors')
ax2.set_ylabel('Frequency')
ax2.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax2.set_axisbelow(True)
ax2.set_facecolor('linen')

ax3.hist(auto['Body Style'] , color = 'green')
ax3.set_title('Imported Autos Body Style')
ax3.set_xlabel('Body Style')
ax3.set_ylabel('Frequency')
ax3.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax3.set_axisbelow(True)
ax3.set_facecolor('linen')

# save the figure to the image file
fig.savefig('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Histograms_FuelType_NumDoors_BodyStyle.png')
plt.show()







'''
# 3) ----  Bar chart   ----
# show the number of imported cars by the car's body style
auto['Body Style'].value_counts().plot(kind = 'bar', figsize = (10,8) , rot = 30 , color = 'purple')
plt.title('Number of imported cars by the body style')
plt.xlabel('Body style')
plt.ylabel('Number of imported cars')



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
'''





