# coding=utf-8
""" k en yakin komsu
k nearest neighbor"""

import math

import operator


def oklit_uzakligi(x1, x2, uzunluk):
    mesafe = 0
    for i in range(uzunluk):
        mesafe += pow((x1[i] - x2[i]), 2)
    return math.sqrt(mesafe)


class KEnYakinKomsu():

    def __init__(self, k):
        self.k = k

    def komsulari_bul(self, egitim, test):

        uzakliklar = list()
        ozellik_sayisi = len(test) - 1
        for e in egitim:
            uzaklik = oklit_uzakligi(test, e, ozellik_sayisi)
            uzakliklar.append((e, uzaklik))
        uzakliklar.sort(key=operator.itemgetter(1))
        komsular = list()
        for i in range(self.k):
            komsular.append(uzakliklar[i][0])
        return komsular

    def tahmin_et(self, komsular):
        siniflandirma_oyu = dict()
        for x in range(len(komsular)):
            oy = komsular[x][-1]
            if oy in siniflandirma_oyu:
                siniflandirma_oyu[oy] += 1
            else:
                siniflandirma_oyu[oy] = 1
        sirali_oylar = sorted(siniflandirma_oyu.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sirali_oylar[0][0]
