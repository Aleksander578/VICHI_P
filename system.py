import numpy as np

#модель верхульста https://ru.wikipedia.org/wiki/Логистическое_уравнение
def equations_1(t, y, r, K):#здесь t - время, у - популяция
    return np.array(
        [
            r*y[0]*( 1 - y[0]/K)
            ]
        )



#модель из воропаевой
def equations_2(t, y, a, b, c, d):#здесь t - время, у - жертвы (0) и хищники (1)
    return np.array(
        [
            a*y[0] - b*y[0]*y[1],
            -c*y[1] + d*y[0]*y[1]
            ]
        )


#модели с миграцией https://nplus1.ru/material/2019/12/04/lotka-volterra-model
#модель с константной миграцией
def equations_3_1(t, y, alfa=1, beta=1, gamma=1, delta=1, migrations_0=1, migrations_1=1):#здесь t - время, у - жертвы (0) и хищники (1)
    return np.array(
        [
            alfa*y[0] - beta*y[0]*y[1]+migrations_0,
            -gamma*y[1] + delta*y[0]*y[1]+migrations_1
            ]
        )

#модель с миграцией по отношению мигрирующих животных к общей массе вида
def equations_3_2(t, y, alfa=1, beta=1, gamma=1, delta=1, migrations_0=1, migrations_1=1):#здесь t - время, у - жертвы (0) и хищники (1)
    return np.array(
        [
            alfa*y[0] - beta*y[0]*y[1]+migrations_0/y[0],
            -gamma*y[1] + delta*y[0]*y[1]+migrations_1/y[1]
            ]
        )
