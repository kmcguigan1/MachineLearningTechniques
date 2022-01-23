# the four assumptions of linear regression

Residual
: the error of a model

## Linear relationship
### there exists a linear relationship between x and y

a scatter plot can be used to determine linearity. if there is not then a non linear transformation like taking the log, sqrt, or reciprocal of one of the variables might help. another technique is adding another independent variable.

## Independence
### the residuals are independent. there is no correlation between consecutive residuals in time series data.

we dont want a pattern to emerge among consecutive residuals. ie if residuals grow larger as time goes on.

Durbin-Watson test is to formally test it, otherwise plot the time series of the data and the residuals


## Homoscedasticity 
### the residuals have constant variance at every level of x.

this means that the residuals should all fall in a similar range from the baseline no matter what the value of x is.

this means there is more variance in the regression coefficient estimates, leading to the model declaring a term is more significant when it is not. I think this is becuase the coefficient is more likely to change meaning the algorithm finds it more important to tune? this might not make sense.

we can detect this by plotting the residual as a funciton of the fitted value, ie the model error as a function of the x value.

one technique to eliminate this is to use the log of the dependent variable y in the regression. antoher is to redefine the dependent variable. one example of this is rate. if we were predicting the number of shops in a city based on population data we may use the per capita shop total as the y value. we could also use weighted regression, this assigns weight to each data point based on the variance of its fitted value. This means data with high variance has a lower weight on the regression.

look into the wieghted regression more

## Normality 
### the residuals of the model are normally distributed.

use Q-Q plots to check that residual or error is distributed normally.

we basically plot quantile or z value of the residual versus the quantile or residual of the input value x.

if not good we can verify no outliers exist or apply nonlinear transformation to independent or dependent variable.