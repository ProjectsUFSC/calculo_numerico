# Resolvedor de Sistema Linear com Método de Jacobi

Este projeto implementa o método iterativo de Jacobi para resolver sistemas de equações lineares. Ele exibe as soluções intermediárias e os erros em cada iteração, permitindo acompanhar o processo de convergência.

## Funcionalidades

- **`jacobi_method`**: Implementa o método de Jacobi para resolver um sistema de equações lineares do tipo `Ax = b`.
- **`print_steps`**: Exibe os valores das variáveis e os erros a cada iteração em uma tabela formatada no terminal.

## Como Usar

1. **Entrada da Matriz e Vetor**:
   - O programa solicita que o usuário insira os coeficientes da matriz `A` e do vetor `b` do sistema de equações lineares `Ax = b`.

2. **Configuração de Tolerância e Máximo de Iterações**:
   - O usuário pode definir uma tolerância diferente da padrão (1e-5) e um número máximo de iterações (padrão: 100).

3. **Execução do Método de Jacobi**:
   - O programa resolve o sistema iterativamente, exibindo os valores das variáveis e os erros em cada iteração até que o critério de convergência seja atendido.

4. **Exibição dos Resultados**:
   - Após a convergência, o programa exibe a solução final do sistema, o vetor original `b` e o vetor `b'` calculado com base na solução aproximada.

## Exemplo de Uso

```bash
python main.py
```

### Exemplo de Entrada
```plaintext
Digite o número de equações: 3

Digite os coeficientes da matriz A:
Equação 1 (separar coeficientes por espaço): 6 -1 1
Equação 2 (separar coeficientes por espaço): 1 8 -1
Equação 3 (separar coeficientes por espaço): 1 1 5

Digite os coeficientes do vetor b:
b (separar coeficientes por espaço): 7 16 18

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): s

Digite a tolerância desejada: 0.01

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Matriz inicial aumentada [A|b]:
+---+----+----+----+
| 6 | -1 |  1 |  7 |
+---+----+----+----+
| 1 |  8 | -1 | 16 |
+---+----+----+----+
| 1 |  1 |  5 | 18 |
+---+----+----+----+

Tabela de Soluções e Erros por Iteração:
+---------+---------+---------+----------+----------+----------+
|      x1 |      x2 |      x3 |   err_x1 |   err_x2 |   err_x3 |
+=========+=========+=========+==========+==========+==========+
| 1.16667 | 2       | 3.6     | 1.16667  | 2        | 3.6      |
+---------+---------+---------+----------+----------+----------+
| 0.9     | 2.30417 | 2.96667 | 0.266667 | 0.304167 | 0.633333 |
+---------+---------+---------+----------+----------+----------+
| 1.05625 | 2.25833 | 2.95917 | 0.15625  | 0.045833 | 0.0075   |
+---------+---------+---------+----------+----------+----------+
| 1.04986 | 2.23787 | 2.93708 | 0.006389 | 0.020469 | 0.022083 |
+---------+---------+---------+----------+----------+----------+
| 1.05013 | 2.2359  | 2.94245 | 0.000269 | 0.001962 | 0.005372 |
+---------+---------+---------+----------+----------+----------+

Solução aproximada final:
x1 = 1.049861
x2 = 2.237865
x3 = 2.937083

Vetor b (coeficientes):
+------+------+------+
|   b1 |   b2 |   b3 |
+======+======+======+
|    7 |   16 |   18 |
+------+------+------+

Vetor b' (calculado com base nos valores de x):
+---------+---------+---------+
|     b'1 |     b'2 |     b'3 |
+=========+=========+=========+
| 6.99839 | 16.0157 | 17.9731 |
+---------+---------+---------+
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- **numpy**: Biblioteca para cálculos matemáticos e manipulação de arrays.
- **tabulate**: Utilizada para exibir os resultados em forma de tabela.

### Instalação das dependências

Você pode instalar as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```
