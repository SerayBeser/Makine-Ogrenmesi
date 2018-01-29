# coding=utf-8
""" Plotting Data
Veri Setinin Grafiginin Cizilmesi"""

import matplotlib.pyplot as plt
import numpy as np


def dagilim_grafigi(veri_seti):
    """

    :param veri_seti: Dagilim Grafiginin Yapilacagi Veri Seti
    """

    pos_veri = veri_seti[veri_seti['Admission'] == 1]
    neg_veri = veri_seti[veri_seti['Admission'] == 0]

    plt.figure()

    plt.plot(pos_veri['Exam1'], pos_veri['Exam2'], '+', markeredgecolor='black', markeredgewidth=2)
    plt.plot(neg_veri['Exam1'], neg_veri['Exam2'], 'o', markeredgecolor='black', markerfacecolor='yellow')
    plt.xlabel('Exam 1 Score')
    plt.ylabel('Exam 2 Score')
    plt.title('Dagilim Grafigi')
    plt.legend(['Admitted', 'Not admitted'])
    plt.show()


def hipotez_grafigi(X, y, teta):
    """

    :param X: Ongorucu Degiskenler, Sinav Notlari
    :param y: Hedef Degisken, Kabul Edilip Edilmedigi
    :param teta: Parametreler
    """

    pos_index = y.nonzero()[0]
    neg_index = (y == 0).nonzero()[0]

    plt.plot(X[pos_index, 0], X[pos_index, 1], '+', markeredgecolor='black', markeredgewidth=2)
    plt.plot(X[neg_index, 0], X[neg_index, 1], 'o', markeredgecolor='black', markerfacecolor='yellow')
    plt.xlabel('Exam 1 score')
    plt.ylabel('Exam 2 score')

    x_hipotez = np.array([X.min() - 2, X.max() + 2])
    y_hipotez = (-teta[0] - teta[1] * x_hipotez) / teta[2]

    plt.plot(x_hipotez, y_hipotez, color='blue')
    plt.legend(['Admitted', 'Not admitted'])
    plt.show()
