Dataset
: California housing dataset
Model
: Linear Regression
Metrics
: RMSE
One sentence insight (“Model over/under fits because…”): Model overfits because it is not able to generalize well on the test data
### Analysis of Train-Test Split Ratios

The distribution of data between training and testing sets significantly impacts the model's bias-variance tradeoff and the reliability of performance metrics:

*   **80/20 Split (Training: 80%, Testing: 20%)**: 
    *   **Pros**: Maximizes the data available for the model to learn complex patterns, typically leading to lower bias and better parameter estimation.
    *   **Cons**: The smaller test set may lead to higher variance in the evaluation metrics (RMSE), as the results are more sensitive to specific outliers in the test data.
*   **70/30 Split (Training: 70%, Testing: 30%)**: 
    *   **Pros**: The industry standard balance. It provides sufficient data for the model to converge while maintaining a large enough test set for statistically significant evaluation.
*   **60/40 Split (Training: 60%, Testing: 40%)**: 
    *   **Pros**: Provides a very rigorous test of the model's generalization capabilities. If the model performs well here, it is likely highly robust.
    *   **Cons**: Reducing training data to 60% often leads to underfitting or higher RMSE, as the model lacks enough examples to capture the full distribution of the California housing market.

### Performance Summary

| Metric | 80/20 Split | 70/30 Split | 60/40 Split |
| :--- | :--- | :--- | :--- |
| **Training Samples** | ~16,512 | ~14,448 | ~12,384 |
| **Testing Samples** | ~4,128 | ~6,192 | ~8,256 |
| **Generalization** | High | Moderate | Low (Current) |
| **Reliability of Results** | Moderate | High | Very High |



SCREENSHOTS

SCREENSHOT 1
    output_40-2.png
    
SCREENSHOT 2
    output_40.png

SCREENSHOT 3
    output_40-3.png

Results 

AS RMSE is high, model is not able to generalize well on the test data

Here are results as 40% of data is used for testing

OLS Regression Results
Dep. Variable:	median_house_value	R-squared:	0.643
Model:	OLS	Adj. R-squared:	0.643
Method:	Least Squares	F-statistic:	2456.
Date:	Sat, 03 Jan 2026	Prob (F-statistic):	0.00
Time:	19:21:03	Log-Likelihood:	-2.0522e+05
No. Observations:	16346	AIC:	4.105e+05
Df Residuals:	16333	BIC:	4.106e+05
Df Model:	12		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
const	-2.147e+06	1.05e+05	-20.413	0.000	-2.35e+06	-1.94e+06
longitude	-2.722e+04	1141.708	-23.841	0.000	-2.95e+04	-2.5e+04
latitude	-2.612e+04	1125.571	-23.208	0.000	-2.83e+04	-2.39e+04
housing_median_age	1036.3175	49.179	21.072	0.000	939.922	1132.713
total_rooms	-6.3977	0.891	-7.184	0.000	-8.143	-4.652
total_bedrooms	99.7707	7.613	13.105	0.000	84.848	114.694
population	-37.3546	1.189	-31.405	0.000	-39.686	-35.023
households	49.9035	8.223	6.069	0.000	33.786	66.021
median_income	3.937e+04	382.254	102.983	0.000	3.86e+04	4.01e+04
<1H OCEAN	-1.49e+05	3.43e+04	-4.339	0.000	-2.16e+05	-8.17e+04
INLAND	-1.878e+05	3.44e+04	-5.456	0.000	-2.55e+05	-1.2e+05
NEAR BAY	-1.519e+05	3.44e+04	-4.416	0.000	-2.19e+05	-8.45e+04
NEAR OCEAN	-1.457e+05	3.44e+04	-4.239	0.000	-2.13e+05	-7.83e+04
Omnibus:	4103.497	Durbin-Watson:	2.017
Prob(Omnibus):	0.000	Jarque-Bera (JB):	16258.145
Skew:	1.201	Prob(JB):	0.00
Kurtosis:	7.255	Cond. No.	8.08e+05


Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.08e+05. This might indicate that there are
strong multicollinearity or other numerical problems.