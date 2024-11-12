import numpy as np
import sympy as sp
from tabulate import tabulate

def parse_function(expr, variables):
    """Converte uma expressão de string em uma função lambda para avaliação."""
    return sp.lambdify(variables, sp.sympify(expr), 'numpy')

def newton_method(F_funcs, J_funcs, x0, tol=1e-5, max_iterations=100):
    x = np.array(x0, dtype=float)
    Fx = np.array([f(*x) for f in F_funcs])
    Er = tol + 1  
    steps = []  
    
    for k in range(max_iterations):
        if np.linalg.norm(Fx, ord=np.inf) <= tol or Er <= tol:
            break
        
        Jx = np.array([[j(*x) for j in row] for row in J_funcs], dtype=float)
        
        try:
            s = np.linalg.solve(Jx, -Fx)
        except np.linalg.LinAlgError:
            raise ValueError("A matriz Jacobiana é singular e não é invertível.")
        
        x_new = x + s
        Er = np.linalg.norm(s, ord=np.inf)
        
        step_info = np.hstack([np.copy(x_new), [Er]])
        steps.append(step_info)
        
        x = x_new
        Fx = np.array([f(*x) for f in F_funcs])

    return x, steps

def print_steps(steps):
    headers = [f"x{i+1}" for i in range(len(steps[0]) - 1)] + ["Er"]
    table = [np.round(step, 6) for step in steps]
    print("\nTabela de Soluções e Erros por Iteração:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

num_vars = int(input("Digite o número de variáveis do sistema: "))
variables = sp.symbols(f"x1:{num_vars+1}")

F_funcs = []
for i in range(num_vars):
    expr = input(f"Digite a expressão para f{i+1}(x1, ..., x{num_vars}): ")
    F_funcs.append(parse_function(expr, variables))

J_funcs = []
for i in range(num_vars):
    row = []
    for j in range(num_vars):
        d_expr = input(f"Digite a derivada ∂f{i+1}/∂x{j+1}: ")
        row.append(parse_function(d_expr, variables))
    J_funcs.append(row)

x0 = list(map(float, input(f"Digite a aproximação inicial para x (x1, ..., x{num_vars}): ").split()))

tol = input("\nDeseja utilizar uma tolerância diferente de 1e-5? (s/n): ")
tol = float(input("\nDigite a tolerância desejada: ")) if tol.lower() == 's' else 1e-5

max_iter = input("\nDeseja utilizar um número máximo de iterações diferente de 100? (s/n): ")
max_iter = int(input("\nDigite o número máximo de iterações desejado: ")) if max_iter.lower() == 's' else 100

try:
    x_sol, steps = newton_method(F_funcs, J_funcs, x0, tol, max_iter)
    
    print_steps(steps)
    
    print("\nSolução aproximada final:")
    for i, xi in enumerate(x_sol):
        print(f"x{i+1} = {xi:.6f}")

except Exception as e:
    print(f"Erro: {e}")
