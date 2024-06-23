import pandas as pd
import numpy as np
from numpy.linalg import norm
import seaborn
import matplotlib.pyplot as plt
from functools import reduce
import math
import os
from collections import Counter
def set(full):
    #print(full)
    # длина массива
    full_length=len(full)
    #print('Всего актов:',full_length)
    # массив векторов
    set_of_vectors =[0] * 400
    for x in range(0, 400):
        set_of_vectors[x] = [0]*22
    # колличество векторов
    j=0

    # разделение массива на векторы
    i=0
    while i < full_length-1:
        #print( full['code'][i])

        if i==0 and full['code'][i] not in [9, 12]:
            while i < full_length - 1 and (full['code'][i] not in [9, 12]):
                #print('1) ',full['code'][i])
                set_of_vectors[j][full['code'][i]] = 1
                i += 1
                # print(i, full['code'][i])
            j += 1

        if full['code'][i] in [9, 12]:
            while i < full_length - 1 and (full['code'][i] in [9, 12]):
                #print('2.1) ',full['code'][i])
                set_of_vectors[j][full['code'][i]] = 1
                i += 1
            while i < full_length - 1 and (full['code'][i] not in [9, 12]):
                #print('2.2) ',full['code'][i])
                set_of_vectors[j][full['code'][i]] = 1
                i += 1
            j += 1
    del set_of_vectors[j:400]
    return (set_of_vectors)
def cos_sim(set_of_vectors):

    j = len(set_of_vectors)
    cosine_sim = [0] * j
    for x in range(0, j):
        cosine_sim[x] = [0] * j

    for i in range(0, j):
        for k in range(0, j):
            cosine = np.dot(set_of_vectors[i], set_of_vectors[k]) / (norm(set_of_vectors[i]) * norm(set_of_vectors[k]))
            cosine_sim[i][k] = (cosine)
    return(cosine_sim)

rats = ['my_r1_f','my_r1_l','my_r2_f','my_r2_l','my_r3_f','my_r3_l',
        'r1_f','r1_l','r2_f','r2_l','r3_f','r3_l']
mice =  ['my_m1_f','my_m1_l','my_m2_f','my_m2_l', 'my_m3_f','my_m3_l', 'my_m4_f','my_m4_l', 'my_m5_f','my_m5_l',
        'm2_f', 'm2_l']

current_directory_path = os.getcwd()
k = 1

plt.figure(figsize=[30, 40])
plt.suptitle("Матрица косинусного сходства. Крысы \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 20, weight = 'extra bold')

for n in rats:
    data = pd.read_csv(n + '.csv')
    set_of_vectors = set(data)
    cosine_sim = cos_sim(set_of_vectors)
    df = pd.DataFrame(cosine_sim)
    plt.subplot(6, 4, k )
    k=k+1
    plt.title(n)
    hmap = seaborn.heatmap(df, center=0, square=True)
    plt.ylabel('Акты между взаимодействиями с кормушкой', fontsize = 8)
    plt.xlabel('Акты между взаимодействиями с кормушкой', fontsize = 8)
    dist = sum(map(Counter, np.array(cosine_sim).round(1)), Counter())
    plt.subplot(6, 4, k)
    plt.bar(dist.keys(), dist.values(), width=0.1, )
    plt.xticks(np.arange(0, 1, step=0.1))
    plt.xlim(-0.1, 1.1)
    plt.ylabel('Частота значения', fontsize=8)
    plt.xlabel('Значение', fontsize=8)
    k = k + 1
    print(k)

plot_name = 'matrixcossim_rats.svg'
plot_path = os.path.join(current_directory_path, plot_name)
plt.savefig(plot_path)
plt.savefig('matrixcossim_rats.png')


plt.figure(figsize=[30, 40])
plt.suptitle("Матрица косинусного сходства. Мыши \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 20, weight = 'extra bold', va = 'bottom')  # + "\nЭнтропия = " + str(round(e, 3)))

k = 1
for n in mice:
    data = pd.read_csv(n + '.csv')
    set_of_vectors = set(data)
    cosine_sim = cos_sim(set_of_vectors)
    df = pd.DataFrame(cosine_sim)
    plt.subplot(6, 4, k)
    k=k+1
    plt.title(n)
    hmap = seaborn.heatmap(df, center=0, square=True)
    plt.ylabel('Акты между взаимодействиями с кормушкой', fontsize = 8)
    plt.xlabel('Акты между взаимодействиями с кормушкой', fontsize = 8)
    dist = sum(map(Counter, np.array(cosine_sim).round(1)), Counter())
    plt.subplot(6, 4, k)
    plt.bar(dist.keys(), dist.values(), width=0.1,)
    plt.xticks(np.arange(0, 1, step=0.1))
    plt.xlim(-0.1, 1.1)
    plt.ylabel('Частота значения', fontsize=8)
    plt.xlabel('Значение', fontsize=8)
    k = k + 1

plot_name = 'matrixcossim_mice.svg'
plot_path = os.path.join(current_directory_path, plot_name)
plt.savefig(plot_path)
plt.savefig('matrixcossim_mice.png')

entropy = lambda df:-reduce( #4.reduce создает одно значение из всех элементов массива.
    lambda x,y:x+y,#5.Складываем значения энтропии, полученные из индивидуальных значений (9,5).
    map( #2.Преобразовываем число (9,5) частотного массива (["○": 9, "×": 5]) в энтропию согласно следующему лямбда-выражению
        lambda x:(x/len(df))*math.log2(x/len(df)),#3.Вычисляем P(E)log2(P(E))
        df.iloc[:,-1].value_counts() #1.Частота последнего столбца DataFrame（например:["○":9,"×":5]）
    )
)
