# coding=utf-8
""" Main
Calistir """

import pandas as pd
import numpy as np

from dereceli_azalma import dereceli_azalma_mini_paket_momentum_ile
from ozellik_normalizasyonu import ozellik_normalizasyonu
from ciz import maliyet_devir_grafigi_ciz

u""" 1- Veri Setinin Yuklenmesi """
print  '1- Veri Seti Yukleniyor ...'  
# Veri Setini Csv Dosyasindan Okuma
veri_seti = pd.read_csv('regresyon_veri_2.txt', delimiter=',', header=None, names=['Buyukluk', 'Oda', 'Fiyat'])

# Tahmin Etmeye Calisacagimiz Verileri Okuma
y = veri_seti['Fiyat'].as_matrix()
del veri_seti['Fiyat']

# Toplam Girdi Sayisi
m = len(y)

# Ongorucu Veriler, ilk iki degisken: buyukluk ve oda sayisi
X_veri = veri_seti.as_matrix()

u""" 2- Ozellik Normalizasyonu """
print  '2- Ozellik Normalizasyonu Yapiliyor ...'  
x, ortalama, standart_sapma = ozellik_normalizasyonu(X_veri)

u""" 3- Kesme Degerinin Eklenmesi"""
print  '3- Kesme Degeri Ekleniyor ...'  
X = np.ones(shape=(m, (len(X_veri[0]) + 1)))
X[:, 1:(len(X_veri[0]) + 1)] = x

# Tahmin Edilecek Hedef Degiskeni Atama ve Boyutunu Ayarlama, yani vektor haline donusturme
y.shape = (m, 1)

u""" 4- Ogrenme Orani ve Devir Sayisinin Ayarlanmasi"""
print  '4- Ogrenme Orani ve Devir Sayisi Ayarlaniyor ...'  
toplam_devir = 1000
alfa = 0.001

print  'Devir Sayisi ', toplam_devir
print  'Alfa ', alfa

beta_mse = np.zeros((len(X[0]), 1))
beta_mae = np.zeros((len(X[0]), 1))
beta_sqrt_err = np.zeros((len(X[0]), 1))
beta_rmse = np.zeros((len(X[0]), 1))

paket = 50

u""" 5.3 - Momentum ile Mini Paket Dereceli Azalmanin Hesaplanmasi"""
print  '5.3- Momentum Mini Paket Dereceli Azalma Hesaplaniyor ...'  
beta_mse, maliyet_mse = dereceli_azalma_mini_paket_momentum_ile(X, y, beta_mse, alfa, toplam_devir, paket, 'mse')
beta_mae, maliyet_mae = dereceli_azalma_mini_paket_momentum_ile(X, y, beta_mae, alfa, toplam_devir, paket, 'mae')
beta_sqrt_err, maliyet_sqrt_err = dereceli_azalma_mini_paket_momentum_ile(X, y, beta_sqrt_err, alfa, toplam_devir,
                                                                          paket,
                                                                          'squared_error')
beta_rmse, maliyet_rmse = dereceli_azalma_mini_paket_momentum_ile(X, y, beta_rmse, alfa, toplam_devir, paket, 'rmse')

u""" 6- Dereceli Azalmanin Dogru Calisip Calismadiginin Kontrolu"""
print  '6- Maliyet Fonksiyonu - Devir Sayisi Grafigi Kaydediliyor ...'  
maliyet_devir_grafigi_ciz(toplam_devir, maliyet_mse, maliyet_mae, maliyet_sqrt_err, maliyet_rmse,
                          baslik='Mini Paket Dereceli Azalma Momentum Optimizasyon ile')

u""" 7- Sonuc"""
print  'Hesaplanan Beta (MSE) ', beta_mse
print  'Hesaplanan Beta (MAE) ', beta_mae
print  'Hesaplanan Beta (SQRT ERR) ', beta_sqrt_err
print  'Hesaplanan Beta (RMSE) ', beta_rmse

print  '7- Hipotez (SQRT ERR\'e gore)'  
print  "J(theta) = " + str(beta_sqrt_err[0][0]) + " + " + str(beta_sqrt_err[1][0]) + " x0 + " + str(
    beta_sqrt_err[2][0]) + " x1"

print  '8- Ev Fiyati Tahmini Yapalim ... (SQRT ERR\'e gore)'  

# X Verilerinde Normalizasyon Yaptigimiz Icin Direkt Kullanamayiz.
# Tahmin etmek icin X ongorucu degiskenlerimizi buldugumuz
# ortalama ve standart sapmalara gore normalize edip kullaniyoruz
x0 = 1
x1 = (1650 - ortalama[0]) / standart_sapma[0]
x2 = (3 - ortalama[1]) / standart_sapma[1]
tahmin = np.dot([x0, x1, x2], beta_sqrt_err)

print  'Ev Buyuklugu 1650, 3 yatak odali ise Fiyati : ', tahmin[0]

x0 = 1
x1 = (1604 - ortalama[0]) / standart_sapma[0]
x2 = (3 - ortalama[1]) / standart_sapma[1]
tahmin = np.dot([x0, x1, x2], beta_sqrt_err)

print  'Ev Buyuklugu 1604, 3 yatak odali ise Fiyati : ', tahmin[0]

x0 = 1
x1 = (1000 - ortalama[0]) / standart_sapma[0]
x2 = (2 - ortalama[1]) / standart_sapma[1]
tahmin = np.dot([x0, x1, x2], beta_sqrt_err)

print  'Ev Buyuklugu 1000, 2 yatak odali ise Fiyati : ', tahmin[0]