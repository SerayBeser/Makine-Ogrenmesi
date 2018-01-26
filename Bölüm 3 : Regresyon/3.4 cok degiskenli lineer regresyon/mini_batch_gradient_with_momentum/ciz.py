# coding=utf-8
""" Plotting Data
Veri Setinin Grafiginin Cizilmesi"""

import matplotlib.pyplot as plt
import numpy as np


def maliyet_devir_grafigi_ciz(toplam_devir, mse, mae, squared_error, rmse, baslik):
    """

    :param toplam_devir: Toplam Devir Sayisi
    :param mse: Mean Squared Error
    :param mae: Mean Absolute Error
    :param squared_error: Squared Error
    :param rmse: Root Mean Squared Error
    :param baslik: Grafigin Basligi
    """
    fig = plt.figure(1)
    fig.suptitle(baslik)

    ax1 = fig.add_subplot(221)
    ax1.set_title("Mean Squarred Error")
    ax1.set_xlabel("Devir")
    ax1.set_ylabel("Maliyet Fonksiyonu")
    ax1.plot(np.arange(toplam_devir), mse, 'blue')

    ax2 = fig.add_subplot(222)
    ax2.set_title("Mean Absolute Error")
    ax2.set_xlabel("Devir")
    ax2.set_ylabel("Maliyet Fonksiyonu")
    ax2.plot(np.arange(toplam_devir), mae, 'red')

    ax3 = fig.add_subplot(223)
    ax3.set_title("Squarred Error")
    ax3.set_xlabel("Devir")
    ax3.set_ylabel("Maliyet Fonksiyonu")
    ax3.plot(np.arange(toplam_devir), squared_error, 'green')
    plt.tight_layout()

    ax4 = fig.add_subplot(224)
    ax4.set_title("Root Mean Square Error")
    ax4.set_xlabel("Devir")
    ax4.set_ylabel("Maliyet Fonksiyonu")
    ax4.plot(np.arange(toplam_devir), rmse, 'magenta')
    plt.tight_layout()

    fig.savefig(str(baslik).strip() + ".png")