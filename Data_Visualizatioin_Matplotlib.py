# Data_Visualizatioin_Matplotlib
#!/bin/python3

# import Matplotlib library
import matplotlib.pyplot as plt
import pandas as pd


from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation


auto = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv' )
'''
schema = Schema ([
    Column('Symboling', [InRangeValidation(-3,3)] ) ,  # integer from -3 to 3 
    Column('Normalized Loss', [InRangeValidation(65,256)] )  , # integer from 65 to 256
    Column('Make',[LeadingWhitespaceValidation(), TrailingWhitespaceValidation()] )  , # text
    Column('Fuel Type', [InListValidation(['diesel', 'gas'])]), # diesel, gas
    Column('Aspiration'), # text
    Column('Num of Doors' , [InListValidation(['two', 'four'])]), # text (two, four)
    Column('Body Style' , [InListValidation(['hardtop', 'wagon','sedan','hatchback', 'convertible'])] ), # text: hardtop, wagon, sedan, hatchback, convertible
    Column('Drive Wheels' , [InListValidation(['4wd', 'fwd' , 'rwd'])]), # text: 4wd, fwd, rwd
    Column('Engine Location' , [InListValidation(['front', 'rear'])]), # text: front, rear
    Column('Wheel Base' , [InRangeValidation([86.6,120.9])] ) ,  # decimal from 86.6 to 120.9
    Column('Length' , [InRangeValidation(65,256)] )  ,  # decimal from 141.1 to 208.1
    Column('Width' , [InRangeValidation(60.3,72.3)] ) ,  # decimal from 60.3 to 72.3
    Column('Height' , [InRangeValidation(47.8,59.8)] ) ,   # decimal from 47.8 to 59.8
    Column('Curb Weight' , [InRangeValidation(1488,4066)] ) ,   # integer from 1488 to 4066
    Column('Engine Type'),[InListValidation(['dohc', 'dohcv', 'l', 'ohc', 'ohcf', 'ohcv', 'rotor'])] , # text
    Column('Num of Cylinders' , [InListValidation(['two','four','three','five','six','eight','twelve'])]) , # text: eight, five, four, six, three, twelve, two
    Column('Engine Size' , [InRangeValidation(61,326)]) ,  # integer from 61 to 326
    Column('Fuel System' , [InListValidation(['1bbl', '2bbl', '4bbl', 'idi','mfi','mpfi','spdi','spfi'])]), #string: 1bbl, 2bbl, 4bbl, idi,mfi,mpfi,spdi,spfi
    Column('Bore' , [InRangeValidation(2.54,3.94)] ) , # decimal from 2.54 to 3.94
    Column('Stroke', [InRangeValidation(2.07,4.17)] ) , #decimal from 2.07 to 4.17
    Column('Compression Ratio' , [InRangeValidation(7,23)] ), #  integer: from 7 to 23
    Column('Horsepower' , [InRangeValidation(48,288)] ),  # integer:from 48 to 288
    Column('Peak rmp'), [InRangeValidation(4150,6600)]  , # integer: from 4150 to 6600
    Column('City mpg'), [InRangeValidation(13,49)]  , #integer: from 13 to 49
    Column('Highway mpg'), [InRangeValidation(16,54)] ,  # integer: 16 to 54
    Column('Price'), [InRangeValidation(5118,45400)]  # integer from 5118 to 45400
])

test_file = pd.read_csv(('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv'))


print()
errors = schema.validate(test_file)
for error in errors:
    print(error)
'''
# The data types of the columns ____________________________________________
print()
print('Check the data type of the columns:')
print()
print('Column Name   |  Data Type')
print('____________________________')
print()
print(auto.dtypes)
print()


auto = auto[auto['Price']  != '?'] # remove rows with <?> at the column <Price> from the data frame
auto['Price'] = auto['Price'].astype(str).astype(int) # convert the values of the column <Price> to  the integer data type
print()
print()
print('the values at the column <Price> are integer data type now')
print(auto.dtypes)
print()

# _________________________________________________________________________________

