import pandas

# Get a dataframe
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get a series
color = data['Primary Fur Color']

# Using method--> series.count()
gray_squirrels = color[color == "Gray"].count()
cinnamon_squirrels = color[color == "Cinnamon"].count()
black_squirrels = color[color == "Black"].count()

# Create a dataframe from scratch
data_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [gray_squirrels, cinnamon_squirrels, black_squirrels],
}

convert = pandas.DataFrame(data_dict)

# Create a new file.
convert.to_csv("result.csv")