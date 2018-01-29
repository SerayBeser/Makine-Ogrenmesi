# coding=utf-8
""" Compute Cost Function
 Maliyet Fonksiyonunu Hesapla"""

import numpy as np
from sigmoid import sigmoid


def maliyeti_hesapla(theta, X, y):
    """

    :param theta:
    :param X:
    :param y:
    :return: maliyet
    """
    m = X.shape[0]
    h = sigmoid(X.dot(theta))
    cost = sum(-y * np.log(h) - (1.0 - y) * np.log(1.0 - h))
    return cost / m
