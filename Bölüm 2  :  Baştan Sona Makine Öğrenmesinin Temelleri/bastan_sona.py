import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. PROBLEM:  Odenen hesaba gore verilen bahsisler nasil degisir?

# 1. veri setini yukleyelim
veri_seti = sns.load_dataset('tips')

# 2. ozellik secimi yapalim
del veri_seti['sex']
del veri_seti['size']
del veri_seti['time']
del veri_seti['day']
del veri_seti['smoker']

# 3. veri setini test-egitim diye ayiralim ve ongorucu-hedef degiskenleri belirleyelim
from sklearn.model_selection import train_test_split

m = len(veri_seti)

# ozellikleri vektor haline donusturme
X = np.reshape(np.asarray(veri_seti['total_bill']), (m, -1))
y = np.reshape(np.asarray(veri_seti['tip']), (m, -1))

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2)

# 4. modeli olusturalim
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# 5. modelimizi egitelim
model.fit(X_egitim, y_egitim)

# 6. modeli test edelim
y_tahmin = model.predict(X_test)

# 7. modelin basarisini olcelim
from sklearn.metrics import mean_squared_error

basari = mean_squared_error(y_test, y_tahmin)

print 'MSE Skoru : ', basari

# 8. test verisi ve modelin grafigini inceleyelim
plt.scatter(X_test, y_test, edgecolors='black', c='magenta')
plt.plot(X_test, y_tahmin, c='orange', zorder=1)
plt.title('Odenen Hesaba gore Verilen Bahsis Miktari')
plt.xlabel('Hesap')
plt.ylabel('Bahsis')
plt.legend(['Model', 'Veri'])
plt.show()

# 2. PROBLEM : 26.5 lira hesap odeyen bir kadin ne kadar bahsis birakir

# 1. veri setini tekrar yukleyelim
veri_seti = sns.load_dataset('tips')

veri_seti = sns.load_dataset('tips')
veri_setinin_kopyasi = veri_seti.copy()
# bundan sonraki islemleri veri_setinin_kopyasi uzerinde yaparsaniz, orjinal veri_seti ni bozmadan tutmus olursunuz


# sadece sex=Female olan ornekleri alma islemi
veri_seti = veri_seti[veri_seti['sex'] == 'Female']

print veri_seti.head()

# 2. ozellik secimi yapalim
del veri_seti['sex']
del veri_seti['size']
del veri_seti['time']
del veri_seti['day']
del veri_seti['smoker']

# 3. veri setini test-egitim diye ayiralim ve ongorucu-hedef degiskenleri belirleyelim
from sklearn.model_selection import train_test_split

m = len(veri_seti)

# ozellikleri vektor haline donusturme
X = np.reshape(np.asarray(veri_seti['total_bill']), (m, -1))
y = np.reshape(np.asarray(veri_seti['tip']), (m, -1))

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2, random_state=False)

# 4. modeli olusturalim
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# 5. modelimizi egitelim
model.fit(X_egitim, y_egitim)

# 6. modeli test edelim
y_tahmin = model.predict(X_test)

# 7. modelin basarisini olcelim
from sklearn.metrics import mean_squared_error

basari = mean_squared_error(y_test, y_tahmin)

print 'MSE Skoru (sadece Female verisi icin): ', basari

tahminimiz = model.predict(26.5)
print '26.5 lira hesap odeyen kadinin verecegi tahmini bahsis ', tahminimiz

# 8. test verisi ve modelin grafigini inceleyelim
plt.scatter(X_test, y_test, edgecolors='black', c='yellow')
plt.plot(X_test, y_tahmin, c='blue', zorder=1)

plt.scatter(26.5, tahminimiz, edgecolors='black', c='red', s=100, zorder=2)
plt.title('26.5 lira Hesap Odeyen Kadinin Verecegi Bahsis')

plt.xlabel('Hesap')
plt.ylabel('Bahsis')
plt.legend(['Model', 'Veri', '26.5 Hesap icin Tahmini Bahsis'])
plt.show()
