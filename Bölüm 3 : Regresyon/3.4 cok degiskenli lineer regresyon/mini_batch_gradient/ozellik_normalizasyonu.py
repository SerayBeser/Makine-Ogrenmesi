# coding=utf-8
""" Feature Normalization
 Ozellik Normalizasyonu"""
import numpy as np


def ozellik_normalizasyonu(x):
    """

    :param x: normallestirilecek ozellikler
    :return: normalize olmus X, ortalamasi ve sapmasi
    """
    butun_ortalamalar = []
    butun_standart_sapmalar = []
    X_normalize = x

    n_c = x.shape[1]
    for i in range(n_c):
        m = np.mean(x[:, i])
        s = np.std(x[:, i])

        butun_ortalamalar.append(m)
        butun_standart_sapmalar.append(s)
        X_normalize[:, i] = (X_normalize[:, i] - m) / s

    return X_normalize, butun_ortalamalar, butun_standart_sapmalar