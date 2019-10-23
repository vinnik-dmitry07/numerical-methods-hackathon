import csv
import numpy as np
from numpy.linalg import inv


def get_housing_data(rel_path):
    x_data_ = []
    y_data_ = []
    with open('data/housing-prices/' + rel_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            x_data_.append([row['OverallQual'], row['GrLivArea'], row['GarageCars'],
                            row['MSSubClass'], row['YrSold'], row['OverallCond']])
            y_data_.append(row['SalePrice'])
    return x_data_, y_data_


x_data, y_data = get_housing_data('simplified/train_cut.csv')

X = np.array(x_data, dtype=np.float64)
y = np.array(y_data, dtype=np.float64)

coef_values = inv(X.T.dot(X)).dot(X.T).dot(y)

x_data, y_data = get_housing_data('simplified/test_cut.csv')

X = np.array(x_data, dtype=np.float64)
y_theoretical = X.dot(coef_values)
y_experimental = np.array(y_data, dtype=np.float64)
print(np.mean(abs(y_experimental - y_theoretical) / y_theoretical))
