import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, TheilSenRegressor, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# veri setinin yuklenmesi
# load dataset
regression_data_1 = pd.read_csv('../input/regression_data_1.txt', header=None, names=['X', 'Y'])

# kopyasini olusturalim, orjinali saklamak icin
# copy dataset for keep original
data_set = regression_data_1.copy()

# veri setini inceleyelim.
# explore dataset
print data_set.head()
print data_set.info()
print data_set.describe()

# 85 tane ornek var, eksik deger yok (float64)
# 85 entries, no null value(float64)

# ortalama :
# mean :  X=10.188789  Y=16.030383

# dagilim grafigine bakalim.
# show scatter plot
# plt.scatter(data_set.X, data_set.Y)
# plt.show()

# Pearson Correlation Coefficient hesaplayalim.
# Compute the Pearson Correlation Coefficient
print data_set.corr()

# aralarinda pozitif guclu bir iliski bulunuyor.
# positive strong correlation
# X-Y = r = 0.797

# egitim test seti olarak ayiralim.
# split train-test set
m = len(data_set.X)
X = np.reshape(np.asarray(data_set.X), (m, -1))
y = np.reshape(np.asarray(data_set.Y), (m, -1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=False)

# modelleri olusturalim.
# create models
model_1 = LinearRegression()
model_2 = TheilSenRegressor()
model_3 = Ridge()
model_4 = Lasso()

# modelleri egitelim.
# train models
model_1.fit(X_train, y_train)
model_2.fit(X_train, y_train)
model_3.fit(X_train, y_train)
model_4.fit(X_train, y_train)

# modelleri test edelim.
# test models
prediction_1 = model_1.predict(X_test)
prediction_2 = model_2.predict(X_test)
prediction_3 = model_3.predict(X_test)
prediction_4 = model_4.predict(X_test)

# modellerin basarisina bakalim.
# scores
score_1 = mean_squared_error(y_test, prediction_1)
score_2 = mean_squared_error(y_test, prediction_2)
score_3 = mean_squared_error(y_test, prediction_3)
score_4 = mean_squared_error(y_test, prediction_4)

print "Lineer Regression Score : ", score_1
print "Theil-Sen Regressor Score : ", score_2
print "Ridge Regression Score : ", score_3
print "Lasso Regression Score : ", score_4

# plot
plt.scatter(X_test, y_test, c='cyan', edgecolors='black')
plt.plot(X_test, prediction_1, 'red', lw=5)
plt.plot(X_test, prediction_2, 'blue')
plt.plot(X_test, prediction_3, 'orange')
plt.plot(X_test, prediction_4, 'green')
plt.legend(['Lineer Regression', 'Theil-Sen Regressor', 'Ridge Regression', 'Lasso Regression', 'Veri'])
plt.title('Tek Degiskenli Lineer Regresyon, One-Variable Lineer Regression')
plt.tight_layout()
plt.show()
