import plotly.graph_objects as go

# def plot_solution(x, y, r, K,a, b, c, d, m1, m2, names=None):
#     fig = go.Figure()

#     if names is None:
#         names = [f'Вид {i+1}' for i in range(len(y))]

#     for i in range(len(y)):
#         fig.add_trace(go.Scatter(x=x, y=y[i], mode='lines', name=names[i]))

#     fig.update_layout(title='Графики Y(x)',
#                        xaxis_title='x',
#                        yaxis_title='y')
#     fig.show()

#     import plotly.graph_objects as go

def plot_solution(x, y, r=None, K=None, a=None, b=None, c=None, d=None, m1=None, m2=None, names=None):
    fig = go.Figure()

    if names is None:
        names = [f'Вид {i+1}' for i in range(len(y))]

    for i in range(len(y)):
        fig.add_trace(go.Scatter(x=x, y=y[i], mode='lines', name=names[i]))

    # Определяем порядок параметров
    params = {
        'r': r,
        'K': K,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'm1': m1,
        'm2': m2
    }

    # Формируем заголовок с учетом порядка параметров
    title_params = [f'{key}={value}' for key, value in params.items() if value is not None]
    title = 'Графики Y(x)'
    if title_params:
        title += ' (' + ', '.join(title_params) + ')'

    fig.update_layout(title=title,
                      xaxis_title='x',
                      yaxis_title='y')
    fig.show()



def plot_solution_for_sp_points(y):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=y[0], y=y[1], mode='lines'))

    fig.update_layout(title='Графики Y(x)',
                        xaxis_title='y1',
                        yaxis_title='y2 ')
    fig.show()


def plot_methods_solutions(methods, names, x0, xf, y0, f, h):
    fig = go.Figure()

    for i, method in enumerate(methods):
        x, y = method(x0, xf, y0, f, h)
        for j in range(len(y0)):
            fig.add_trace(go.Scatter(x=x, y=y[j], mode='lines', name=f'{names[i]} - Вид {j+1}'))

    fig.update_layout(title='Графики Y(x) для различных методов',
                      xaxis_title='x',
                      yaxis_title='y')
    fig.show()


