import numpy as np
from tabulate import tabulate

def LU_decomposition(A, b):
    n = len(b)
    L_steps = []
    U_steps = []
    
    L = np.zeros((n, n))
    U = np.copy(A)
    
    for i in range(n):
        L[i, i] = 1
        for j in range(i + 1, n):
            if U[i,i] == 0:
                for k in range(i + 1, n):
                    if U[k, i] != 0:
                        U[[i, k]] = U[[k, i]]
                        L[[i, k]] = L[[k, i]]
                        break
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
        
        L_steps.append(np.copy(L))
        U_steps.append(np.copy(U))

    y = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x, y, L_steps, U_steps

def print_steps(L_steps, U_steps):
    L_headers = [f"Passo {i+1}" for i in range(len(L_steps))]
    L_tables = [np.round(step, 4) for step in L_steps]
    
    for i, table in enumerate(L_tables):
        print(f"\nMatriz L no Passo {i+1}:")
        print(tabulate(table, tablefmt="grid"))
        print("\n")
        print(f"Matriz U no Passo {i+1}:")
        print(tabulate(U_steps[i], tablefmt="grid"))
    

n = int(input("Digite o número de equações: "))
A = np.zeros((n, n))
b = np.zeros(n)


print("\nDigite os coeficientes da matriz A:")
for i in range(n):
    A[i] = list(map(float, input(f"Equação {i+1} (separar coeficientes por espaço): ").split()))

print("\nDigite os coeficientes do vetor b:")
b = np.array(list(map(float, input("b (separar coeficientes por espaço): ").split())))

Ab = np.hstack([A, b.reshape(-1, 1)])
print("\nMatriz inicial aumentada [A|b]:")
print(tabulate(np.round(Ab, 4), tablefmt="grid"))

try:

    x, y, L_steps, U_steps = LU_decomposition(A, b)
    
    print_steps(L_steps, U_steps)

    print("\nSolução Y:")
    for i, yi in enumerate(y):
        print(f"y{i+1} = {yi:.6f}")
    
    print("\nSolução aproximada:")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi:.6f}")

    

except Exception as e:
    print(f"Erro: {e}")
