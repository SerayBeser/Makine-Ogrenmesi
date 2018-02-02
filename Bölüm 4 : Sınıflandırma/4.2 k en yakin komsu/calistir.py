# coding=utf-8
""" Main
Calistir """
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from ciz import dagilim_grafigi, hipotez_grafigi
from k_en_yakin_komsu import KEnYakinKomsu

u""" 1. Veri Setinin Yuklenmesi """
print '1. Veri Seti Yukleniyor ...'
# Veri Setini Csv Dosyasindan Okuma
iris = pd.read_csv('iris.csv', header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class'])

# orjinal veri setini bozmamak icin kopya olusturalim.
veri_seti = iris.copy()

# sadece sepal length ve sepal width ozellikleri kullanarak knn algoritmasini kullanacagiz
# bu nedenle kullanmayacagimiz verileri silelim
del veri_seti['PetalLength']
del veri_seti['PetalWidth']

u""" 2. Dagilim Grafigi"""
print '2. Dagilim Grafigi Gosteriliyor ...'
dagilim_grafigi(veri_seti)

# Tahmin Etmeye Calisacagimiz Verileri Okuma
y = veri_seti['Class'].as_matrix()
del veri_seti['Class']

# Toplam Girdi Sayisi
m, n = veri_seti.shape

# Ongorucu Veriler, ilk iki degisken: sepal length ve sepal width
X = veri_seti.as_matrix()

u""" 3. Egitim-Test Setinin Bolunmesi"""
print '3. Egitim-Test Seti Bolunmesi Yapiliyor ...'
X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.30, random_state=False)

print ' Egitim Seti: ', len(X_egitim)
print ' Test Seti: ', len(X_test)

# X,y setleri birlestiriliyor, ve type=liste
y_egitim = np.reshape(y_egitim, (-1, len(y_egitim)))
egitim = np.concatenate((X_egitim, y_egitim.T), axis=1).tolist()

y_test = np.reshape(y_test, (-1, len(y_test)))
test = np.concatenate((X_test, y_test.T), axis=1).tolist()

u""" 4. KNN Algoritmasinin Calistirilmasi"""
print '4. KNN Algoritmasinin Calistiriliyor ...'

k_NN = KEnYakinKomsu(k=3)
tahminler = list()
for t in test:
    komsular = k_NN.komsulari_bul(egitim, t)
    sonuc = k_NN.tahmin_et(komsular)
    tahminler.append(sonuc)

u""" 5. KNN Algoritmasinin Basarisi Hesaplaniyor..."""
print '5. KNN Algoritmasinin Basarisi Hesaplaniyor ...'

dogru_tahmin_sayisi = 0
for i in range(len(test)):
    if test[i][-1] == tahminler[i]:
        dogru_tahmin_sayisi += 1

print ' Basarisi : ', dogru_tahmin_sayisi / float(len(test)) * 100.0, '%'

u""" 6. Test Setinin Grafigi ..."""
print '6. Test Setinin Grafigi Gosteriliyor...'

egitim_seti = pd.DataFrame(egitim, columns=['SepalLength', 'SepalWidth', 'Class'])
tahminler = np.reshape(np.array(tahminler), (-1, len(tahminler)))
test = np.concatenate((test, (tahminler).T), axis=1)
test_seti = pd.DataFrame(test, columns=['SepalLength', 'SepalWidth', 'Class', 'Prediction'])

hipotez_grafigi(egitim_seti, test_seti)
