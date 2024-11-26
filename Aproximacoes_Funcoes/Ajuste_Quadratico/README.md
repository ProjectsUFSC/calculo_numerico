# Ajuste Quadrático com Mínimos Quadrados

Este projeto implementa o **método dos mínimos quadrados** para realizar um ajuste **quadrático** de um conjunto de dados experimentais. O ajuste encontra a equação da forma \( y = ax^2 + bx + c \) que melhor se aproxima dos pontos fornecidos, minimizando os resíduos.

---

## Funcionalidades

1. **Cálculo dos coeficientes \(a\), \(b\) e \(c\):** Determina os coeficientes do ajuste quadrático.
2. **Resíduos e SSR:** Calcula os resíduos (\( y_{\text{observado}} - y_{\text{ajustado}} \)) e a soma dos quadrados dos resíduos (SSR).
3. **Tabela de resultados:** Mostra os valores de \(x\), \(y\), \(y_{\text{ajustado}}\) e os resíduos em uma tabela.

---

## Como executar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - **numpy** para cálculos numéricos
  - **tabulate** para exibição em formato de tabela

Instale as dependências com:
```bash
pip install requirements.txt
```

### Executando o programa

1. Clone este repositório ou copie o arquivo Python para o seu ambiente local.
2. Execute o programa:
   ```bash
   python main.py
   ```
3. Siga as instruções do programa para fornecer os dados:
   - Insira o número de pontos \(n\).
   - Forneça os valores de \(x\) e \(y\) separados por espaços.



## Exemplo de execução

Entrada do usuário:
```
Digite o número de pontos experimentais: 6

Digite os valores de x separados por espaço:
0 1 2 3 4 5

Digite os valores de y separados por espaço:
2.1 7.7 13.6 27.2 40.9 61.1
```

Saída do programa:
```
Tabela de Dados e Resíduos:
+----------+-----------+--------------+-----------+
|        x |         y |   y ajustado |   Resíduo |
+==========+===========+==============+===========+
| 0.000000 |  2.100000 |     2.478571 | -0.378571 |
+----------+-----------+--------------+-----------+
| 1.000000 |  7.700000 |     6.698571 |  1.001429 |
+----------+-----------+--------------+-----------+
| 2.000000 | 13.600000 |    14.640000 | -1.040000 |
+----------+-----------+--------------+-----------+
| 3.000000 | 27.200000 |    26.302857 |  0.897143 |
+----------+-----------+--------------+-----------+
| 4.000000 | 40.900000 |    41.687143 | -0.787143 |
+----------+-----------+--------------+-----------+
| 5.000000 | 61.100000 |    60.792857 |  0.307143 |
+----------+-----------+--------------+-----------+

Equação do ajuste quadrático:
y = 1.860714x² + 2.359286x + 2.478571

Soma dos quadrados dos resíduos (SSR):
SSR = 3.746571
```


## Estrutura do Código

1. **`quadratic_least_squares_fit`**: Calcula os coeficientes \(a\), \(b\), e \(c\) do ajuste quadrático.
2. **`calculate_residuals`**: Determina os resíduos entre os valores observados e ajustados.
3. **`print_table`**: Exibe os dados \(x\), \(y\), \(y_{\text{ajustado}}\) e os resíduos em formato tabular.
4. **Bloco principal**: Interage com o usuário para entrada de dados e exibição dos resultados.
