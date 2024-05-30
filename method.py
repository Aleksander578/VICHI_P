import numpy as np


#Численные методы решения ДУ
def Runge_Kutty_4(x0, xf, y0, f, h):
    count = int((xf - x0) / h) + 1
    y = np.zeros((len(y0), count))
    y[:, 0] = y0
    x = np.arange(x0, xf + h, h)[:count]  # Ensure correct length including xf

    for i in range(1, count):
        k1 = h * f(x[i-1], y[:, i-1])
        k2 = h * f(x[i-1] + h/2, y[:, i-1] + k1/2)
        k3 = h * f(x[i-1] + h/2, y[:, i-1] + k2/2)
        k4 = h * f(x[i-1] + h, y[:, i-1] + k3)
        y[:, i] = y[:, i-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return x, y

def Euler(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1
    y = np.zeros((len(y0), count-1))
    y[:,0]=y0
    x = np.arange(x0, xf, h)

    for i in range (1, count-1):
        y[:,i] = y[:,i-1]+ h * f(x[i-1], y[:, i-1])

    return x, y

def recountable_Euler(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1
    y_correct = np.zeros((len(y0), count-1))
    y_correct[:, 0] = y0

    x = np.arange(x0, xf, h)

    for i in range (1, count-1):
        y_predict = y_correct[:,i-1] + h * f(x[i-1], y_correct[:, i-1])
        y_correct[:,i] = y_correct[:,i-1] + (h/2) * (f(x[i-1], y_correct[:, i-1]) + f(x[i], y_predict))

    return x, y_correct

def Adams_Bashforth(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1
    x, y_RK = Runge_Kutty_4(x0, xf, y0, f, h)
    y = np.zeros((len(y0), count-1))
    y[:,0]=y0
    y[:,1]=y_RK[:,1]
    y[:,2]=y_RK[:,2]
    y[:,3]=y_RK[:,3]

    v_func = [f(x[4], y[:, 4-1]), f(x[4-1], y[:, 4-2]), f(x[4-2], y[:, 4-3]), f(x[4-3], y[:, 4-4])]
    y[:, 4] = y[:, 4-1] + (h/24) * (55*v_func[0] - 59*v_func[1] + 37*v_func[2] - 9*v_func[3])
    for i in range (5, count-1):
        v_func.pop()
        v_func.insert(0, f(x[i], y[:, i-1]))
        y[:, i] = y[:, i-1] + (h/24) * (55*v_func[0] - 59*v_func[1] + 37*v_func[2] - 9*v_func[3])

    return x, y

def Adams_Bashforth_Moulton(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1

    x, y_RK = Runge_Kutty_4(x0, xf, y0, f, h)
    y = np.zeros((len(y0), count-1))
    y[:,0]=y0
    y[:,1]=y_RK[:,1]
    y[:,2]=y_RK[:,2]

    x, y_predict = Adams_Bashforth(x0, xf, y0, f, h)
    v_func = [f(x[3], y_predict[:, 3]), f(x[3-1], y[:, 3-1]), f(x[3-2], y[:, 3-2]), f(x[3-3], y[:, 3-3])]
    y[:, 3] = y[:, 3-1] + (h/24) * (9*v_func[0] + 19*v_func[1] - 5*v_func[2] + v_func[3])
    for i in range(4, count-1):
        v_func.pop()
        v_func.pop(0)
        v_func.insert(0, f(x[i-1], y[:, i-1]))
        v_func.insert(0, f(x[i], y_predict[:, i]))
        y[:, i] = y[:, i-1] + (h/24) * (9*v_func[0] + 19*v_func[1] - 5*v_func[2] + v_func[3])

    return x, y

def Gir_4(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1
    n=100

    x, y_RK = Runge_Kutty_4(x0, xf, y0, f, h/n)
    y = np.zeros((len(y0), count-1))
    y[:,0]=y0
    y[:,1]=y_RK[:,n]
    y[:,2]=y_RK[:,2*n]
    y[:,3]=y_RK[:,3*n]

    y_predict = y_RK

    for i in range(4, count-1):
        y[:, i] = (1/25) * (12*h*f(x[i*n], y_predict[:, i*n]) + 48*y[:, i-1] - 36*y[:, i-2] + 16*y[:, i-3] - 3*y[:, i-4])

    return x[::n], y

def Gir_4_iters(x0, xf, y0, f, h):
    count = int((xf- x0)/h) + 1

    n = 100
    x, y_RK = Runge_Kutty_4(x0, xf, y0, f, h/n)
    y = np.zeros((len(y0), count-1))
    y[:,0]=y0
    y[:,1]=y_RK[:,1*n]
    y[:,2]=y_RK[:,2*n]
    y[:,3]=y_RK[:,3*n]
    iters = np.zeros(count-1-4)

    for i in range(4, count-1):
        y_i_m1 = y[:, i-1]
        new_y = (1/25) * (12*h*f(x[(i-1)*n], y_i_m1) + 48*y[:, i-1] - 36*y[:, i-2] + 16*y[:, i-3] - 3*y[:, i-4])
        iter = 1
        while np.linalg.norm(np.subtract(new_y, y_i_m1))/np.linalg.norm(y_i_m1) > 1e-5:
            # ic(np.linalg.norm(np.subtract(new_y, y_i_m1))/np.linalg.norm(y_i_m1))
            y_i_m1 = new_y
            new_y = (1/25) * (12*h*f(x[i*n], new_y) + 48*y[:, i-1] - 36*y[:, i-2] + 16*y[:, i-3] - 3*y[:, i-4])
            iter += 1
        y[:,i] = new_y
        iters[i-4] = iter
    return x[::n], y 


                  
  