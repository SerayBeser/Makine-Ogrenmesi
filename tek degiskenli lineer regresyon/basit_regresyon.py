import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.metrics import mean_squared_error

# veri setinin yuklenmesi
# load dataset
regresyon_veri_1 = pd.read_csv('regresyon_veri_1.txt', header=None, names=['X', 'Y'])

# kopyasini olusturalim, orjinali saklamak icin
# copy dataset for keep original
veri_seti = regresyon_veri_1.copy()

# veri setini inceleyelim.
# explore dataset
print veri_seti.head()
print veri_seti.info()
print veri_seti.describe()

# 85 tane ornek var, eksik deger yok (float64)
# 85 entries, no null value(float64)

# ortalama :
# mean :  X=10.188789  Y=16.030383

# dagilim grafigine bakalim.
# show scatter plot
# plt.scatter(veri_seti.X, veri_seti.Y)
# plt.show()

# Pearson Correlation Coefficient hesaplayalim.
# Compute the Pearson Correlation Coefficient
print veri_seti.corr()

# aralarinda pozitif guclu bir iliski bulunuyor.
# positive strong correlation
# X-Y = r = 0.797

# egitim test seti olarak ayiralim.
# split train-test set
m = len(veri_seti.X)
X = np.reshape(np.asarray(veri_seti.X), (m, -1))
y = np.reshape(np.asarray(veri_seti.Y), (m, -1))

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2, random_state=False)

# modelleri olusturalim.
# create models
model_1 = LinearRegression()
model_2 = TheilSenRegressor()

# modelleri egitelim.
# train models
model_1.fit(X_egitim, y_egitim)
model_2.fit(X_egitim, y_egitim)

# modelleri test edelim.
# test models
tahmin_1 = model_1.predict(X_test)
tahmin_2 = model_2.predict(X_test)

# modellerin basarisina bakalim.
# scores
basari_1 = mean_squared_error(y_test, tahmin_1)
basari_2 = mean_squared_error(y_test, tahmin_2)

print "Lineer Regression Score : ", basari_1
print "Theil-Sen Regressor Score : ", basari_2

# plot
plt.scatter(X_test, y_test, c='cyan', edgecolors='black')
plt.plot(X_test, tahmin_1, 'red')
plt.plot(X_test, tahmin_2, 'blue')
plt.legend(['Lineer Regression', 'Theil-Sen Regressor', 'Veri'])
plt.title('Tek Degiskenli Lineer Regresyon')
plt.tight_layout()
plt.show()
