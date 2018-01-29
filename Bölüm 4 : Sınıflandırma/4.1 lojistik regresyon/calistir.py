# coding=utf-8
""" Main
Calistir """

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import pandas as pd
import numpy as np

from ciz import dagilim_grafigi, hipotez_grafigi
from maliyeti_hesapla import maliyeti_hesapla
from dereceli_fonksiyon import dereceli_fonksiyon
from sigmoid import sigmoid

from scipy import optimize

u""" 1. Veri Setinin Yuklenmesi """
print '1. Veri Seti Yukleniyor ...'
# Veri Setini Txt Dosyasindan Okuma
ex1data1 = pd.read_csv('ex2data1.txt', delimiter=',', header=None, names=['Exam1', 'Exam2', 'Admission'])

# orjinal veri setini bozmamak icin kopya olusturalim.
veri_seti = ex1data1.copy()

u""" 2. Dagilim Grafigi"""
print '2. Dagilim Grafigi Gosteriliyor ...'
dagilim_grafigi(veri_seti)

# Tahmin Etmeye Calisacagimiz Verileri Okuma
y = veri_seti['Admission'].as_matrix()
del veri_seti['Admission']

# Toplam Girdi Sayisi
m, n = veri_seti.shape

# Ongorucu Veriler, ilk iki degisken: exam1 ve exam2
X_veri = veri_seti.as_matrix()

u""" 3. Kesme Degerinin Eklenmesi"""
print '3. Kesme Degeri Ekleniyor ...'
X = np.ones(shape=(m, (len(X_veri[0]) + 1)))
X[:, 1:(len(X_veri[0]) + 1)] = X_veri

u""" 4. Tetanin ilk Degeri(initial) Ayarlaniyor ..."""
print '4. Tetanin ilk Degeri(initial) Ayarlaniyor ...'
teta = np.zeros(n + 1)

maliyet = maliyeti_hesapla(teta, X, y)
gradyan = dereceli_fonksiyon(teta, X, y)

print ' Initial tetaya gore maliyet: ', maliyet
print ' Initial tetaya gore gradyan: ', gradyan

u""" 5. scipy ile Optimizasyon Yapiliyor ..."""
print '5. scipy ile Optimizasyon Yapiliyor ...'

result = optimize.minimize(
    lambda teta: maliyeti_hesapla(teta, X, y),
    teta,
    method='Nelder-Mead',
    options={
        'maxiter': 400}
)

teta = result.x
maliyet = result.fun
print ' Maliyet: ', maliyet
print ' Teta :', teta

u""" 6. Hipotez Grafigi Gosteriliyor ..."""
print '6. Hipotez Grafigi Gosteriliyor'
# grafik cizilirken kesme degerini ekledigimiz bolumu cikartarak cizdiriyoruz
hipotez_grafigi(X[:, 1:], y, teta)

u""" 7. Tahminler Yapalim ..."""
print '7. Tahminler Yapalim ...'
print ' 45 ve 85 notlarini alan bir ogrencinin kabul edilme olasiligi', sigmoid(np.array([1, 45, 85]).dot(teta))
print ' 50 ve 50 notlarini alan bir ogrencinin kabul edilme olasiligi', sigmoid(np.array([1, 50, 50]).dot(teta))
print ' 65 ve 70 notlarini alan bir ogrencinin kabul edilme olasiligi', sigmoid(np.array([1, 65, 70]).dot(teta))

u""" 8. Modelin Basarisi ..."""
print '8. Modelin Basarisi ...'
tahminler = sigmoid(X.dot(teta)) >= 0.5
basari = 100 * np.mean(tahminler == y)
print ' Egitimin Basarisi : ', basari, '%'
