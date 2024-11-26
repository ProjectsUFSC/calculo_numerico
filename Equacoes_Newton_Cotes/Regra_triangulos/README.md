### `README.md`

# Método dos Retângulos

Este projeto implementa o método dos retângulos com ponto médio para aproximar numericamente a integral de uma função contínua \( f(x) \) em um intervalo \([a, b]\). O programa é interativo e exibe uma tabela detalhada com os cálculos intermediários.

## Funcionalidades

- **Entrada de Função:** O programa solicita ao usuário a entrada de \( f(x) \) em termos de `x`, como uma expressão Python válida.
- **Definição do Intervalo:** O usuário informa os limites do intervalo \([a, b]\) e o número de subdivisões (\( n \)).
- **Cálculo da Integral:** O programa aplica o método dos retângulos com ponto médio para calcular a integral aproximada.
- **Tabela de Resultados:** Exibe uma tabela detalhada com as seguintes informações:
  - \( h \): largura de cada subintervalo.
  - \( a' \): início de cada subintervalo.
  - \( b' \): fim de cada subintervalo.
  - \( x' \): ponto médio de cada subintervalo.
  - \( f(x') \): valor da função no ponto médio.
  - Área acumulada.
- **Personalização do Arredondamento:** O usuário pode especificar o número de casas decimais para os valores exibidos.

## Como Usar

1. **Entrada da Função:**
   - O programa solicita ao usuário que insira a função \( f(x) \) em termos de `x`, por exemplo:
     ```python
     x**2 + 2*x + 1
     ```

2. **Definição do Intervalo e Subdivisões:**
   - Informe os limites do intervalo \([a, b]\) e o número de subdivisões \( n \).

3. **Arredondamento dos Resultados:**
   - Escolha o número de casas decimais para exibição dos resultados.

4. **Execução do Método:**
   - O programa calcula a integral aproximada e exibe uma tabela com os passos do cálculo.

5. **Exibição dos Resultados:**
   - A solução aproximada é exibida após a tabela.

## Exemplo de Uso

```bash
python main.py
```

### Exemplo de Entrada
```plaintext
Digite a função f(x) em termos de 'x':  x / (1 + x**2)

Digite o limite inferior do intervalo (a): 0
Digite o limite superior do intervalo (b): 1
Digite o número de subdivisões (n): 10

Digite o número de casas decimais para o arredondamento: 4
```

### Exemplo de Saída
```plaintext
Tabela de Cálculo (Método dos Retângulos):
+------------+-----+------+------+------+---------+--------+
|   Iteração |   h |   a' |   b' |   x' |   f(x') |   área |
+============+=====+======+======+======+=========+========+
|          1 | 0.1 |  0   |  0.1 | 0.05 |  0.0499 | 0.0499 |
+------------+-----+------+------+------+---------+--------+
|          2 | 0.1 |  0.1 |  0.2 | 0.15 |  0.1467 | 0.1966 |
+------------+-----+------+------+------+---------+--------+
|          3 | 0.1 |  0.2 |  0.3 | 0.25 |  0.2353 | 0.4319 |
+------------+-----+------+------+------+---------+--------+
|          4 | 0.1 |  0.3 |  0.4 | 0.35 |  0.3118 | 0.7437 |
+------------+-----+------+------+------+---------+--------+
|          5 | 0.1 |  0.4 |  0.5 | 0.45 |  0.3742 | 1.1179 |
+------------+-----+------+------+------+---------+--------+
|          6 | 0.1 |  0.5 |  0.6 | 0.55 |  0.4223 | 1.5402 |
+------------+-----+------+------+------+---------+--------+
|          7 | 0.1 |  0.6 |  0.7 | 0.65 |  0.4569 | 1.9971 |
+------------+-----+------+------+------+---------+--------+
|          8 | 0.1 |  0.7 |  0.8 | 0.75 |  0.48   | 2.4771 |
+------------+-----+------+------+------+---------+--------+
|          9 | 0.1 |  0.8 |  0.9 | 0.85 |  0.4935 | 2.9706 |
+------------+-----+------+------+------+---------+--------+
|         10 | 0.1 |  0.9 |  1   | 0.95 |  0.4993 | 3.4699 |
+------------+-----+------+------+------+---------+--------+

Valor aproximado da integral: 0.3470
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando o comando:

```bash
pip install requirements.txt
```