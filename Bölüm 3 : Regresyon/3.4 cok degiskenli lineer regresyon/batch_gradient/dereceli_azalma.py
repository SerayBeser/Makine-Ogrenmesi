# coding=utf-8
""" Gradient Descent
 Dereceli Azalma """

import numpy as np
from maliyet_hesapla import squarred_error_maliyet_hesapla, mae_maliyet_fonksiyonu_hesapla, \
    mse_maliyet_fonksiyonu_hesapla, \
    rmse_maliyet_fonksiyonu_hesapla


def dereceli_azalma(x, y, beta, alfa, devir_sayisi, maliyet_fonksiyonu):
    """

    :param x: ozellik degiskenleri
    :param y: hedef degisken
    :param beta: parametreler
    :param alfa: ogrenme orani
    :param devir_sayisi: devir sayisi
    :param maliyet_fonksiyonu: hesaplanacak maliyet fonksiyonu turu
    :return: beta ve maliyet fonksiyonu
    """
    maliyet_J = np.zeros(shape=(devir_sayisi, 1))

    for devir in range(devir_sayisi):

        m = y.size

        tahminler = x.dot(beta)
        beta_size = beta.size

        for i in range(beta_size):
            X_i = x[:, i]
            X_i.shape = (m, 1)

            beta[i][0] = beta[i][0] - alfa * (1.0 / m) * ((tahminler - y) * X_i).sum()

        if maliyet_fonksiyonu == 'mse':
            maliyet_J[devir, 0] = mse_maliyet_fonksiyonu_hesapla(x, y, beta)
        if maliyet_fonksiyonu == 'mae':
            maliyet_J[devir, 0] = mae_maliyet_fonksiyonu_hesapla(x, y, beta)
        if maliyet_fonksiyonu == 'rmse':
            maliyet_J[devir, 0] = rmse_maliyet_fonksiyonu_hesapla(x, y, beta)
        if maliyet_fonksiyonu == 'squared_error':
            maliyet_J[devir, 0] = squarred_error_maliyet_hesapla(x, y, beta)
    return beta, maliyet_J