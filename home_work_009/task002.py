# Узнать какая максимальная households в зоне минимального значения population.



import pandas as pnd
data = pnd.read_csv('sample_data/california_housing_train.csv')
data[data['population'] == data['population'].min()]['households'].max()
