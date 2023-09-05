# IBOVESPA

## Technical Indicators

### 1- Simple Moving Average (SMA):
It is the arithmetic average of the closing prices over the last n periods. In this case, the most recent values have the same weight as the older ones. It is divided into (5, 10, 15, 20) days.

### 2- Exponential Moving Average (EMA):
It is similar to SMA, but the most recent prices have a higher weight. It is more sensitive to recent price changes than SMA. It is divided into (5, 10, 15, 20) days.

### 3- Relative Strength Index (RSI):
It is a momentum indicator that compares the magnitude of recent gains with recent losses to determine if an asset is overbought or oversold. Chosen period of 14 days.

### 4- Chande Momentum Oscillator (CMO):
It is a momentum indicator that measures the rate of change of prices relative to the moving average. Chosen period of 14 days.

### 5- Commodity Channel Index (CCI):
It is a momentum indicator that measures the relationship between the current price and the moving average of prices. It is used to identify trend changes and overbought or oversold conditions. Chosen period of 14 days.

### 6- Moving Average Convergence Divergence (MACD):
It is an indicator that uses the difference between two exponential moving averages to identify trend changes. Short period is 12 days and long period is 26 days.

### 7- 9-period EMA of MACD:
It is often used as a buy or sell signal. 9-day period.

### 8- Rate of Change (ROC):
It is an indicator that measures the percentage change in price over time. 5-day period.

### 9- Percentage Price Oscillator (PPO):
It is similar to MACD but uses the percentage difference between two exponential moving averages. Short period is 12 days and long period is 26 days.

### 10- Triangular Moving Average (TMA):
It is a moving average that gives more weight to recent prices using a triangular function. 20-day period.

### 11- Slow Stochastic %K:
It is an indicator that compares the current price with the range between the highest and lowest price over a period of time. 14-day period.

### 12- Slow Stochastic %D:
It is the moving average of Slow Stochastic %K. 3-day period.

### 13 - Fast Stochastic %K:
It is similar to Slow Stochastic %K but uses a shorter period. 14-day period.

### 14 - Fast Stochastic %D:
It is the moving average of Fast Stochastic %K. 3-day period.

### 15 - Chaikin A/D Oscillator:
It is an indicator that measures the money flow into an asset based on the difference between the closing price and the trading range. Fast set to 3 days and slow set to 10 days.

### 16- Bollinger Bands:
They are three bands that surround the moving average of an asset. The upper band and lower band are two standard deviations from the moving average. The middle band is the moving average.

### 17- Highest High:
It is the highest price observed during a certain period. 14-day period.

### 18- Lowest Low:
It is the lowest price observed during a certain period. 14-day period.

### 19- William's %R:
It is a momentum indicator that compares the current price with the range between the highest and lowest price over a period of time, expressed on a scale from 0 to -100. 14-day period.

## Evaluation Metrics

### 1- MSE (Mean Squared Error):
It is the average of the squared difference between the predicted values and the actual values. It is widely used because it penalizes large errors more than small errors.

### 2- EVS (Explained Variance Score):
It measures the proportion of variance in the data that is explained by the model. It is a metric between 0 and 1, where 1 indicates that the model explains all the variance in the data.

### 3- MAE (Mean Absolute Error):
It is the average of the absolute difference between the predicted values and the actual values. It is less sensitive to outliers than MSE.

### 4- MSLE (Mean Squared Logarithmic Error):
It is the average of the squared logarithmic difference between the predicted values and the actual values. It is used when the data variation is large.

### 5- R2 (R-squared):
It is a measure of how well the model fits the data. It is a metric between 0 and 1, where 1 indicates a perfect fit of the model to the data.
