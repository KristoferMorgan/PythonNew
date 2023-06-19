# Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).






import pandas as pnd
data = pnd.read_csv('sample_data/california_housing_train.csv')
data[(data['population'] > 501)]['median_house_value'].mean()