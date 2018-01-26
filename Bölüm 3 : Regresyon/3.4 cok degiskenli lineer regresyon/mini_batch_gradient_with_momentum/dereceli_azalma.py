# coding=utf-8
""" Mini Batch Gradient Descent with Momentum
Mini Paket Dereceli Azalma Momentum ile """

import numpy as np
from maliyet_hesapla import squarred_error_maliyet_hesapla, mae_maliyet_fonksiyonu_hesapla, \
    mse_maliyet_fonksiyonu_hesapla, \
    rmse_maliyet_fonksiyonu_hesapla


def mini_paket_al(x, y, mini_paket_buyuklugu):
    """

    :param x: ozellik degiskenleri
    :param y: hedef degisken
    :param mini_paket_buyuklugu:
    :return: veri setinden secilen paket(mini batch)
    """
    mini_paketler = []

    # X, y = np.random.shuffle(X,y)

    for i in range(0, x.shape[0], mini_paket_buyuklugu):
        x_mini = x[i:i + mini_paket_buyuklugu]
        y_mini = y[i:i + mini_paket_buyuklugu]

        mini_paketler.append((x_mini, y_mini))

    return mini_paketler


def dereceli_azalma_mini_paket_momentum_ile(x, y, beta, alfa, devir_sayisi, paket_buyuklugu, maliyet_fonksiyonu):
    """

    :param x: ozellik degiskenleri
    :param y: hedef degisken
    :param beta: parametreler
    :param alfa: ogrenme orani
    :param devir_sayisi: devir sayisi
    :param paket_buyuklugu: secilen mini paketin buyuklugu
    :param maliyet_fonksiyonu: hesaplanacak maliyet fonksiyonu turu
    :return: beta ve maliyet fonksiyonu
    """
    maliyet_J = np.zeros(shape=(devir_sayisi, 1))
    momentum_sabiti = 0.9
    hiz = 1
    for devir in range(devir_sayisi):

        for paketler in mini_paket_al(x, y, paket_buyuklugu):

            x = paketler[0]
            y = paketler[1]
            m = y.size

            tahminler = x.dot(beta)
            beta_size = beta.size

            for i in range(beta_size):
                X_i = x[:, i]
                X_i.shape = (m, 1)

                hiz = momentum_sabiti * hiz - alfa * (1.0 / m) * ((tahminler - y) * X_i).sum()
                beta[i][0] = beta[i][0] + hiz

                if maliyet_fonksiyonu == 'mse':
                    maliyet_J[devir, 0] = mse_maliyet_fonksiyonu_hesapla(x, y, beta)
                if maliyet_fonksiyonu == 'mae':
                    maliyet_J[devir, 0] = mae_maliyet_fonksiyonu_hesapla(x, y, beta)
                if maliyet_fonksiyonu == 'rmse':
                    maliyet_J[devir, 0] = rmse_maliyet_fonksiyonu_hesapla(x, y, beta)
                if maliyet_fonksiyonu == 'squared_error':
                    maliyet_J[devir, 0] = squarred_error_maliyet_hesapla(x, y, beta)
    return beta, maliyet_J
