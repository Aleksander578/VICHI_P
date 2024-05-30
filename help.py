import numpy as np
import pandas as pd
import time

# Функция для оценки погрешности метода 
def estimate_error(method, equations, x0, xf, y0, h):
    x_1, y_1 = method( x0, xf, y0, equations, h)
    x_2, y_2 = method( x0, xf, y0, equations, h / 2)
    
    # Оценка погрешности как максимальная разница между решениями при различных шагах
    error = np.max(np.abs(y_1 - y_2[:, ::2]))
    return error

def estimate_errors_and_orders(methods, equations, x0, xf, y0, h, steps):
    all_data = {
        'Method': [],
        'Errors': [],
        'Orders': [],
        'Times': []
    }

    for method in methods:
        errors = []
        L_S = []
        times = []
        h_val = h
        for i in range(steps):
            start_time = time.time()
            error = estimate_error(method, equations, x0, xf, y0, h_val)
            end_time = time.time()
            method_time = end_time - start_time
            errors.append(error)
            L_S.append(h_val)
            times.append(method_time)
            h_val /= 2

        orders = [0]  # начальное значение для порядка точности
        for i in range(steps - 1):
            p1 = np.log2(errors[i] / errors[i + 1])
            orders.append(p1)
        
        all_data['Method'].append(method.__name__)
        all_data['Errors'].append(errors)
        all_data['Orders'].append(orders)
        all_data['Times'].append(times)
        

    return all_data



