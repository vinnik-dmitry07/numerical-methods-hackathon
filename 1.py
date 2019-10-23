import csv
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, log, E, lambdify, Matrix

x, c1, c2, c3, c4, c5, c6, k1, k2 = vars_ = symbols('x, c1:7, k1:3')
coef = vars_[1:]

f = c1 * x + c2 * x ** 2 + c3 * cos(k1 * x) + c4 * sin(k2 * x) + c5 * E ** x + c6 * log(x)

x_data = []
y_data = []
with open('data/guess-koeffs/data-3.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        x_data.append(row['x'])
        y_data.append(row['y'])

x_data = np.array(x_data, dtype=np.float64)
y_data = np.array(y_data, dtype=np.float64)

r = []
for x_i, y_i in zip(x_data, y_data):
    r.append(y_i - f.subs(x, x_i))
r = Matrix(r)

J = r.jacobian(coef)

plt.plot(x_data, y_data, 'b-', label='data')

c = Matrix(np.ones(len(coef)))
for _ in range(10):
    sub = list(zip(coef, c))
    J_ = J.subs(sub)
    r_ = r.subs(sub)
    c = c - ((J_.T * J_).inv() * J_.T * r_)

c = np.array(c).astype(np.float64)[:, 0]

plt.plot(x_data, lambdify(vars_, f)(x_data, *c), 'r-',
         label='fit: c1={:5.3f}, c2={:5.3f}, c3={:5.3f}, c4={:5.3f}, c5={:5.3f}, c6={:5.3f}, k1={:5.3f}, k2={:5.3f}'.
         format(*c))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
