# coding=utf-8
""" Gradient Descent
Dereceli Azalma """
import numpy as np
from maliyeti_hesapla import maliyet_hesapla


def dereceli_azalma(x, y, theta, alpha, epoch):
    """

    :param x: Ongorucu Degisken
    :param y: Hedef Degisken
    :param theta: Parametreler
    :param alpha: Ogrenme Orani
    :param devir_sayisi: Iterasyon Sayisi
    :return: theta: bulunan parametreler ve maliyet
    """
    yeni_theta = np.matrix(np.zeros(theta.shape))
    parametreler = int(theta.ravel().shape[1])

    maliyet_J = np.zeros(shape=(epoch, 1))

    for i in range(epoch):
        hata = (x * theta.T) - y

        for j in range(parametreler):
            term = np.multiply(hata, x[:, j])
            ara_islem = (np.divide(alpha, len(x)) * np.sum(term))
            yeni_theta[0, j] = np.subtract(theta[0, j], ara_islem)

            theta = yeni_theta
            maliyet_J[i, 0] = maliyet_hesapla(x, y, theta)

    return theta, maliyet_J