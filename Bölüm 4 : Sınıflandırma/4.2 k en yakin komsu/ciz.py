# coding=utf-8
""" Plotting Data
Veri Setinin Grafiginin Cizilmesi"""

import matplotlib.pyplot as plt


def dagilim_grafigi(veri_seti):
    """

    :param veri_seti: Dagilim Grafiginin Yapilacagi Veri Seti
    """

    setosa = veri_seti[veri_seti['Class'] == 'Iris-setosa']
    versi = veri_seti[veri_seti['Class'] == 'Iris-versicolor']
    virginica = veri_seti[veri_seti['Class'] == 'Iris-virginica']

    plt.figure()

    plt.plot(setosa['SepalLength'], setosa['SepalWidth'], 'o', markeredgecolor='red', markerfacecolor='red')
    plt.plot(versi['SepalLength'], versi['SepalWidth'], 'o', markeredgecolor='green', markerfacecolor='green')
    plt.plot(virginica['SepalLength'], virginica['SepalWidth'], 'o', markeredgecolor='blue', markerfacecolor='blue')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Dagilim Grafigi')
    plt.legend(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    plt.show()


def hipotez_grafigi(egitim_seti, test_seti):
    """

    :param egitim_seti: Dagilim Grafiginin Yapilacagi Veri Seti
    """
    plt.figure()

    # test setinin gorsellestirilmesi
    setosa_ = test_seti[test_seti['Prediction'] == 'Iris-setosa']
    versi_ = test_seti[test_seti['Prediction'] == 'Iris-versicolor']
    virginica_ = test_seti[test_seti['Prediction'] == 'Iris-virginica']

    plt.plot(setosa_['SepalLength'], setosa_['SepalWidth'], 'o', markeredgecolor='black', markerfacecolor='red',
             markeredgewidth=3)
    plt.plot(versi_['SepalLength'], versi_['SepalWidth'], 'o', markeredgecolor='black', markerfacecolor='green',
             markeredgewidth=3)
    plt.plot(virginica_['SepalLength'], virginica_['SepalWidth'], 'o', markeredgecolor='black', markerfacecolor='blue',
             markeredgewidth=3)

    # egitim setinin gorsellestirilmesi
    setosa = egitim_seti[egitim_seti['Class'] == 'Iris-setosa']
    versi = egitim_seti[egitim_seti['Class'] == 'Iris-versicolor']
    virginica = egitim_seti[egitim_seti['Class'] == 'Iris-virginica']

    plt.plot(setosa['SepalLength'], setosa['SepalWidth'], 'o', markeredgecolor='red', markerfacecolor='red')
    plt.plot(versi['SepalLength'], versi['SepalWidth'], 'o', markeredgecolor='green', markerfacecolor='green')
    plt.plot(virginica['SepalLength'], virginica['SepalWidth'], 'o', markeredgecolor='blue', markerfacecolor='blue')

    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Hipotez Grafigi')
    plt.legend(['Test Iris-setosa', 'Test Iris-versicolor', 'Test Iris-virginica', 'Iris-setosa', 'Iris-versicolor',
                'Iris-virginica'])

    plt.show()
