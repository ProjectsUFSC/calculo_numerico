# Resolvedor de Decomposição LU

Este projeto implementa o método da Decomposição LU para resolver sistemas de equações lineares. Inclui a exibição do progresso da solução e das matrizes intermediárias em forma de tabelas no terminal.

## Funcionalidades

- **LU_decomposition**: Resolve um sistema de equações lineares usando o método da Decomposição LU, com pivotamento para estabilidade numérica.
- **print_steps**: Exibe as matrizes intermediárias em cada passo do processo de eliminação, permitindo uma visualização do progresso.

## Como Usar

1. **Entrada da Matriz e Vetor**:
   - O programa solicita ao usuário que insira os coeficientes da matriz `A` e do vetor `b`.

2. **Exibição dos Passos Intermediários**:
   - O programa gera e exibe as matrizes em cada passo do processo da Decomposição LU para uma melhor compreensão do progresso da solução.

3. **Execução da Decomposição LU**:
   - O programa resolve o sistema de equações e exibe os resultados em uma tabela formatada.

4. **Exibição dos Resultados**:
   - O programa exibe a solução final para o sistema e as matrizes intermediárias resultantes de cada passo da eliminação.

## Exemplo de Uso

```bash
python main.py
```

### Exemplo de Entrada
```plaintext
Digite o número de equações: 3

Digite os coeficientes da matriz A:
Equação 1 (separar coeficientes por espaço): 3 2 4
Equação 2 (separar coeficientes por espaço): 1 1 2
Equação 3 (separar coeficientes por espaço): 4 3 2

Digite os coeficientes do vetor b:
b (separar coeficientes por espaço): 1 2 3



```

### Exemplo de Saída
```plaintext
Matriz inicial aumentada [A|b]:
+---+---+---+---+
| 3 | 2 | 4 | 1 |
+---+---+---+---+
| 1 | 1 | 2 | 2 |
+---+---+---+---+
| 4 | 3 | 2 | 3 |
+---+---+---+---+

Matriz L no Passo 1:
+--------+---+---+
| 1      | 0 | 0 |
+--------+---+---+
| 0.3333 | 0 | 0 |
+--------+---+---+
| 1.3333 | 0 | 0 |
+--------+---+---+


Matriz U no Passo 1:
+---+----------+-----------+
| 3 | 2        |  4        |
+---+----------+-----------+
| 0 | 0.333333 |  0.666667 |
+---+----------+-----------+
| 0 | 0.333333 | -3.33333  |
+---+----------+-----------+

Matriz L no Passo 2:
+--------+---+---+
| 1      | 0 | 0 |
+--------+---+---+
| 0.3333 | 1 | 0 |
+--------+---+---+
| 1.3333 | 1 | 0 |
+--------+---+---+


Matriz U no Passo 2:
+---+-------------+-----------+
| 3 | 2           |  4        |
+---+-------------+-----------+
| 0 | 0.333333    |  0.666667 |
+---+-------------+-----------+
| 0 | 5.55112e-17 | -4        |
+---+-------------+-----------+

Matriz L no Passo 3:
+--------+---+---+
| 1      | 0 | 0 |
+--------+---+---+
| 0.3333 | 1 | 0 |
+--------+---+---+
| 1.3333 | 1 | 1 |
+--------+---+---+


Matriz U no Passo 3:
+---+-------------+-----------+
| 3 | 2           |  4        |
+---+-------------+-----------+
| 0 | 0.333333    |  0.666667 |
+---+-------------+-----------+
| 0 | 5.55112e-17 | -4        |
+---+-------------+-----------+

Solução Y:
y1 = 1.000000
y2 = 1.666667
y3 = -0.000000

Solução aproximada:
x1 = -3.000000
x2 = 5.000000
x3 = 0.000000
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
