import pandas as pd
from datetime import datetime
from datetime import timedelta

#rat
def data(name):
    file1 = open(name, "r", encoding='utf-8-sig')
    name = []
    time = []
    start = []
    finish = []
    s=1
    while True:
        # считываем строку
        line = file1.readline()
        name.append(line.strip())
        line = file1.readline()
        #time.append(line.strip())
        start.append(line.strip().split("-")[0])
        #finish.append(line.strip().split("-")[1])
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        #print(name)
        #print(time)
    # закрываем файл
    file1.close

    #df = pd.DataFrame({'Start - Finish': time, 'd_name': name})
    #df = pd.DataFrame({'Start': start, 'Finish': finish, 'd_name': name})
    df = pd.DataFrame({'Start': start, 'd_name': name})
    l = len(df)
    df = df.drop(labels=[l-1])

    time = []
    x = datetime.strptime(str(df['Start'][0]).strip().split()[0], '%H:%M:%S.%f')
    for i in range(len(df) - 1):
        y = datetime.strptime(str(df['Start'][i + 1]).strip().split()[0], '%H:%M:%S.%f')
        time_diff = - timedelta(hours=x.hour, minutes=x.minute, seconds=x.second,
                                microseconds=x.microsecond) + timedelta(hours=y.hour, minutes=y.minute,
                                                                        seconds=y.second, microseconds=y.microsecond)
        time.append(time_diff.total_seconds())

    df = df.drop(labels=[l - 2])
    df = pd.concat([df, pd.DataFrame({'Time': time})], axis=1)
    print(len(df))
    df.to_csv('data.csv', index=None)
    #act = set(data['name'])
    #print(act)

    return (df)
def dasha_act_last(data):
    name=[]
    for i in range(len(data)):
        if str(data['d_name'][i]).strip() == 'подход к кормушке':
            name.append('approach_feeder')
        if str(data['d_name'][i]).strip() == 'сидит под правой педалью':
            name.append('look_down')
        if str(data['d_name'][i]).strip() == 'взаимодействие с педалью':
            name.append('around_wallwithlever')
        if str(data['d_name'][i]).strip() == 'подход к правой педали':
            name.append('approach_right')
        if str(data['d_name'][i]).strip() == 'грумминг':
            name.append('grooming')
        if str(data['d_name'][i]).strip() == 'ест':
            name.append('feeder')
        if str(data['d_name'][i]).strip() == 'взаимодействие с правой педалью':
            name.append('around_right')
        if str(data['d_name'][i]).strip() == 'нажатие на правую педаль':
            name.append('push_right')
        if str(data['d_name'][i]).strip() == 'нюхает у двери':
            name.append('around_door')
        if str(data['d_name'][i]).strip() == 'нажатие на левую педаль':
            name.append('push_left')
        if str(data['d_name'][i]).strip() == 'сидит в углу у кормушки??':
            name.append('around_feeder')
        if str(data['d_name'][i]).strip() == 'взаимодействие с левой педалью':
            name.append('around_left')
        if str(data['d_name'][i]).strip() == 'нос к педали':
            name.append('around_right')
        if str(data['d_name'][i]).strip() == 'подход к левой педали':
            name.append('approach_left')
        if str(data['d_name'][i]).strip() == 'нос над правой педалью':
            name.append('around_right')
        if str(data['d_name'][i]).strip() == 'поиск еды вне кормушки':
            name.append('look_down')
        if str(data['d_name'][i]).strip() == 'стойка с опорой':
            name.append('rearing_sup')
        if str(data['d_name'][i]).strip() == 'голова на педали':
            name.append('around_right')
        if str(data['d_name'][i]).strip() == 'умывание':
            name.append('grooming')
        if str(data['d_name'][i]).strip() == 'нос вверх':
            name.append('look_around')
        if str(data['d_name'][i]).strip() == 'стойка':
            name.append('rearing_nosup')
        if str(data['d_name'][i]).strip() == 'голова на левой педали':
            name.append('around_left')


    data = pd.concat([data, pd.DataFrame({'Name': name})], axis=1)

    return(data)
