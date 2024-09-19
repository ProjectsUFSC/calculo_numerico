# Resolvedor de Eliminação Gaussiana

Este projeto implementa o método de eliminação gaussiana para resolver sistemas de equações lineares. Inclui a exibição do progresso da solução e das matrizes intermediárias em forma de tabelas no terminal.

## Funcionalidades

- **gauss_elimination**: Resolve um sistema de equações lineares usando o método de eliminação gaussiana, com pivotamento para estabilidade numérica.
- **print_steps**: Exibe as matrizes intermediárias em cada passo do processo de eliminação, permitindo uma visualização do progresso.

## Como Usar

1. **Entrada da Matriz e Vetor**:
   - O programa solicita ao usuário que insira os coeficientes da matriz `A` e do vetor `b` para o sistema de equações `Ax = b`.

2. **Exibição dos Passos Intermediários**:
   - O programa gera e exibe as matrizes em cada passo do processo de eliminação gaussiana para uma melhor compreensão do progresso da solução.

3. **Execução da Eliminação Gaussiana**:
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
Equação 1 (separar coeficientes por espaço): 0.25 0.5 1
Equação 2 (separar coeficientes por espaço): 0.09 0.3 1
Equação 3 (separar coeficientes por espaço): 0.01 0.1 1

Digite os coeficientes do vetor b:
b (separar coeficientes por espaço): 0.25 0.49 0.81



```

### Exemplo de Saída
```plaintext
Matriz no Passo 1:
+------+------+------+------+
| 0.25 | 0.5  | 1    | 0.25 |
+------+------+------+------+
| 0    | 0.12 | 0.64 | 0.4  |
+------+------+------+------+
| 0    | 0.08 | 0.96 | 0.8  |
+------+------+------+------+

Matriz no Passo 2:
+------+------+--------+--------+
| 0.25 | 0.5  | 1      | 0.25   |
+------+------+--------+--------+
| 0    | 0.12 | 0.64   | 0.4    |
+------+------+--------+--------+
| 0    | 0    | 0.5333 | 0.5333 |
+------+------+--------+--------+

Matriz no Passo 3:
+------+------+--------+--------+
| 0.25 | 0.5  | 1      | 0.25   |
+------+------+--------+--------+
| 0    | 0.12 | 0.64   | 0.4    |
+------+------+--------+--------+
| 0    | 0    | 0.5333 | 0.5333 |
+------+------+--------+--------+

Solução aproximada:
x1 = 1.000000
x2 = -2.000000
x3 = 1.000000
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
