import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics import tsaplots
from statsmodels.tsa.stattools import adfuller
from collections import Counter
def ftf_duration(data):
    k = 0
    duration = []
    for i in range(len(data)):
        if data.iloc[i, 3] == 9 or data.iloc[i, 3] == 12:
            if (data.iloc[i,5]-data.iloc[k,6])>1:
                duration.append((data.iloc[i, 5] - data.iloc[k, 6]).round(1))
                k = i
    return(duration)
def d_ftf_duration(data):
    k = 0
    duration = []
    for i in range(len(data)):
        if data.iloc[i, 4] == 9 or data.iloc[i, 4] == 12:
            if (data.iloc[i,2]-data.iloc[k,2])>1:
                duration.append((data.iloc[i-1, 2] - data.iloc[k, 2]).round(1))
                k = i
    return(duration)
def test_df(duration, name):
    #print('Результат теста:')
    df_result = adfuller(duration)
    # df_labels = ['ADF Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used']
    # for result_value, label in zip(df_result, df_labels):
    #     print(label + ' : ' + str(result_value))


    if df_result[1] <= 0.05:
        res = 'стационарный'
        #print(name, "Сильные доказательства против нулевой гипотезы, ряд является стационарным.")
    else:
        res = 'не стационарный'
        #print(name, "Слабые доказательства против нулевой гипотезы, ряд не является стационарным.")
    return(res)
def gr_ftf(duration, name):
    fig2 = plt.figure(figsize=(6, 4))
    # fig2.suptitle("day 1")
    fig2.suptitle(name)
    fig2.set_tight_layout(True)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')

    l = len(duration)
    av = sum(duration) / l

    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig2.add_subplot(111)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.savefig(name+'_time_ftf.png')
    # plt.show()
    print('Подходов к кормушке:', l)
def gr_autocor(duration, name):
    l = len(duration)
    # print(duration)
    # acor = sm.tsa.acf(duration, nlags= l-1)
    # acor = np.delete(acor, 0)
    # print(acor.max())
    plt.axis('off')
    fig = plt.figure(figsize=(6,4))
    ax1 = fig.add_subplot(211)
    fig = tsaplots.plot_acf(duration, lags= l-1, color='g', title='Autocorrelation function', ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = tsaplots.plot_pacf(duration, lags= l//2-1, color='g', title='Partial Autocorrelation function', ax=ax2)
    plt.savefig(name + '_autocor_time_ftf.png')
    # plt.show()
    return(l)

rats_mf = ['my_r1_f','my_r2_f','my_r3_f',]
rats_ml = ['my_r1_l','my_r2_l','my_r3_l']
rats_df = ['r1_f','r2_f','r3_f',]
rats_dl = ['r1_l','r2_l','r3_l']
mice_f =  ['my_m1_f','my_m2_f', 'my_m3_f', 'my_m4_f', 'my_m5_f']
mice_l =  ['my_m1_l','my_m2_l', 'my_m3_l', 'my_m4_l', 'my_m5_l']

av_rats_f = []
av_rats_l = []
av_mice_f = []
av_mice_l = []

fig = plt.figure(figsize=[10, 30])
plt.suptitle("Временной ряд подходов к кормушке. Крысы \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 15, weight = 'extra bold', va = 'bottom')  # + "\nЭнтропия = " + str(round(e, 3)))

res = []
k = 1
for n in rats_mf:
    data = pd.read_csv(n + '.csv')
    duration = ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(6, 2, k)
    plt.title(n + '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_rats_f.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(6, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2
for n in rats_df:
    data = pd.read_csv(n + '.csv')
    duration = d_ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(6, 2, k)
    plt.title(n + '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_rats_f.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(6, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2

print("Результаты теста Дики-Фуллера для крыс f: ", dict(Counter(res)))

res = []
k=2
for n in rats_ml:
    data = pd.read_csv(n + '.csv')
    duration = ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(6, 2, k)
    plt.title(n + '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_rats_l.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(6, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2
for n in rats_dl:
    data = pd.read_csv(n + '.csv')
    duration = d_ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(6, 2, k)
    plt.title(n + '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_rats_l.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(6, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2
plt.savefig('rats.svg')
plt.savefig('rats.png')
print("Результаты теста Дики-Фуллера для крыс l: ", dict(Counter(res)))




fig = plt.figure(figsize=[10, 25])
plt.suptitle("Временной ряд подходов к кормушке. Мыши \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 15, weight = 'extra bold', va = 'bottom')

res = []
k = 1
for n in mice_f:
    data = pd.read_csv(n + '.csv')
    duration = ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(5, 2, k)
    plt.title(n +  '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_mice_f.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(5, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2
print("Результаты теста Дики-Фуллера для мышей f: ", dict(Counter(res)))
res = []
k = 2
for n in mice_l:
    data = pd.read_csv(n + '.csv')
    duration = ftf_duration(data)
    res.append(test_df(duration, n))
    plt.subplot(5, 2, k)
    plt.title(n +  '\nРезультат теста Дики-Фуллера: ' + test_df(duration, n))
    fig.set_tight_layout(True)
    l = len(duration)
    av = sum(duration) / l
    av_mice_l.append(av)
    x = 1 + np.arange(l)
    y = [av] * (l)
    xt = np.arange(1, l - 1, 50)
    xt = np.append(xt, l)
    plt.axis('off')
    ax = fig.add_subplot(5, 2, k)
    ax.bar(x, duration, width=0.95, linewidth=0.7, color="#3d85c6")
    ax.set(xlim=(0, l + 1), xticks=xt, ylim=(0, max(duration)), yticks=[0, av, max(duration)])
    plt.plot(x, y, c="#db3226", linewidth=2.0)
    plt.ylabel('время')
    plt.xlabel('подход к кормушке')
    k = k + 2
print("Результаты теста Дики-Фуллера для мышей l: ", dict(Counter(res)))
plt.savefig('mice.svg')
plt.savefig('mice.png')

from scipy.stats import mannwhitneyu

# perform mann whitney test
def mw (batch_1, batch_2):
    stat, p_value = mannwhitneyu(batch_1, batch_2)
    print('Statistics=%.2f, p=%.2f' % (stat, p_value))
    # Level of significance
    alpha = 0.01
    # conclusion
    if p_value < alpha:
        print('Reject Null Hypothesis (Significant difference between two samples). p_value = ', p_value)
    else:
        print('Do not Reject Null Hypothesis (No significant difference between two samples). p_value = ', p_value)

print(av_rats_f, '    ' ,av_rats_l)
mw(av_rats_f, av_rats_l)
print(av_mice_f, '    ' ,av_mice_l)
mw(av_mice_f, av_mice_l)

    # gr_ftf(d, n)
    # gr_autocor(d, n)
