# coding=utf-8
""" Gradient Descent
 Dereceli Fonksiyon """

from sigmoid import sigmoid
import numpy as np


def dereceli_fonksiyon(theta, X, y):
    """

    :param theta:
    :param X:
    :param y:
    :return: gradyan
    """
    m = X.shape[0]
    h = sigmoid(X.dot(theta))
    cost = sum(-y * np.log(h) - (1.0 - y) * np.log(1.0 - h))
    grad = X.T.dot(h - y)
    return grad / m
