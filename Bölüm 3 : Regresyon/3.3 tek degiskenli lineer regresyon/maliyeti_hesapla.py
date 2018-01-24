# coding=utf-8
""" Compute Cost Function
Maliyet Fonksiyonunu Hesapla """
import numpy as np


def maliyet_hesapla(x, y, theta):
    """

    :param x: Ongorucu Degisken
    :param y: Hedef Degisken
    :param theta: parametre
    :return: maliyet
    """
    m = len(x)
    toplamin_acilimi = np.power(((x * theta.T) - y), 2)
    maliyet = np.sum(toplamin_acilimi) / (2 * m)
    return maliyet