def dasha_act_first(data):
    name = []
    for i in range(len(data)):
        if str(data['d_name'][i]).strip() == 'передвижение по клетке':
            name.append('walk')
        elif str(data['d_name'][i]).strip() == 'поворот головы в сторону педалей':
            name.append('look_around')
        elif str(data['d_name'][i]).strip() == 'поворот головы у стенки с педалями':
            name.append('look_around')
        elif str(data['d_name'][i]).strip() == 'поворот головы от кормушки':
            name.append('look_around')
        elif str(data['d_name'][i]).strip() == 'подход к стене с педалями':
            name.append('approach_wallwithlever')
        elif str(data['d_name'][i]).strip() == 'подход к стенке с педалями':
            name.append('approach_wallwithlever')
        elif str(data['d_name'][i]).strip() == 'сидит у стены с педалями':
            name.append('around_wallwithlever')
        elif str(data['d_name'][i]).strip() == 'подход к кормушке':
            name.append('approach_feeder')
        elif str(data['d_name'][i]).strip() == 'сидит под правой педалью':
            name.append('look_down')
        elif str(data['d_name'][i]).strip() == 'взаимодействие с педалью':
            name.append('around_wallwithlever')
        elif str(data['d_name'][i]).strip() == 'нахождение у стенки с педалями':
            name.append('around_wallwithlever')
        elif str(data['d_name'][i]).strip() == 'подход к правой педали':
            name.append('approach_right')
        elif str(data['d_name'][i]).strip() == 'грумминг':
            name.append('grooming')
        elif str(data['d_name'][i]).strip() == 'ест':
            name.append('feeder')
        elif str(data['d_name'][i]).strip() == 'нос в кормушку':
            name.append('feeder')
        elif str(data['d_name'][i]).strip() == 'взаимодействие с правой педалью':
            name.append('around_right')
        elif str(data['d_name'][i]).strip() == 'нажатие на правую педаль':
            name.append('push_right')
        elif str(data['d_name'][i]).strip() == 'нюхает у двери':
            name.append('around_door')
        elif str(data['d_name'][i]).strip() == 'сидит у двери(нюхает)':
            name.append('around_door')
        elif str(data['d_name'][i]).strip() == 'нажатие на левую педаль':
            name.append('push_left')
        elif str(data['d_name'][i]).strip() == 'сидит в углу у кормушки??':
            name.append('around_feeder')
        elif str(data['d_name'][i]).strip() == 'сидит в углу у кормушки':
            name.append('around_feeder')
        elif str(data['d_name'][i]).strip() == 'поиск еды в кормушке':
            name.append('around_feeder')
        elif str(data['d_name'][i]).strip() == 'взаимодействие с левой педалью':
            name.append('around_left')
        elif str(data['d_name'][i]).strip() == 'нос к педали':
            name.append('around_right')
        elif str(data['d_name'][i]).strip() == 'подход к левой педали':
            name.append('approach_left')
        elif str(data['d_name'][i]).strip() == 'нос над правой педалью':
            name.append('around_right')
        elif str(data['d_name'][i]).strip() == 'поиск еды вне кормушки':
            name.append('look_down')
        elif str(data['d_name'][i]).strip() == 'стойка с опорой':
            name.append('rearing_sup')
        elif str(data['d_name'][i]).strip() == 'голова на педали':
            name.append('around_right')
        elif str(data['d_name'][i]).strip() == 'умывание':
            name.append('grooming')
        elif str(data['d_name'][i]).strip() == 'нос вверх':
            name.append('look_around')
        elif str(data['d_name'][i]).strip() == 'следит за тем, что происходит снаружи':
            name.append('look_around')
        elif str(data['d_name'][i]).strip() == 'стойка без опоры':
            name.append('rearing_nosup')
        elif str(data['d_name'][i]).strip() == 'стойка':
            name.append('rearing_nosup')
        elif str(data['d_name'][i]).strip() == 'голова на левой педали':
            name.append('around_left')
        elif str(data['d_name'][i]).strip() == 'нахождение у стенки с педалями(неподвижное)':
            name.append('sit')
        elif str(data['d_name'][i]).strip() == 'просто сидит':
            name.append('sit')
        elif str(data['d_name'][i]).strip() == 'взаимодействие с кормушкой':
            name.append('around_feeder')
        elif str(data['d_name'][i]).strip() == 'нос к кормушке':
            name.append('around_feeder')
        else:
            print('ERROR!!!!!!!', str(data['d_name'][i]).strip())
    data = pd.concat([data, pd.DataFrame({'Name': name})], axis=1)

    return (data)

