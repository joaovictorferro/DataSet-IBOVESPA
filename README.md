# DataSet-IBOVESPA

## Indicadores Técnicos

### 1- Simple Moving Average (SMA):
É a média aritmética dos preços de fechamento dos últimos n períodos. Neste caso, os valores mais recentes têm o mesmo peso que os mais antigos. Esta dividido em (5,10,15,20) dias.

### 2- Exponential Moving Average (EMA):
É semelhante ao SMA, mas os preços mais recentes têm um peso maior. É mais sensível a mudanças recentes nos preços do que o SMA.Esta dividido em (5,10,15,20) dias.

### 3- Relative Strength Index (RSI): 
É um indicador de momentum que compara a magnitude dos ganhos recentes com as perdas recentes para determinar se um ativo está sobrecomprado ou sobrevendido. Período escolhido de 14 dias.

### 4- Chande Momentum Oscillator (CMO): 
É um indicador de momentum que mede a taxa de mudança dos preços em relação à média móvel.Período escolhido de 14 dias.

### 5- Commodity Channel Index (CCI):
É um indicador de momentum que mede a relação entre o preço atual e a média móvel dos preços. É usado para identificar mudanças na tendência e condições de sobrecompra ou sobrevenda. Período escolhido de 14 dias.

### 6- Moving Average Convergence Divergence (MACD)
É um indicador que usa a diferença entre duas médias móveis exponenciais para identificar mudanças na tendência. Periódo curto foi de 12 dias e o periódo longo foi de 26 dias.

### 7- 9-period EMA do MACD:
É frequentemente usado como um sinal de compra ou venda. Periódo de 9 dias.

### 8- Rate of Change (ROC):
É um indicador que mede a mudança percentual no preço ao longo do tempo. Periódo 14 dias.

### 9- Percentage Price Oscillator (PPO): 
É semelhante ao MACD, mas usa a diferença percentual entre duas médias móveis exponenciais. Periódo curto foi de 12 dias e o periódo longo foi de 26 dias.

### 10- Triangular Moving Average (TMA): 
É uma média móvel que dá mais peso aos preços mais recentes, usando uma função triangular. Periódo de 20 dias.

### 11- Slow Stochastic %K:
É um indicador que compara o preço atual com o intervalo entre o preço mais alto e mais baixo ao longo de um período de tempo. Periódo de 14 dias.

### 12- Slow Stochastic %D
É a média móvel do Slow Stochastic %K. Periódo de 14 dias.

### 13 - Fast Stochastic %K:
É semelhante ao Slow Stochastic %K, mas usa um período mais curto. Periódo de 9 dias.

### 14 - Fast Stochastic %D:
É a média móvel do Fast Stochastic %K. Periódo de 9 dias.

### 15 - Chaikin A/D Oscillator:
É um indicador que mede o fluxo de dinheiro em um ativo, com base na diferença entre o preço de fechamento e a faixa de negociação. Fast definido de 3 dias e o slow de 10 dias.

### 16- Bollinger Bands:
São três bandas que envolvem a média móvel de um ativo. A banda superior e a banda inferior são dois desvios padrão da média móvel. A banda do meio é a média móvel.

### 17- Highest High:
É o preço mais alto observado durante um determinado período. Periódo de 14 dias.

### 18- Lowest Low:
É o preço mais baixo observado durante um determinado período. Periódo de 14 dias.

### 19- William's %R: 
É um indicador de momentum que compara o preço atual com o intervalo entre o preço mais alto e mais baixo ao longo de um período de tempo, expresso em uma escala de 0 a - 100. Periódo de 14 dias.

## Métricas de Avaliação

### 1- MSE (Mean Squared Error):
É a média do quadrado da diferença entre os valores preditos e os valores reais. É amplamente utilizado porque penaliza grandes erros mais do que pequenos erros.

### 2- EVS (Explained Variance Score):
Mede a proporção da variância nos dados que é explicada pelo modelo. É uma métrica entre 0 e 1, onde 1 indica que o modelo explica toda a variância nos dados.

### 3- MAE (Mean Absolute Error):
É a média da diferença absoluta entre os valores preditos e os valores reais. É menos sensível a outliers do que o MSE.

### 4- MSLE (Mean Squared Logarithmic Error): 
É a média do quadrado do logaritmo da diferença entre os valores preditos e os valores reais. É usado quando a variação dos dados é muito grande.

### 5- R2 (R-squared): 
É uma medida de quão bem o modelo se ajusta aos dados. É uma métrica entre 0 e 1, onde 1 indica um ajuste perfeito do modelo aos dados.

# Referências
