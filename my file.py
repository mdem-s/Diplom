import pandas as pd
from datetime import datetime
from datetime import timedelta

def data(time, name):
    data2 = pd.read_csv(time, delimiter='-', encoding='ISO-8859-1’', on_bad_lines='warn', header=None)
    data2.columns = ['Start', 'Finish']
    data1 = pd.read_csv(name, encoding='ISO-8859-1’', on_bad_lines='warn', header=None)
    data1.columns = ['Name']
    data = pd.concat([data1, data2], axis=1)
    f = len(data)

    code = []
    s = ['push_right', 'approach_right', 'around_left', 'around_right', 'grooming',
         'sit', 'approach_left', 'push_left', 'feeder', 'approach_wallwithlever',
         'approach_feeder', 'around_feeder', 'around_wallwithlever', 'around_door', 'around_emptywall',
         'rearing_sup', 'rearing_nosup', 'walk', 'look_around', 'look_down']

    er=0
    for i in range(len(data)):
        er = 1
        for j in range(len(s)):
            if str(data['Name'][i]).strip() == s[j]:
                code.append(j+1)
                er = 0
                break
        if er == 1:
            print('error', i, data['Name'][i])

    data = pd.concat([data, pd.DataFrame({'code': code})], axis=1)
    duration = []

    for i in range(len(data)):
        x = datetime.strptime(str(data['Start'][i]).strip().split()[0], '%H:%M:%S.%f')
        y = datetime.strptime(str(data['Finish'][i]).strip().split()[0], '%H:%M:%S.%f')
        time_diff = - timedelta(hours=x.hour, minutes=x.minute, seconds=x.second, microseconds=x.microsecond) + timedelta(
        hours=y.hour, minutes=y.minute, seconds=y.second, microseconds=y.microsecond)
        duration.append(time_diff.total_seconds())
    data = pd.concat([data, pd.DataFrame({'duration': duration})], axis=1)

    time_start = []
    time_finish = []

    x = datetime.strptime(str(data['Start'][0]).strip().split()[0], '%H:%M:%S.%f')
    for i in range(len(data)):
        y = datetime.strptime(str(data['Start'][i]).strip().split()[0], '%H:%M:%S.%f')
        time_diff = - timedelta(hours=x.hour, minutes=x.minute, seconds=x.second,
                                microseconds=x.microsecond) + timedelta(hours=y.hour, minutes=y.minute,
                                                                        seconds=y.second, microseconds=y.microsecond)
        time_start.append(time_diff.total_seconds())

    for i in range(len(data)):
        y = datetime.strptime(str(data['Finish'][i]).strip().split()[0], '%H:%M:%S.%f')
        time_diff = - timedelta(hours=x.hour, minutes=x.minute, seconds=x.second,
                                microseconds=x.microsecond) + timedelta(hours=y.hour, minutes=y.minute,
                                                                        seconds=y.second, microseconds=y.microsecond)
        time_finish.append(time_diff.total_seconds())

    df = pd.DataFrame({'time_start': time_start, 'time_finish': time_finish})
    data = pd.concat([data, df], axis=1)

    if len(data) != f:
        print('ERROR')

    data = data[data['time_start']< 1200]

    return (data)

name = ['my_r1_f','my_r1_l','my_r2_f','my_r2_l','my_r3_f','my_r3_l',
        'my_m1_f','my_m1_l','my_m2_f','my_m2_l', 'my_m3_f','my_m3_l', 'my_m4_f','my_m4_l', 'my_m5_f','my_m5_l',]

for n in name:
    data1 = data('time_' + n + '.txt', 'name_' + n + '.txt')
    data1.to_csv(n + '.csv', index=None)

