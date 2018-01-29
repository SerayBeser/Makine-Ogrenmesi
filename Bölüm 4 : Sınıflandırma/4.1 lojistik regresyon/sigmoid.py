# coding=utf-8
""" Sigmoid
Sigmoid """

import numpy as np


def sigmoid(z):
    """

    :param z: veri
    :return: sigmoid fonksiyonu

    >> sigmoid(0) == 0.5
    """
    return 1.0 / (1.0 + np.exp(-z))
