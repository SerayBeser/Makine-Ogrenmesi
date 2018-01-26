# coding=utf-8
""" Normal Equation
 Normal Denklemler """

import pandas as pd
import numpy as np
from ozellik_normalizasyonu import ozellik_normalizasyonu

u""" 1- Veri Setinin Yuklenmesi """
print '1- Veri Seti Yukleniyor ...', 'blue'
veri_seti = pd.read_csv('regresyon_veri_2.txt', delimiter=',', header=None, names=['Buyukluk', 'Oda', 'Fiyat'])
y = veri_seti['Fiyat'].as_matrix()
del veri_seti['Fiyat']
X = veri_seti.as_matrix()
m = len(y)

u""" 2- Ozellik Normalizasyonu """
print '2- Ozellik Normalizasyonu Yapiliyor ...'
x, ort, std = ozellik_normalizasyonu(X)

u""" 3- Kesme Degerinin Eklenmesi """
print '3- Kesme Degeri Ekleniyor ...'
X = np.ones(shape=(m, (len(X[0]) + 1)))
X[:, 1:(len(X[0]) + 1)] = x

u""" 4- Normal Denklem ile Tetalarin Hesaplanmasi """
print '4- Normal Denklem ile Tetalar Hesaplanıyor ...'
teta = ((np.linalg.inv(X.T.dot(X))).dot(X.T)).dot(y)  # (X.T * X) ^-1 * X.T * Y
print 'Hesaplanan Teta : ', teta

print '5- Hipotez'
print "J(theta) = " + str(teta[0]) + " + " + str(teta[1]) + " x0 + " + str(
    teta[2]) + " x1"

print '6- Ev Fiyati Tahmini Yapalim ...'
print ('Ev Buyuklugu 1650, 3 yatak odali ise Fiyati : ',
               np.dot([1, ((1650 - ort[0]) / std[0]), ((3 - ort[1]) / std[1])], teta))
print ('Ev Buyuklugu 1604, 3 yatak odali ise Fiyati : ',
               np.dot([1, ((1604 - ort[0]) / std[0]), ((3 - ort[1]) / std[1])], teta))
print ('Ev Buyuklugu 1000, 2 yatak odali ise Fiyati : ',
               np.dot([1, ((1000 - ort[0]) / std[0]), ((2 - ort[1]) / std[1])], teta))