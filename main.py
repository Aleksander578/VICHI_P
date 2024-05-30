import numpy as np
import plotly.graph_objects as go
import time
from method import *
from system import *
from graph import *
from help import *


# #ВЫБОР МЕТОДА
# a = 0.3
# b = 0.28
# c = 0.7
# d = 0.2
# x0 = 0
# xf = 100
# y0 = [5 , 1.5]
# h = 0.01
# steps = 10

# methods = [Runge_Kutty_4, Euler, recountable_Euler, Adams_Bashforth, Adams_Bashforth_Moulton, Gir_4, Gir_4_iters]
# names = ['Runge-Kutta 4', 'Euler', 'Recountable Euler', 'Adams-Bashforth', 'Adams-Bashforth-Moulton', 'Gir 4', 'Gir 4 with iterations']

# #ГРАФИК
# plot_methods_solutions(methods, names, x0, xf, y0, lambda t, y: equations_2(t, y, a, b, c, d), h)

# #ПОРЯДКИ, ОШИБКИ, ВРЕМЯ
# x0 = 0
# xf = 5
# y0 = [5 , 1.5]
# h = 1
# steps = 10

# all_data = estimate_errors_and_orders(methods, lambda t, y: equations_2(t, y, a, b, c, d), x0, xf, y0, h, steps)

# df = pd.DataFrame(all_data)

# print(df)

# # Сохранение DataFrame в файл CSV
# df.to_csv('table1.csv', index=False)  # Имя файла можно выбрать любое


# a = 0.6
# b = 1
# c = 0.63
# d = 0.3
# x0 = 0
# xf = 100
# y0 = [ 20 , 5 ]
# h = 0.01
# steps = 10

# methods = [Runge_Kutty_4, Euler, recountable_Euler, Adams_Bashforth, Adams_Bashforth_Moulton, Gir_4, Gir_4_iters]
# names = ['Runge-Kutta 4', 'Euler', 'Recountable Euler', 'Adams-Bashforth', 'Adams-Bashforth-Moulton', 'Gir 4', 'Gir 4 with iterations']

# #ГРАФИК
# plot_methods_solutions(methods, names, x0, xf, y0, lambda t, y: equations_2(t, y, a, b, c, d), h)

# #ПОРЯДКИ, ОШИБКИ, ВРЕМЯ
# x0 = 0
# xf = 5
# y0 = [5 , 1.5]
# h = 1
# steps = 10

# all_data = estimate_errors_and_orders(methods, lambda t, y: equations_2(t, y, a, b, c, d), x0, xf, y0, h, steps)

# df = pd.DataFrame(all_data)

# print(df)

# # Сохранение DataFrame в файл CSV
# df.to_csv('table2.csv', index=False)  # Имя файла можно выбрать любое


# a = 0.7
# b = 0.03
# c = 1
# d = 0.15
# x0 = 0
# xf = 100
# y0 = [ 5 , 22 ]
# h = 0.01
# steps = 10

# methods = [Runge_Kutty_4, Euler, recountable_Euler, Adams_Bashforth, Adams_Bashforth_Moulton, Gir_4, Gir_4_iters]
# names = ['Runge-Kutta 4', 'Euler', 'Recountable Euler', 'Adams-Bashforth', 'Adams-Bashforth-Moulton', 'Gir 4', 'Gir 4 with iterations']

# #ГРАФИК
# plot_methods_solutions(methods, names, x0, xf, y0, lambda t, y: equations_2(t, y, a, b, c, d), h)

# #ПОРЯДКИ, ОШИБКИ, ВРЕМЯ
# x0 = 0
# xf = 5
# y0 = [5 , 1.5]
# h = 1
# steps = 10

# all_data = estimate_errors_and_orders(methods, lambda t, y: equations_2(t, y, a, b, c, d), x0, xf, y0, h, steps)

# df = pd.DataFrame(all_data)

# print(df)

# # Сохранение DataFrame в файл CSV
# df.to_csv('table3.csv', index=False)  # Имя файла можно выбрать любое


#ВОРОПАЕВА
# Начальные условия
x0 = 0
xf = 100
y0 = [3 , 5]
y0_1 = [0.1]
h = 0.01

# Расчет методом Рунге-Кутты
y0_1 = [3]
r = 1
K = 6
x1, y1 = Runge_Kutty_4(x0, xf, y0_1, lambda t, y: equations_1(t, y, r, K), h)
plot_solution(x1, y1, r, K)

y0_1 = [6]
r = 4
K = 2
x1, y1 = Runge_Kutty_4(x0, xf, y0_1, lambda t, y: equations_1(t, y, r, K), h)
plot_solution(x1, y1, r, K)

a = 0.3
b = 0.28
c = 0.7
d = 0.2
y0 = [5 , 1.5]
x2, y2 = Runge_Kutty_4(x0, xf, y0, lambda t, y: equations_2(t, y, a, b, c, d), h)
plot_solution(x2, y2, a, b, c, d)
plot_solution_for_sp_points(y2)

a = 0.3
b = 0.28
c = 0.7
d = 0.2
y0 = [50 , 20]
x2, y2 = Runge_Kutty_4(x0, xf, y0, lambda t, y: equations_2(t, y, a, b, c, d), h)
plot_solution(x2, y2, a, b, c, d)
plot_solution_for_sp_points(y2)

a = 0.4
b = 0.1
c = 0.8
d = 0.25
m1 = 0.45
m2 = 0
y0 = [10 , 16]
x3, y3 = Runge_Kutty_4(x0, xf, y0, lambda t, y: equations_3_2(t, y, a, b, c, d ,m1 ,m2), h)
plot_solution(x3, y3, a, b, c, d, m1, m2)
plot_solution_for_sp_points(y3)

a = 0.4
b = 0.14
c = 0.07
d = 0
m1 = 0.48
m2 = 0.8
y0 = [3 , 5]
x3, y3 = Runge_Kutty_4(x0, xf, y0, lambda t, y: equations_3_2(t, y, a, b, c, d ,m1 ,m2), h)
plot_solution(x3, y3, a, b, c, d, m1, m2)
plot_solution_for_sp_points(y3)










