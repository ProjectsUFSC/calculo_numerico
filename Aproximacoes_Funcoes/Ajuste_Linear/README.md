# Ajuste Linear com Mínimos Quadrados

Este projeto implementa o **método dos mínimos quadrados** para realizar um ajuste linear de um conjunto de dados experimentais. O código é escrito em Python e calcula a equação da reta que melhor se ajusta aos dados no formato \( y = ax + b \), além de exibir os resíduos e a soma dos quadrados dos resíduos (SSR).


## Funcionalidades

1. **Cálculo dos coeficientes \(a\) e \(b\):** Determinação da equação da reta \( y = ax + b \) que minimiza os resíduos.
2. **Resíduos e SSR:** Calcula os resíduos (\( y_{\text{observado}} - y_{\text{ajustado}} \)) e exibe a soma dos quadrados dos resíduos.
3. **Tabela de resultados:** Mostra uma tabela tabulada com os valores de \(x\), \(y\), os valores ajustados (\( y_{\text{ajustado}} \)) e os resíduos.


## Como executar

### Pré-requisitos
- Python 3.7 ou superior
- Biblioteca **numpy** para cálculos numéricos
- Biblioteca **tabulate** para exibição em formato de tabela

Instale as dependências executando:
```bash
pip install requirements.txt
```

### Executando o programa
1. Clone este repositório ou copie o arquivo Python para o seu ambiente local.
2. Execute o programa com:
   ```bash
   python main.py
   ```

3. Siga as instruções do programa para fornecer os dados:
   - Insira o número de pontos \(n\).
   - Forneça os valores de \(x\) e \(y\) separados por espaços.


## Exemplo de execução

Entrada do usuário:
```
Digite o número de pontos experimentais: 11

Digite os valores de x separados por espaço:
-1.00 -0.75 -0.6 -0.5 -0.3 0.0 0.2 0.4 0.5 0.7 1.0

Digite os valores de y separados por espaço:
1.0 1.7 1.5 2.4 2.0 2.0 4.0 3.8 4.0 5.0 4.5
```

Saída:
```
Tabela de Dados e Resíduos:
+-----------+----------+--------------+-----------+
|         x |        y |   y ajustado |   Resíduo |
+===========+==========+==============+===========+
| -1.000000 | 1.000000 |     0.968886 |  0.031114 |
+-----------+----------+--------------+-----------+
| -0.750000 | 1.700000 |     1.467531 |  0.232469 |
+-----------+----------+--------------+-----------+
| -0.600000 | 1.500000 |     1.766717 | -0.266717 |
+-----------+----------+--------------+-----------+
| -0.500000 | 2.400000 |     1.966175 |  0.433825 |
+-----------+----------+--------------+-----------+
| -0.300000 | 2.000000 |     2.365091 | -0.365091 |
+-----------+----------+--------------+-----------+
|  0.000000 | 2.000000 |     2.963464 | -0.963464 |
+-----------+----------+--------------+-----------+
|  0.200000 | 4.000000 |     3.362379 |  0.637621 |
+-----------+----------+--------------+-----------+
|  0.400000 | 3.800000 |     3.761295 |  0.038705 |
+-----------+----------+--------------+-----------+
|  0.500000 | 4.000000 |     3.960753 |  0.039247 |
+-----------+----------+--------------+-----------+
|  0.700000 | 5.000000 |     4.359668 |  0.640332 |
+-----------+----------+--------------+-----------+
|  1.000000 | 4.500000 |     4.958041 | -0.458041 |
+-----------+----------+--------------+-----------+

Equação da reta ajustada:
y = 1.994578x + 2.963464

Soma dos quadrados dos resíduos (SSR):
SSR = 2.405331
```


## Estrutura do código

1. **`least_squares_fit`**: Calcula os coeficientes \(a\) e \(b\) para o ajuste linear.
2. **`calculate_residuals`**: Determina os resíduos entre os valores observados \(y\) e os valores ajustados \(y_{\text{ajustado}}\).
3. **`print_table`**: Exibe os dados \(x\), \(y\), \(y_{\text{ajustado}}\) e os resíduos em formato de tabela.
4. **Bloco principal**: Interage com o usuário para entrada de dados e exibição dos resultados.
