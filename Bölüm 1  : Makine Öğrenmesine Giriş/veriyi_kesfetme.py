import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

veri_seti = sns.load_dataset('tips')

print veri_seti.head()

print veri_seti.info()

print veri_seti.describe()

veri_seti.hist()
plt.show()


def bol_test_egitim(veri, oran):
    karisik_indeks = np.random.permutation(len(veri))
    test_buyuklugu = int(len(veri) * oran)
    test_indeksleri = karisik_indeks[:test_buyuklugu]
    egitim_indekleri = karisik_indeks[test_buyuklugu:]
    return veri.iloc[egitim_indekleri], veri.iloc[test_indeksleri]


egitim_seti, test_seti = bol_test_egitim(veri_seti, oran=0.2)

veri_seti.plot(x='total_bill', y='tip', kind='scatter')
plt.show()

sns.pairplot(veri_seti, hue='sex', palette='magma')
plt.show()

print veri_seti.corr()

print veri_seti.info()

del veri_seti['size']
del veri_seti['time']
del veri_seti['day']
del veri_seti['smoker']

print veri_seti.head()

print veri_seti['sex'].unique()

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
veri_seti['sex'] = label_encoder.fit_transform(veri_seti['sex'])

print veri_seti.head()
