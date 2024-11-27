# Implementação da Regra de Simpson

Este projeto implementa a **Regra de Simpson** para aproximar numericamente o valor de integrais definidas de uma função \( f(x) \) no intervalo \([a, b]\).

## Funcionalidades

- **Regra de Simpson**:
  - Aproxima a integral definida de \( f(x) \) utilizando a Regra de Simpson.
  - O método exige um número **par** de subdivisões para funcionar corretamente.
- **Tabela de Resultados**:
  - Mostra os cálculos intermediários, incluindo os valores dos pontos \( x \), \( f(x) \), os pesos usados na fórmula e os termos somados à integral.
- **Configuração de Precisão**:
  - Permite especificar o número de casas decimais para arredondar os resultados.

## Como Usar

1. **Entrada da Função**:
   - O programa solicita que você insira a função \( f(x) \) como uma expressão Python válida.
   - Exemplo: Para \( f(x) = e^x \), digite `np.exp(x)`.

2. **Entrada dos Limites de Integração**:
   - Digite os valores de \( a \) (limite inferior) e \( b \) (limite superior) do intervalo.

3. **Número de Subdivisões**:
   - Insira o número de subdivisões \( n \). **Atenção: \( n \) deve ser um número par.**

4. **Casas Decimais**:
   - Insira o número de casas decimais desejado para arredondar os valores da tabela e do resultado final.

5. **Resultados**:
   - O programa exibe uma tabela detalhada com as seguintes colunas:
     - **Iteração**: Índice do ponto avaliado.
     - **x**: Ponto no intervalo.
     - **f(x)**: Valor da função no ponto \( x \).
     - **Peso**: Peso atribuído ao ponto (1, 2 ou 4).
     - **Termo**: Valor ponderado a ser somado à integral.
   - Exibe o valor aproximado da integral.

## Exemplo de Uso

### Entrada
```plaintext
Digite a função f(x) em termos de 'x': np.exp(x)

Digite o limite inferior do intervalo (a): 0
Digite o limite superior do intervalo (b): 1
Digite o número de subdivisões (n): 10

Digite o número de casas decimais para o arredondamento: 4
```

### Saída
```plaintext
Tabela de Cálculo (Regra de Simpson):
+------------+-----+--------+-----+----------+------------+
|   Iteração |   x |   f(x) |   c |   c*f(x) |   Integral |
+============+=====+========+=====+==========+============+
|          0 | 0   | 1      |   1 |   1      |     1      |
+------------+-----+--------+-----+----------+------------+
|          1 | 0.1 | 1.1052 |   4 |   4.4207 |     5.4207 |
+------------+-----+--------+-----+----------+------------+
|          2 | 0.2 | 1.2214 |   2 |   2.4428 |     7.8635 |
+------------+-----+--------+-----+----------+------------+
|          3 | 0.3 | 1.3499 |   4 |   5.3994 |    13.2629 |
+------------+-----+--------+-----+----------+------------+
|          4 | 0.4 | 1.4918 |   2 |   2.9836 |    16.2466 |
+------------+-----+--------+-----+----------+------------+
|          5 | 0.5 | 1.6487 |   4 |   6.5949 |    22.8415 |
+------------+-----+--------+-----+----------+------------+
|          6 | 0.6 | 1.8221 |   2 |   3.6442 |    26.4857 |
+------------+-----+--------+-----+----------+------------+
|          7 | 0.7 | 2.0138 |   4 |   8.055  |    34.5407 |
+------------+-----+--------+-----+----------+------------+
|          8 | 0.8 | 2.2255 |   2 |   4.4511 |    38.9918 |
+------------+-----+--------+-----+----------+------------+
|          9 | 0.9 | 2.4596 |   4 |   9.8384 |    48.8302 |
+------------+-----+--------+-----+----------+------------+
|         10 | 1   | 2.7183 |   1 |   2.7183 |    51.5485 |
+------------+-----+--------+-----+----------+------------+

Valor aproximado da integral: 1.7183
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install requirements.txt
```
