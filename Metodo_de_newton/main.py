import numpy as np
from tabulate import tabulate

def find_interval(f, start=-100, end=100, step=1):
    x1 = start
    x2 = start + step
    f_x1 = f(x1)
    
    while x2 <= end:
        f_x2 = f(x2)
        if f_x1 * f_x2 < 0:
            return x1, x2
        x1, f_x1 = x2, f_x2
        x2 += step
    
    raise ValueError("\nNão foi encontrado um intervalo com mudança de sinal dentro do intervalo {-100, 100}")


def find_initial_value(f, ddf, x1, x2):
    if ddf(x1) * f(x1) > 0:
        return x1
    elif ddf(x2) * f(x2) > 0:
        return x2
    else:
        raise ValueError("\nNão foi encontrado um valor inicial")


def newton_method(f, df, x0, tol, max_iter):
    steps = []
    
    for iter_count in range(1, max_iter + 1):
        f_x0 = f(x0)
        df_x0 = df(x0)
        if df_x0 == 0:
            raise ValueError(f"A derivada é zero em x = {x0}. Método falhou.")
        
        x1 = x0 - (f_x0 / df_x0)
        err = abs(x1 - x0)
        
        steps.append((iter_count, x0, f_x0, df_x0, x1, err))
        
        if err <= tol:
            break
        
        x0 = x1
    
    return steps

def plot_ascii(f, start=-30, end=30, width=60, height=10):
    x_values = np.linspace(start, end, width)
    y_values = np.array([f(x) for x in x_values])
    
    min_y, max_y = y_values.min(), y_values.max()
    y_range = max_y - min_y
    
    y_scaled = np.floor((y_values - min_y) / y_range * (height - 1)).astype(int)
    
    canvas = np.full((height, width), ' ', dtype=str)
    
    for i in range(width):
        y_pos = height - 1 - y_scaled[i]
        if 0 <= y_pos < height:
            canvas[y_pos, i] = '*'
    
    canvas_str = '\n'.join([''.join(row) for row in canvas])
    
    print(f"\nGráfico ASCII de f(x) no intervalo [{start}, {end}]:\n")
    print(canvas_str)

# Entrada da função e da derivada
expression = input("\nDigite a função f(x) em termos de 'x': ")
derivative_expression = input("\nDigite a derivada df(x) em termos de 'x': ")
second_derivative_expression = input("\nDigite a segunda derivada d²f(x) em termos de 'x': ")
f = lambda x: eval(expression)
df = lambda x: eval(derivative_expression)
ddf = lambda x: eval(second_derivative_expression)

plot_ascii(f)

tol = input("\nDeseja utilizar uma tolerância diferente de 1e-5? (s/n): ")
tol = float(input("\nDigite a tolerância desejada: ")) if tol == 's' else 1e-5

max_iter = input("\nDeseja utilizar um número máximo de iterações diferente de 100? (s/n): ")
max_iter = int(input("\nDigite o número máximo de iterações desejado: ")) if max_iter == 's' else 100

try:
    x1 , x2= find_interval(f)
    x0 = find_initial_value(f, ddf, x1, x2)
    print(f"\nValor inicial encontrado automaticamente: x0 = {x0:.2f}")
    
    steps = newton_method(f, df, x0, tol, max_iter)
    
    headers = ["Iteração", f"xn", "f(xn)", "df(xn)", "x(n+1)", "Erro"]
    table = [[step[0], f"{step[1]:.6f}", f"{step[2]:.6f}", f"{step[3]:.6f}", f"{step[4]:.6f}", f"{step[5]:.6f}"] for step in steps]

    print("\nTabela de Passos do Método de Newton:")
    print(tabulate(table, headers, tablefmt="grid"))

    print(f"\nA solução aproximada é: {steps[-1][4]:.6f}\n")

except ValueError as e:
    print(f"Erro: {e}")
