# coding=utf-8
""" Compute Cost Function
 Maliyet Fonksiyonunu Hesapla"""

import numpy as np


def squarred_error_maliyet_hesapla(x, y, teta):
    """

    :param x: Ongorucu Degisken, Ev Buyuklukleri
    :param y: Hedef Degisken, Ev Fiyatlari
    :param teta: parametre
    :return: maliyet
    """
    m = len(x)
    toplamin_acilimi = np.power(((x * teta.T) - y), 2)
    maliyet = np.sum(toplamin_acilimi) / (2 * m)
    return maliyet


def mae_maliyet_fonksiyonu_hesapla(x, y, teta):
    """

    :param x: Ongorucu Degisken, Ev Buyuklukleri
    :param y: Hedef Degisken, Ev Fiyatlari
    :param teta: parametre
    :return: maliyet
    """
    m = len(x)
    toplamin_acilimi = np.abs(((x * teta.T) - y))
    maliyet = np.sum(toplamin_acilimi) / m
    return maliyet


def mse_maliyet_fonksiyonu_hesapla(x, y, teta):
    """

    :param x: Ongorucu Degisken, Ev Buyuklukleri
    :param y: Hedef Degisken, Ev Fiyatlari
    :param teta: parametre
    :return: maliyet
    """
    m = len(x)
    toplamin_acilimi = np.power(((x * teta.T) - y), 2)
    maliyet = np.sum(toplamin_acilimi) / m
    return maliyet


def rmse_maliyet_fonksiyonu_hesapla(x, y, teta):
    """

    :param x: Ongorucu Degisken, Ev Buyuklukleri
    :param y: Hedef Degisken, Ev Fiyatlari
    :param teta: parametre
    :return: maliyet
    """
    m = len(x)
    toplamin_acilimi = np.power(((x * teta.T) - y), 2)
    maliyet = np.sqrt(np.sum(toplamin_acilimi) / m)
    return maliyet