# Create aggregations 
# group by <Body Style>, aggregate(mean)
auto_agg = auto.groupby('Body Style').Price.agg(['mean']).astype(int)
print(auto_agg)
print()
sorted_auto_agg = auto_agg.sort_values(['mean'] , ascending = False) # sort the avg price at the descending order 
print(sorted_auto_agg)
sorted_auto_agg.plot(kind='bar', rot = 0, legend = False) # create bar chart for the aggregation, display the greatest values first
plt.xlabel('Body Style')
plt.ylabel('Average Price, $ US')
plt.show() # display the bar chart

fig, axes = plt.subplots()
fig.set_facecolor('beige')
ax = sorted_auto_agg.plot( use_index = True , y = 'mean' , kind = 'bar' , ax = axes , legend = False , rot = 0)
ax.set_xlabel('Car Body Style' , fontsize = 12, color = 'purple')
ax.set_ylabel('Car Average Price, $ US', fontsize = 12 , color = 'purple')

plt.show()






"""
print("*---------------------------------------------------------*")
print()

print('Sort the DataFrame <auto_new> by the column <Price> the descending way')
auto_new.sort_values( by = ['Price'] , inplace = True , ascending = False)
print("Sorted <auto_new> DataFrame")
print(auto_new)




# work with the data file 'Auto_Import_1985.csv'

# Data Validation
# define the checking methonds

def decimal_check(value): # check of a value is a decimal number 
    try:
        Decimal(dec_number)
    except InvalidOperation:
        return False
    return True

def integer_check(value): # check if a value is a integer
    try:
        int(value)
    except ValueError:
        return False
    return True

def text_check(value): # check if a value is a text string
    try:
        str(value)
    except

decimal_validation = [CustomerElementValidation(lambda d: decimal_check(d) , 'is not decimal')]
integer_validation = [CustomerElementValidation(lambda i: integer_check(b) , 'is not integer')]
'null_validation = [CustomerElementValidation(lambda d: d is not  np.nan, 'this field cannot be null']


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

print('Questions and Answers:')
print()
print('______________________________________________________')
print()
print('Question: What are the top 3 most expensive cars?')
print()
# sort the data frame by the column Price, the descending way and obtain top 3 rows
auto_sorted = auto.sort_values( by = ['Price'] , inplace = False , ascending = False)
print(auto_sorted)

print('Question: What are the top 3 car models with highest mileage (city, highway')
print('_______________________________________________________')
print()
# Which cars are more imported: gaspline of diesel fuel type?
print('Question: Which cars are more imported: gas of diesel fuel type?')
diesel_cars = auto[auto['Fuel Type'] == 'diesel'] # imported cars of diesel fuel type
num_diesel_cars = len(diesel_cars.index)


gasoline_cars = auto[auto['Fuel Type'] == 'gas'] # this data frame only contains the gasoline type cars
num_gasoline_cars = len(gasoline_cars.index)
print()
total_num_cars = len(auto.index)
percent_gasoline_cars = round((100 * num_gasoline_cars/total_num_cars),1)
percent_diesel_cars = round((100 * num_diesel_cars/total_num_cars),1)

print('Total number of imported cars: ' + str(total_num_cars))
print("Number of imported cars by the fuel type: ")
print('Gasoline: ' + str(num_gasoline_cars) + '(' + str(percent_gasoline_cars) + ' %)')
print('Diesel: ' + str(num_diesel_cars) + '(' + str(percent_diesel_cars) + ' %)')
print()
print('Answer: ')
if num_gasoline_cars > num_diesel_cars :
    print(str(percent_gasoline_cars) + " "% of the imported cars are gasoline cars" )
elif num_diesel_cars > num_gasoline_cars :
    print(print(str(percent_diesel_cars) + "% of the imported cars are diesel cars" ))
else:
    print('Gasoline and diesel cars are imported at the some numbers')

print('_______________________________________________________')

print()
# What the body style of the imported cars is more in demand?
print("Question: What the body style of the imported cars is more popular?")
print()
list_body_style = auto['Body Style'].unique() # unique body styles
print('Car body styles: ')
for style in list_body_style :
    print(style)

print()
print("Car body style: number of cars")
list_num =[] # this list will contain the number of cars for each body style
for style in list_body_style :
    num_cars = len(auto[auto['Body Style'] == style])
    print(style + ': ' + str(num_cars))
    list_num.append(num_cars) # populate the list

print()

sorted_list_num = sorted(list_num, reverse = True)
max_num = sorted_list_num[0]


position_num = list_num.index(max_num)
position_body_style = position_num
body_style = list_body_style[position_body_style]

print()
percent = round((100 * max_num / total_num_cars),1)
print('Answer: ' + body_style + ' is the most popular car body style; ')
print(str(max_num) + ' cars are sedans and it makes ' + str(percent)+'% of all imported cars')
print('___________________________________________________')

print()
# What cars are more in demand: 2-doors or  4-doors ?
print('Question: What cars are more in demand: 2-door or 4-door?')
print()
list_doors = auto['Num of Doors'].unique()

print('Number of doors :')
for door in list_doors :
    print(door)

print()

list_cars = []
print('Number of doors : Number of cars')
for door in list_doors :
    num_cars = len(auto[auto['Num of Doors'] == door ])
    print(door + ': ' + str(num_cars))
    list_cars.append(num_cars) # populate the list

print()
print(list_doors)
print(list_cars)

sorted_list_cars = sorted(list_cars , reverse = True)
max_cars = sorted_list_cars[0]
print(max_cars)

position = list_cars.index(max_cars)
num_doors = list_doors[position]
print(num_doors)

print()
percent = round((100 * max_cars / total_num_cars),1)
print('Answer: ' + num_doors + '-door cars are more in demand and  they make '  + str(percent)+'% of all imported cars')

print('_________________________________________________________')

position_num = list_num_doors.index(max_num_cars)
num_doors = list_num_doors[position_num]
print(num_doors)

# 1) ----  Scatter Plot  ----


# 1.1) scatter plot: the city mpg against highway mpg
fig, ax = plt.subplots()
fig.set_facecolor('gainsboro')

ax.scatter(auto['City mpg'] , auto['Highway mpg'])
# set a title and labels
ax.set_title('Auto Imports, 1985 year')
ax.set_xlabel('City miles per gallon')
ax.set_ylabel('Highway miles per gallon')
ax.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True) # do not show the grid lines on the graph/the data points
ax.set_facecolor('beige')
plt.show()
print()

# 1.2) scatter plot:curb weight against city  miles per gallon
fig, ax = plt.subplots()
fig.set_facecolor('gainsboro')

ax.scatter(auto['Curb Weight'] , auto['City mpg'] , color = 'green')
ax.set_title('Auto Weight and Speed')
ax.set_xlabel('Curb Weight')
ax.set_ylabel('City mpg')
ax.grid( color = 'brown' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('lavender')
plt.show()

# 1.3) subplots of the scatter graphs, vertical order
fig, (ax1 , ax2 ) = plt.subplots(nrows = 2 , ncols = 1 , figsize = (5, 10))
fig.set_facecolor('gainsboro')

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


# 1.4) subplots of the scatter graphs, horizontal order
fig, (ax1 , ax2 ) = plt.subplots(nrows = 1 , ncols = 2 , figsize = (10, 5))
fig.set_facecolor('gainsboro')

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
fig.set_facecolor('lightcyan')

ax.hist(auto['Symboling'] , color = 'salmon' , align = 'mid' , edgecolor = 'royalblue', linewidth = 3 )
ax.set_title('Risk factor (-3 the most risky, 3 the safest)')
ax.set_xlabel('Risk factor')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('beige')
plt.show()

# 2.2) plot the frequency of the mileage
fig, ax = plt.subplots()
fig.set_facecolor('gainsboro')

ax.hist(auto['City mpg'] , color = 'grey', edgecolor = 'red' , linewidth = 2)
ax.set_title('Frequency of the mileage')
ax.set_xlabel('City mileage, mpg')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('lightcyan')
plt.show()
# 2.3) plot the frequency of the engine size
fig, ax = plt.subplots()
fig.set_facecolor('gainsboro')

ax.hist(auto['Engine Size'], color = 'orange' , edgecolor = 'black' , linewidth = 1.5)
ax.set_title('Imported cars engine size')
ax.set_xlabel('Engine size')
ax.set_ylabel('Frequency')
ax.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax.set_axisbelow(True)
ax.set_facecolor('cornsilk')
plt.show()

# 2.4) subplot the historams at the vertical order
fig , (ax1,ax2,ax3,ax4) = plt.subplots(nrows = 4 , ncols = 1, figsize = (5,17))
fig.set_facecolor('gainsboro')

ax1.hist(auto['Num of Doors'] , color = 'brown', edgecolor = 'orange' , linewidth = 1.5)
ax1.set_title('Risk factor (-3 is the most risky, 3 is the safest)')
ax1.set_xlabel('Risk factor')
ax1.set_ylabel('Frequency')
ax1.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax1.set_axisbelow(True)
ax1.set_facecolor('beige')


ax2.hist(auto['City mpg'] , color = 'indigo', edgecolor = 'orange' , linewidth = 1.5 )
ax2.set_title('Frequency of the mileage')
ax2.set_xlabel('City mileage, mpg')
ax2.set_ylabel('Frequency')
ax2.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax2.set_axisbelow(True)
ax2.set_facecolor('beige')


ax3.hist(auto['Engine Type'], color = 'green', edgecolor = 'orange' , linewidth = 1.5)
ax3.set_title('')
ax3.set_xlabel('Engine Type')
ax3.set_ylabel('Frequency')
ax3.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax3.set_axisbelow(True)
ax3.set_facecolor('beige')

ax4.hist(auto['Num of Cylinders'], color = 'purple', edgecolor = 'orange' , linewidth = 1.5)
ax4.set_title('')
ax4.set_xlabel('Num of Cylinders')
ax4.set_ylabel('Frequency')
ax4.grid( color = 'grey' , linestyle = 'dashed', linewidth = 0.8)
ax4.set_axisbelow(True)
ax4.set_facecolor('beige')


fig.savefig('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Histograms_RiskFactor_Mileage_EngineType_NumCylinders.png')
plt.show()

# 2.5) subplot the histograms at the horizontal order 
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (15,5))
fig.set_facecolor('gainsboro')

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

# 2.6) save the figure to the image file
fig.savefig('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Histograms_FuelType_NumDoors_BodyStyle.png')
plt.show()

# _________________________________________________________________________________________________________________


# 3) ----  Bar chart   ----

# 3.1) bar chart: number of imported cars by the car's body style
fig, ax = plt.subplots()
fig.set_facecolor('lightcyan')
# count the occurences of each class
data = auto['Body Style'].value_counts()
# get x and y data
points = data.index
frequency = data.values
# create bar chart
ax.bar(points,frequency,color = 'forestgreen')
# set title and labels
ax.set_title('Number of imported cars by body style')
ax.set_xlabel('Body style')
ax.set_ylabel('Number of imported cars')
ax.set_facecolor('beige')
plt.show()

# 3.2) bar chart : price of the imported cars by the car make
fig, ax = plt.subplots()
fig.set_facecolor('azure')
# count the occurences of each class
data = auto.groupby('Body Style')['Price'].sum()

# get x and y data
points = data.index
frequency = data.values
# create bar chart
ax.bar(points,frequency,color = 'royalblue')
# set title and labels
ax.set_title('Price of imported cars by the body style')
ax.set_xlabel('Body style')
ax.set_ylabel('Amount, $')
ax.set_facecolor('lightyellow')
plt.show()


# 3.3) bar charts at the same figure
fig, (ax1,ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))

# the first bar chart; count the occurences of each class/body style
data1 = auto['Body Style'].value_counts()
# get x and y data
points1 = data1.index
frequency1 = data1.values
# create bar chart
ax1.bar(points1,frequency1,color = 'forestgreen')
# set title and labels
ax1.set_title('Number of imported cars by body style')
ax1.set_xlabel('Body style')
ax1.set_ylabel('Number of imported cars')
ax1.set_facecolor('beige')

#  the second bar chart; count the occurences of each class/body style 
data2 = auto.groupby('Body Style')['Price'].sum()

# get x and y data
points2 = data2.index
frequency2 = data2.values
# create bar chart
ax2.bar(points2 , frequency2 , color = 'royalblue')
# set title and labels
ax2.set_title('Price of imported cars by the body style')
ax2.set_xlabel('Body style')
ax2.set_ylabel('Amount, $')
ax2.set_facecolor('lightyellow')

# fig.savefig('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Histograms_BodyStyle_NumOfCars_Price.png')
plt.show()



numbers = auto['Body Style'].value_counts()
print(numbers)
print()
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

"""