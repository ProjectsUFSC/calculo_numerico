# Regra do Trapézio

Este projeto implementa a **Regra do Trapézio** para aproximação numérica de integrais definidas. O programa solicita ao usuário uma função, os limites do intervalo de integração, o número de subdivisões, e o número de casas decimais para os resultados.

## Funcionalidades

- **Regra do Trapézio**: Calcula a área aproximada sob a curva de uma função \( f(x) \) usando a fórmula dos trapézios:
  \[
  \text{Área} = \frac{h}{2} \cdot \left(f(a') + f(b')\right)
  \]
  onde \( h = \frac{b - a}{n} \), sendo \( a \) e \( b \) os limites do intervalo e \( n \) o número de subdivisões.

- **Tabela Detalhada de Cálculo**: 
  - Mostra o tamanho do subintervalo \( h \), os valores de \( a' \), \( b' \), \( f(a') \), \( f(b') \), a área de cada trapézio, e a área acumulada.

- **Precisão Configurável**: Permite ao usuário escolher o número de casas decimais para exibir nos resultados.

## Como Usar

1. **Entrada da Função**: 
   - Digite a função \( f(x) \) como uma expressão válida em Python. Por exemplo, `x**2`, `np.sin(x)`, etc.
   - **Atenção:** A biblioteca `numpy` (`np`) está disponível para funções matemáticas.

2. **Defina o Intervalo**:
   - Insira os limites inferior (`a`) e superior (`b`) do intervalo de integração.

3. **Escolha o Número de Subdivisões**:
   - Insira o número de subdivisões \( n \) para o cálculo. Um valor maior de \( n \) resulta em maior precisão.

4. **Configuração de Casas Decimais**:
   - Especifique o número de casas decimais para arredondamento dos resultados.

5. **Resultados**:
   - O programa exibirá uma tabela com os detalhes de cada iteração, bem como o valor final aproximado da integral.

## Exemplo de Uso

### Execução do Programa
```bash
python main.py
```

### Exemplo de Entrada
```plaintext
Digite a função f(x) em termos de 'x': 1/x

Digite o limite inferior do intervalo (a): 3.0
Digite o limite superior do intervalo (b): 3.6
Digite o número de subdivisões (n): 6

Digite o número de casas decimais para o arredondamento: 4
```

### Exemplo de Saída
```plaintext
Tabela de Cálculo (Regra do Trapézio):
+------------+-----+------+------+---------+---------+--------------------+------------------+
|   Iteração |   h |   a' |   b' |   f(a') |   f(b') |   Área do Trapézio |   Área Acumulada |
+============+=====+======+======+=========+=========+====================+==================+
|          1 | 0.1 |  3   |  3.1 |  0.3333 |  0.3226 |             0.0328 |           0.0328 |
+------------+-----+------+------+---------+---------+--------------------+------------------+
|          2 | 0.1 |  3.1 |  3.2 |  0.3226 |  0.3125 |             0.0318 |           0.0645 |
+------------+-----+------+------+---------+---------+--------------------+------------------+
|          3 | 0.1 |  3.2 |  3.3 |  0.3125 |  0.303  |             0.0308 |           0.0953 |
+------------+-----+------+------+---------+---------+--------------------+------------------+
|          4 | 0.1 |  3.3 |  3.4 |  0.303  |  0.2941 |             0.0299 |           0.1252 |
+------------+-----+------+------+---------+---------+--------------------+------------------+
|          5 | 0.1 |  3.4 |  3.5 |  0.2941 |  0.2857 |             0.029  |           0.1542 |
+------------+-----+------+------+---------+---------+--------------------+------------------+
|          6 | 0.1 |  3.5 |  3.6 |  0.2857 |  0.2778 |             0.0282 |           0.1823 |
+------------+-----+------+------+---------+---------+--------------------+------------------+

Valor aproximado da integral: 0.1823
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install requirements.txt
```
