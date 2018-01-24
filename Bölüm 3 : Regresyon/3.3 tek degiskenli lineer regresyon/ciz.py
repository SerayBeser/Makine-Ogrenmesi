# coding=utf-8
""" Plotting Data
Veri Setinin Grafiginin Cizilmesi"""

import numpy as np
import matplotlib.pyplot as plt


def dagilim_grafigi(veri_seti):
    """

    :param veri_seti: Dagilim Grafiginin Yapilacagi Veri Seti
    """
    x = np.asarray(veri_seti['X'])
    y = np.asarray(veri_seti['Y'])
    plt.figure()
    plt.scatter(x, y, c='magenta', edgecolors='black')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Dagilim Grafigi')
    plt.show()


def hipotez_grafigi(x, y, theta):
    """

    :param x: Ongorucu Degisken, Ev Buyuklukleri
    :param y: Hedef Degisken, Ev Fiyatlari
    :param theta: Parametreler
    """
    agirliklar = np.asarray(theta)
    hipotez = x * agirliklar[0][1] + agirliklar[0][0]
    plt.figure()
    plt.scatter(x, y, c="magenta")
    plt.plot(x, hipotez, c='blue')
    plt.title("Hipotez Egrisi")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def maliyet_devir_grafigi(toplam_devir, maliyet):
    """

    :param toplam_devir: Toplam Devir Sayisi
    :param maliyet: Maliyet
    """
    plt.title("Maliyet - Devir")
    plt.xlabel("Devir Sayisi")
    plt.ylabel(r"Maliyet Fonksiyonu $J(\theta)$")
    plt.plot(np.arange(toplam_devir), maliyet, 'blue')
    plt.show()
