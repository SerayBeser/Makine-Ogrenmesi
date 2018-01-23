import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://wiki.csc.calpoly.edu/datasets/wiki/Houses
print '1 - Veri Seti Yukleniyor...'
houses = pd.read_csv('RealEstate.csv')
veri_seti = houses.copy()
print 'HOUSES veri seti yuklendi. Bir kopyasi olusturuldu.'

print '2 - Veriye Hizli Bir Bakis...'
print 'Veri Setinin ilk 5 ornegi :\n', veri_seti.head()
print 'Veri Setinin Ozellikleri :\n', veri_seti.info()
print 'Sayisal Verilerin Ozellikleri :\n', veri_seti.describe()
print 'Sayisal Verilerin Dagilim Grafikleri Gosteriliyor...\n'
veri_seti.hist(color='magenta')
plt.show()

print '3 - Veriyi Hazirlayalim...'
# kullanmayacagimiz ozellikleri temizleyelim.
del veri_seti['MLS']
del veri_seti['Location']
del veri_seti['Bedrooms']
del veri_seti['Bathrooms']
del veri_seti['Price/SQ.Ft']
del veri_seti['Status']
print 'Kullanilmayacak Ozellikler Silindi.'

# veri donusumu islemini yapalim.
# 1 square foot = 0.09290304 m2
veri_seti['Size'] = veri_seti['Size'] * 0.09290304
print 'Square Foot degeri Metrekareye Donusturuldu.'

print 'Veri Setinin Yeni Hali :'
print veri_seti.head()

# ozelliklerin isimlerini turkceye cevirelim
veri_seti.rename(columns={'Price': 'Fiyat', 'Size': 'Buyukluk'}, inplace=True)

print veri_seti.corr(method='pearson')

plt.scatter(x=veri_seti.Buyukluk, y=veri_seti.Fiyat, edgecolors='black', c='magenta')
plt.title('Ev Fiyatlari - Buyuklukleri')
plt.xlabel(r'$Buyuluk (m^2)$')
plt.ylabel(r'$Fiyat (TL)$')
plt.tight_layout()
plt.show()

# veri setini test ve egitim olarak ikiye ayiralim.
from sklearn.model_selection import train_test_split

X = veri_seti.Buyukluk
y = veri_seti.Fiyat

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2, random_state=False)


# makine ogrenmesi
# modeli olusturalim
# m = [ nE(xy) - ExEy) ]  / [ nE(x^2)-(Ex)^2 ]
# b = ( Ey - mEx ) / n
class lineer_regresyon:
    def __init__(self):
        self.m = 0
        self.b = 0

    def egit(self, _x_, _y_):
        _x_ = np.asarray(_x_)
        _y_ = np.asarray(_y_)
        n = len(np.asarray(_x_))
        self.m = (n * sum(_x_ * _y_) - sum(_x_) * sum(_y_)) / (n * sum(_x_ * _x_) - sum(_x_) * sum(_x_))
        self.b = (sum(_y_) - self.m * sum(_x_)) / n

    def tahmin_et(self, _x_test_):
        return self.m * np.asarray(_x_test_) + self.b


# MSE = ( 1 / n ) * ( E(y - yi)^2 )
def ortalama_kare_hata(_y_test_, _y_tahmin_):
    _y_test_ = np.asarray(_y_test_)
    return sum((_y_test_ - _y_tahmin_) ** 2) / len(_y_test_)


model = lineer_regresyon()
model.egit(X_egitim, y_egitim)
y_tahmin = model.tahmin_et(X_test)

basari = ortalama_kare_hata(y_test, y_tahmin)

plt.scatter(X_test, y_test, c='magenta', edgecolors='black')
plt.plot(X_test, y_tahmin, c='blue')
plt.title('Ev Fiyatlari - Buyuklukleri')
plt.xlabel(r'$Buyuluk (m^2)$')
plt.ylabel(r'$Fiyat (TL)$')
plt.tight_layout()
plt.show()

tahminimiz = model.tahmin_et(232)
print '232 metrekarelik evin fiyati : ', tahminimiz, 'TL'

plt.scatter(X_test, y_test, edgecolors='black', c='yellow')
plt.plot(X_test, y_tahmin, c='blue', zorder=1)
plt.scatter(232, tahminimiz, edgecolors='black', c='red', s=100, zorder=2)
plt.title('232 metrekarelik Evin Fiyati')
plt.xlabel(r'$Buyuluk (m^2)$')
plt.ylabel(r'$Fiyat (TL)$')
plt.legend(['Model', 'Veri', r'232 $(m^2)$lik evin fiyati'])
plt.tight_layout()
plt.show()
