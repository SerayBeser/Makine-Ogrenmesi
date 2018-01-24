# coding=utf-8
""" Main
Calistir """

from ciz import dagilim_grafigi, hipotez_grafigi, maliyet_devir_grafigi
from dereceli_azalma import dereceli_azalma
import pandas as pd
import numpy as np

u""" 1- Veri Setinin Yuklenmesi """
print '1. Veri Seti Yukleniyor...'
regresyon_veri_1 = pd.read_csv('regresyon_veri_1.txt', header=None, names=['X', 'Y'])

# orjinal veri setini bozmamak icin kopya olusturalim.
veri_seti = regresyon_veri_1.copy()

print '2. Verilerin Dagilim Grafigi Gosteriliyor ...'
dagilim_grafigi(veri_seti)

print '3. Veri Arastirmasi ...'
print 'Verilerin Arasindaki Iliski, Pearson Momentler Carpimi :'
print veri_seti.corr()
print 'Aralarinda Guclu Pozitif Korelasyon var, r : 0.797073934649'

u""" 4. Kesme Degerinin Eklenmesi"""
print '4. Kesme Degeri Ekleniyor...'
veri_seti.insert(0, 'Kesme Degeri', 1)
kesme_degeri_kolonu = veri_seti.shape[1]
X = np.matrix(veri_seti.iloc[:, 0:kesme_degeri_kolonu - 1])
y = np.matrix(veri_seti.iloc[:, kesme_degeri_kolonu - 1:kesme_degeri_kolonu])

teta = np.matrix(np.array([0, 0]))

u""" 5. Ogrenme Orani ve Devir Sayisinin Ayarlanmasi"""
print '5. Ogrenme Orani ve Devir Sayisi Ayarlaniyor ...'
alpha = 0.0001
toplam_devir = 1000

print 'Devir Sayisi ', toplam_devir
print 'Alfa ', alpha

u""" 6. Dereceli Azalmanin Hesaplanmasi"""
print '6. Dereceli Azalma Hesaplaniyor ...'
teta, maliyet = dereceli_azalma(X, y, teta, alpha, toplam_devir)

u""" 5- Sonuc"""
print '5- [Sonuc]: Grafikler ...'
print 'Hesaplanan Teta ', teta
maliyet_devir_grafigi(toplam_devir, maliyet)
hipotez_grafigi(veri_seti['X'], veri_seti['Y'], teta)

print '[BILGI] : Program Basari ile Sonlandi.'