def code(data):
    code = []
    s = ['push_right', 'approach_right', 'around_left', 'around_right', 'grooming',
         'sit', 'approach_left', 'push_left', 'feeder', 'approach_wallwithlever',
         'approach_feeder', 'around_feeder', 'around_wallwithlever', 'around_door', 'around_emptywall',
         'rearing_sup', 'rearing_nosup', 'walk', 'look_around', 'look_down']

    er = 0
    for i in range(len(data)):
        er = 1
        for j in range(len(s)):
            if str(data['Name'][i]).strip() == s[j]:
                code.append(j + 1)
                er = 0
                break
        if er == 1:
            print('error', i, data['Name'][i])

    data = pd.concat([data, pd.DataFrame({'code': code})], axis=1)
    return (data)

for i in ["первый день 1","первый день 2","первый день 3"]:
    data1 = data(i + ".txt")
    data1 = dasha_act_first(data1)
    data1 = code(data1)
    data1.to_csv(i + '.csv', index=None)

for i in ["стабильный навык 1","стабильный навык 2", "стабильный навык 3"]:
    data2 = data(i + ".txt")
    data2 = dasha_act_last(data2)
    data2 = code(data2)
    data2.to_csv(i + '.csv', index=None)

#mice
days = { 'm1_f' : [7,17,3,5,11,3,14,5,3,16,8,5,5,7,3,14,5,3,10,5,2,7,5,10,12,3,5,2,14,2,5,5,14,10,5,5,3,10,5,3,7,17,10,17,3,7,5,17,5,3,2,6,10,17,5,2,5,3,5,5,5,3,16,10,3,5,3,13,5,5,2,5,3,7,17,5,10,3,5,5,5,10,5,12,7,17,5,2,5,3,10,5,5,10,17,3,2,2,16,2,5,2,5,2,5,3,5,5,10,17,5,17,5,7,17,5,2,16,2,3,5,2,5,3,5,3,2,5,5,3,5,10,17,5,3,5,16,7,17,5,17,5,3,10,5,2,3,16,7,5,3,6,3,5,7,5,17,5,2,3,2,3,2,5,7,17,5,16,10,5,1,5,16,3,10,5,1,3,5,3,5],
'm2_f' : [7,17,10,17,3,5,7,17,10,17,5,3,7,3,10,7,5,6,10,5,7,5,2,10,5,17,3,3,1,7,17,10,5,17,10,2,5,7,17,3,5,3,5,3,7,5,10,5,2,3,14,2,7,3,3,2,10,17,3,5,7,5,5,8,3,5,10,3,5,3,2,3,7,7,10,17,3,5,3,7,17,5,3,5,5,7,5,10,5,2,2,3,16,7,17,10,17,3,5,5,3,5,6,5,7,5,10,17,7,17,3,5,3,5,7,17,5,10,5,7,17,5,3,5,3,5,5,3,5,16,2,10,2,1,1,2,5,5,3,6,10,5,5,7,5,5,3,5,3,6,5,3,6,5,7,5,3,6,10,17,5,7,6,3,5],
'm3_f' : [3,10,5,7,5,3,5,7,17,5,17,3,10,3,2,1,5,3,1,5,16,10,5,3,5,3,5,1,6,5,5,3,16,7,5,2,7,18,2,1,1,5,7,3,1,10,5,16,2,5,7,5,5,1,5,3,5,5,7,17,5,5,10,17,5,3,10,17,5,5,3,5,6,3,5,5,7,5,17,5,16,5,7,17,16,5,5,3,2,3,1,16,7,1,3,5,5,10,17,1,6,10,17,17,5,3,1,5,3,6,6,3,2,1,2,3,7,17,10,3,5,7,17,5,10,17,5,3,5,10,1,7,1,5,9,1,2,3,7,17,5,5,5,3,1,3,5,5,5,10,5,2,1,3,5,2],
'm4_f' : [7,17,5,10,17,1,5,3,14,3,1,6,1,5,7,5,2,5,10,5,7,5,3,1,1,3,1,3,1,7,5,3,5,6,5,6,6,5,1,2,5,10,5,10,17,7,10,11,5,7,8,3,2,3,2,7,2,6,2,5,3,6,6,5,10,12,7,5,7,17,3,16,2,16,7,5,2,3,5,2,5,2,5,5,3,7,17,2,10,17,5,2,17,2,7,8,5,2,3,1,16,2,5,6,2,10,5,17,2,7,5,5,3,10,17,2,7,8,5,2,17,2,3,10,17,2,17,2,7,2,17,5,2,16,5,10,11,12,5,17,2,16,2,7,8,9,5,2,5,3,16,10,2,3,2,7,2,3,10,2,11,2,7,8,2],
'm2_l' : [7,5,10,5,2,3,10,17,7,9,5,3,13,7,2,3,5,5,5,7,9,5,3,2,7,9,3,2,10,2,7,9,3,2,10,7,3,7,9,2,3,2,7,17,10,3,2,7,3,2,5,16,2,7,2,9,5,9,10,2,5,3,7,3,7,9,3,7,2,3,5,7,8,3,10,2,7,9,3,13,6,5,2,3,7,5,3,10,2,3,2,7,3,7,8,3,2,7,3,7,5,3,7,9,3,13,6,7,10,2,11,2,1,5,2,7,3,6,7,2,3,7,9,3,13,2,1,5,7,3,7,2,8,2,3,7,17,10,12,2,3,2,7,8,5,3,10,7,5,3,2,6,10,5,7,3,2,10,5,7,3,7,9,3,13,1,2,7,3,5,2,7,5,3,7,2,9,3,13,6,7,2,9,3,13,7,3,7,3,10,7,9,3,13,2,5,7,5,2,3,7,17,3,1,7,2,8,3,5,7,9,3,13,1,5,7,1,3,7,9,3,13,10,11,5,3,7,1,3,2,3,5,5,7,3,2,5,7,2,8,5,3,7,8,2,9,3,13,6,2,7,17,3,7,1,3,5,3,5,7,5,2,3,6,5,7,2,8,3,2,10,5,6,3,6,5,5,7,5,10,5,12,2,6,3,7,5,2,17,2],
'm1_pf' : [9,3,10,6,3,7,3,13,2,10,5,2,7,2,3,7,9,10,3,10,3,5,10,2,7,9,9,2,3,2,5,2,3,2,7,9,9,2,3,7,9,10,5,12,2,3,2,7,6,9,2,7,6,5,2,3,10,6,2,5,2,3,2,3,6,7,5,2,3,10,7,9,9,3,10,5,2,6,3,5,2,3,5,10,2,1,12,3,13,2,7,9,5,5,3,13,5,2,10,5,3,10,5,10,5,12,12,2,7,9,9,2,10,2,5,2,7,5,9,2,3,13,2,7,5,9,9,2,3,2,10,2,7,3,5,10,5,2,6,1,2,6,6,7,5,3,5,10,5,2,3,5,10,5,7,9,5,10,7,2,9,9,9,3,5,10,2,7,9,9,3,7,2,1,10,12,2,7,9,7,9,10,2],
'm2_pf' : [7,8,10,3,7,8,3,7,9,5,3,7,3,7,9,9,5,3,10,5,7,3,13,10,2,7,9,3,13,2,7,3,2,7,3,7,9,3,10,7,9,3,13,2,7,2,1,2,3,10,2,7,3,13,2,10,7,3,7,2,3,10,2,7,9,3,13,10,7,3,7,3,2,7,3,5,5,8,3,2,10,7,9,3,7,2,9,3,10,7,8,2,3,13,7,3,7,3,7,2,8,3,7,9,3,10,12,7,8,3,13,1,7,2,3,7,2,3,7,9,3,10,2,7,9,9,3,13,6,7,2,10,5,12,7,2,3,13,2,7,3,10,7,3,7,9,2,3,7,2,3,7,8,3,7,2,3,10,7,9,9,3,10,7,3,13,7,2,6,3,10,7,3,7,8,3,7,9,3,7,2,3,7,9,9,3,10,7,9,9,3,13,7,3,7,2,8,3,5,10,7,9,6,3,13,7,2,5,8,3,7,9,3,10,7,9,9,3,7,3,7,3,10,7,9,9,3,13,6,7,5,2,3,7,6,10,5,7,2,3,7,9,3,7,2,3,7,8,3,5,6,3,5,6,6,2,3,7,8,5,7,3,5,7,5,2,3,7,9,3,7,9,3,7,3,7,3,7,3,5,2,7,5,3,7,3,7,9,3,2,10,11,7,9,3,10,7,9,3,10,7,9,3,5,10,5,3,13],
'm3_pf' : [3,7,5,3,5,7,9,3,7,9,3,7,9,3,7,9,3,7,9,3,7,9,3,7,9,3,10,5,7,9,3,13,7,9,9,3,2,7,9,3,7,9,5,9,3,1,7,9,9,2,10,3,7,9,2,1,9,3,13,7,9,3,10,12,7,5,9,9,9,3,13,7,5,9,3,5,5,3,7,9,3,2,7,9,3,2,10,12,7,3,13,6,2,7,9,3,7,9,3,7,9,3,7,9,9,2,3,2,3,7,9,9,3,7,9,3,5,7,9,3,7,9,2,3,5,10,12,5,3,13,7,2,1,3,7,9,3,7,9,9,3,7,9,5,9,3,2,5,7,9,3,7,9,3,5,10,5,12,5,3,13,7,9,9,2,3,6,2,7,9,3,2,7,9,2,9,9,3,2,7,3,5,5,3,10,12,3,13,6,3,7,9,1,5,9,9,3,2,6,2,5,3,2,7,5,5,3,7,8,3,6,10,12,3,13,10,6,3,7,6,5,3,10,12,3,13,2,6,2,3,7,9,3,2,6,10,12,3,13,2,3,2,7,8,3,2,7,3,10,11,3,13,2,3,16,3,2,7,9,3,6,2,7,9,3,7,8,3,2,7,9,3,10,12,3,13],
'm4_pf' : [5,3,13,7,9,5,3,10,7,9,9,3,2,7,9,3,2,7,9,2,10,7,9,3,13,2,7,5,3,5,2,10,5,7,9,3,13,7,9,2,3,2,10,7,9,9,3,7,9,9,3,7,9,9,9,3,2,10,7,3,13,7,8,2,8,3,10,7,9,2,3,7,9,9,3,7,9,9,9,3,2,10,7,9,9,3,7,9,9,9,3,2,7,9,5,9,3,10,3,13,2,7,3,10,2,3,13,6,7,9,9,3,2,7,9,9,3,7,9,2,3,7,9,9,3,7,9,3,10,7,2,3,13,6,2,5,7,9,9,3,7,9,3,5,10,2,7,5,3,10,3,13,2,7,9,3,7,9,3,7,9,3,7,9,10,12,7,9,3,13,2,7,3,2,7,10,3,13,7,2,3,2,10,3,13,6,7,9,9,3,7,9,9,3,7,9,9,9,3,7,5,9,9,3,7,2,5,9,3,7,5,9,9,3,7,9,9,1,3,7,9,3,7,2,3,10,7,9,9,10,7,9,3,7,9,3,7,9,9,2,3,1,2,7,8,10,3,2,7,9,2,3,1,10,2,11,3,13],
'm1_pl' : [7,3,10,2,12,3,13,7,10,5,7,9,3,5,7,9,3,2,7,9,3,7,9,9,10,3,10,17,2,3,7,9,3,10,12,3,13,10,2,3,7,9,3,7,9,3,10,12,3,13,7,3,10,7,2,3,10,7,9,10,12,3,13,2,3,10,7,3,7,9,3,7,9,9,3,10,12,12,3,13,10,2,12,3,7,2,3,10,11,3,7,9,9,3,2,10,12,3,13,10,17,3,10,12,3,13,2,10,11,3,10,12,3,13,2,10,12,7,8,2,3,13,2,10,3,10,12,3,13,10,2,7,8,2,3,2,10,12,3,7,9,9,10,12,3,13,10,11,12,3,7,2,9,2,3,10,12,5,12,3,13,10,12,3,2,7,10,12,5,3,2,13,13,2,7,5,10,7,8,2,3,13,10,2,3,7,10,6,12,2,12,3,13,10,3,13,3,2,7,9,10,3],
'm2_pl' : [7,19,3,10,5,7,8,2,3,7,2,3,7,2,10,3,5,2,3,7,5,3,10,12,3,13,10,2,12,3,13,2,10,5,3,2,7,3,10,7,9,3,7,9,5,3,2,10,2,3,7,10,3,7,9,9,3,10,12,3,13,2,5,10,7,3,10,2,12,3,13,2,7,2,3,10,2,7,3,10,12,3,13,7,9,3,10,2,3,7,10,12,12,3,13,2,10,2,11,3,10,12,12,3,13,2,7,2,6,2,3,7,10,2,3,10,5,3,7,9,10,3,10,7,9,3,10,3,7,10,3,10,2,3,10,12,3,10,12,3,7,10,2,3,10,12,3,13,2,7,3,10,2,7,9,3,2,10,11,7,10,3,10,12,3,13,10,12,3,13,2,10,3,7,8,10,3,7,9,3,10,12,3,13,2,10,3,10,12,3,13,7,9,3,10,5,3,2,7,10,12,3,13,6,10,2,12,12,3,13],
'm3_pl' : [3,16,3,10,12,3,7,9,3,7,9,3,10,12,3,13,10,12,10,12,3,13,13,7,9,3,10,12,3,13,2,10,12,3,13,10,12,3,13,2,10,12,3,13,10,12,3,13,10,12,3,13,7,9,3,10,12,3,13,5,10,12,3,10,12,3,13,10,12,3,13,2,10,12,3,13,7,9,9,3,10,12,3,13,10,12,3,13,2,10,12,3,13,2,10,12,3,10,5,11,3,2,7,2,9,3,7,9,9,3,10,12,12,3,13,10,12,12,3,13,7,2,3,13,3,10,12,3,13,10,12,3,13,10,2,12,3,13,7,8,10,12,3,13,2,10,12,3,7,9,2,7,9,3,7,8,10],
'm4_pl' : [10,12,3,13,13,2,7,9,3,10,12,3,13,10,12,3,13,10,12,3,13,2,10,12,12,3,7,9,2,3,5,10,5,12,3,5,10,12,3,13,10,7,3,13,13,10,12,3,2,7,9,9,10,12,3,13,2,10,12,3,10,12,1,7,9,3,10,12,2,3,13,10,12,2,3,7,9,9,5,3,7,9,9,5,10,12,12,2,12,3,13,10,12,12,3,13,2,13,13,10,12,5,7,2,6,3,13,10,11,2,3,13,7,5,8,3,5,10,12,3,2,10,12,2,7,9,9,3,13,13,13,10,12,2,6,3,13,1,10,12,12,12,3,10,12,7,9,3,2,13,13,13,6,6,6,6,3,7,2,10,12,3,13,1]
         }
