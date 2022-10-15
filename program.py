import pandas
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pandas.read_csv("clean_train.csv")

formula = "SalePrice ~ GrLivArea"
data = sm.add_constant(data)
mod = smf.ols(formula=formula, data=data)
res = mod.fit()
print(res.rsquared)

x_new = [200]
x_new = sm.add_constant(x_new)
y_pred = mod.predict(x_new) 
print(y_pred)
