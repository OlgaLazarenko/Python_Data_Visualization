# Data_Visualizatioin_Matplotlib
#!/bin/python3

# import Matplotlib library
import matplotlib.pyplot as plt
import pandas as pd
import pandas_schema

from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation,
                                    CanConvertValidation, MatchesPatternValidation,
                                    InRangeValidation, InListValidation



schema = Schema ([
    Column('Symboling', [InRangeValidation(-3,3)] ) #integer from -3 to 3
    Column('Normalized Loss', [InRangeValidation(65,256)] )  # integer from 65 to 256
    Column('Make',[LeadingWhitespaceValidation(), TrailingWhitespaceValidation()] )  # text
    Column('Fuel Type', [InListValidation(['diesel', 'gas'])]), # diesel, gas
    Column('Aspiration'), # text
    Column('Num of Doors' , [InListValidation(['two', 'four'])]), # text (two, four)
    Column('Body Style' , [InListValidation(['hardtop', 'wagon','sedan','hatchback', 'convertible'])] ), 
    # text: hardtop, wagon, sedan, hatchback, convertible
    Column('Drive Wheels' , [InListValidation(['4wd', 'fwd' , 'rwd'])]), # text: 4wd, fwd, rwd
    Column('Engine Location' , [InListValidation(['front', 'rear'])]), # text: front, rear
    Column('Wheel Base' , [InRangeValidation([86.6,120.9])] ) # decimal from 86.6 to 120.9
    Column('Length' , [InRangeValidation(65,256)] )  # decimal from 141.1 to 208.1
    Column('Width' , [InRangeValidation(60.3,72.3)] ) # decimal from 60.3 to 72.3
    Column('Height' , [InRangeValidation(47.8,59.8)] )   # decimal from 47.8 to 59.8
    Column('Curb Weight' , [InRangeValidation(1488,4066)] )   # integer from 1488 to 4066
    Column('Num of Cylinders' , [InListValidation(['two','four','three','five','six','eight','twelve'])]), # text: eight, five, four, six, three, twelve, two
    Column('Engine Size' , [InRangeValidation(61,326)) # integer from 61 to 326
    Column('Fuel System' , [InListValidation(['1bbl', '2bbl', '4bbl', 'idi','mfi','mpfi','spdi','spfi']')]), #string: 1bbl, 2bbl, 4bbl, idi,mfi,mpfi,spdi,spfi
    Column('Bore' , [InRangeValidation(2.54,3.94)] )  # decimal from 2.54 to 3.94
    Column('Stroke' [InRangeValidation(2.07,4.17)] ) #decimal from 2.07 to 4.17
    Column('Compression Ratio' , [InRangeValidation(7,23)] ), #  integer: from 7 to 23
    Column('Horsepower' , [InRangeValidation(48,288)] ),  # integer:from 48 to 288
    Column('Peak rmp'), [InRangeValidation(4150,6600)]  # integer: from 4150 to 6600
    Column('City mpg'), [InRangeValidation(13,49)]  #integer: from 13 to 49
    Column('Highway mpg'), [InRangeValidation(16,54)]  # integer: 16 to 54
    Column('Price')  [InRangeValidation(5118,45400)]  # integer from 5118 to 45400


])

# work with the data file 'Auto_Import_1985.csv'

# Data Validation
# define the checking methonds
'''
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
null_validation = [CustomerElementValidation(lambda d: d is not  np.nan, 'this field cannot be null']

# define a validation schema
#define what rules will be applied for each of the columns to be read from the file
schema = pandas_schema.Schema([
    Column('Symboling'), integer_validation  #integer from -3 to 3
    Column('Normalized Loss'), integer_validation   # integer from 65 to 256
    Column('Make'), # text
    Column('Fuel Type'), # diesel, gas
    Column('Aspiration'), # text
    Column('Num of Doors'), # text (two, four)
    Column('Body Style'), # text: hardtop, wagon, sedan, hatchback, convertible
    Column('Drive Wheels'), # text: 4wd, fwd, rwd
    Column('Engine Location'), # text: front, rear
    Column('Wheel Base'), decimal_validation  # decimal from 86.6 to 120.9
    Column('Length'),  decimal_validation   # decimal from 141.1 to 208.1
    Column('Width'), decimal_validation  # decimal from 60.3 to 72.3
    Column('Height'), decimal_validation   # decimal from 47.8 to 59.8
    Column('Curb Weight'), integer_validation   # integer from 1488 to 4066
    Column('Num of Cylinders'), # text: eight, five, four, six, three, twelve, two
    Column('Engine Size'),  integer_validation # integer from 61 to 326
    Column('Fuel System'), #string: 1bbl, 2bbl, 4bbl, idi,mfi,mpfi,spdi,spfi
    Column('Bore'),decimal_validation  # decimal from 2.54 to 3.94
    Column('Stroke'), decimal_validation #decimal from 2.07 to 4.17
    Column('Compression Ratio'), integer_validation #  integer: from 7 to 23
    Column('Horsepower'), integer_validation  # integer:from 48 to 288
    Column('Peak rmp'), integer_validation  # integer: from 4150 to 6600
    Column('City mpg'), integer_validation  #integer: from 13 to 49
    Column('Highway mpg'), integer_validation  # integer: 16 to 54
    Column('Price')  integer_validation  # integer from 5118 to 45400
])
'''

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
'''
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

'''
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
ax.legend()

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
ax.legend()

plt.show()


'''
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
print(avg_city_mpg)
'''