def dasha_act(data, key):
    data = data[key]
    name=[]
    for i in range(len(data)):
        if data[i] == 1:
            name.append('look_around')
        elif data[i] == 2:
            name.append('grooming')
        elif data[i] == 3:
            name.append('approach_feeder')
        elif data[i] == 4:
            name.append('rearing_nosup')
        elif data[i] == 5:
            name.append('rearing_sup')
        elif data[i] == 6:
            name.append('rearing_nosup')
        elif data[i] == 7:
            name.append('approach_left')
        elif data[i] == 8:
            name.append('around_left')
        elif data[i] == 9:
            name.append('push_left')
        elif data[i] == 10:
            name.append('approach_right')
        elif data[i] == 11:
            name.append('around_right')
        elif data[i] == 12:
            name.append('push_right')
        elif data[i] == 13:
            name.append('feeder')
        elif data[i] == 14:
            name.append('around_feeder')
        elif data[i] == 15:
            name.append('look_around')
        elif data[i] == 16:
            name.append('approach_wallwithlever')
        elif data[i] == 17:
            name.append('around_wallwithlever')
        elif data[i] == 18:
            name.append('look_around')
        elif data[i] == 19:
            name.append('around_right')
        elif data[i] == 20:
            name.append('around_left')
        else:
            print(key, i, data[i])

    if len(name) == len(data):
        df = pd.DataFrame({'Name': name, 'd_code': data})
    else:
        print('ERROR', data)
        df = pd.DataFrame({'Name': [], 'd_code': []})
    df = code(df)
    return (df)

for key in days.keys():
    df = dasha_act(days, key)

    df.to_csv( key +'.csv', index=None)

print(days.keys())

