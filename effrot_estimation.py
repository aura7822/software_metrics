#effort estimation using linear regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data={
    'KLOC': [2.5,5.0,7.5,10.0,12.5,15.0,17.5,20.0],
    'EFFORT':[25,45,70,90,110,135,160,180] #person-months

}

aura = pd.DataFrame(data)
aura
plt.scatter(aura['KLOC'],aura['EFFORT'],color='blue')
plt.xlabel("KLOC(Thousand lines of code)")
plt.ylabel("Effort per persons(months)")
plt.title("Efforts vs KLOC")
plt.grid(True)
plt.show()

X=aura[['KLOC']]
y=aura['EFFORT']
model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)
print("Intercept : ",model.intercept_)
print("Slope(KLOC coefficient):",model.coef_[0])

print("R2 score : ",r2_score(y,y_pred))
print("Mean squared error : ",mean_squared_error(y,y_pred))

plt.scatter(X,y,color='red',label='Actual Effort')
plt.plot(X,y_pred,color='cyan',linewidth=2, label='Predicted Effort')
plt.xlabel("KLOC")
plt.ylabel("Efort")
plt.title("Linear regression : effort estimation")
plt.legend()
plt.grid(True)
plt.show()
