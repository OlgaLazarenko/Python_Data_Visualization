README.md
# Auto Imports for 1985 year

The project uses the data available here: [1985 Auto Imports Database](https://archive.ics.uci.edu/ml/datasets/Automobile)
and also here [1985 Auto Imports Database](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/)

#### The dataset consists of the files:
- [imports-85.data](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/), actually the data
- [imports-85.names](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/), the description


### The purpose of the project:
Read the file containing the data about auto imports, perform data cleansing and validation and create visualizations using the Python library Matplotlib
#### Use Python pandas library:
- [x] Read the data from the csv file into a pandas DataFrame 
- [] Inspect a technical summary of the DataFrame: the columns( the data types:), null values, missing values
- [] Validate data, remove the rows with errors, the duplicate rows 
- [] Transform the data if it is necessary 
#### Use Matplotlib library to do the data visualizations:
- [x] Create scatter plots
- [] Create line plots
- [x] Create histograms
- [] Create bar charts
#### Answer the following questions:
- [] Top 3 most expensive car models
- [] Top 3 car models with highest mileage (city, highway)
- [] Find out that was the most popular body style of the imported cars (sedan,wagon, etc)
- [] Find out the risk factor of  the top 3 most popular imported cars ( the risk factor =-3, the car is risky; the risk factor=3, the car is safe)
- [] Determine what were the relative average loss (year insurance) for the top 3 popular vehicles at each category (2-doors,4-doors, etc)
