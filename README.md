my_m1, ..., my_m5, my_r1, my_r2, my_r3 - данные разметки видео мышей (m) и крыс (r), обученных Машей 
m2, r1, r2, r3  - данные разметки видео мышей (m) и крыс (r), обученных Дашей 
 
_f - first day
_l  - last day

колонки датафрейма: 
['Start', 'Finish', 'Name', 'code', 'duration', 'time_start', 'time_finish']
'Start', 'Finish' - время '%H:%M:%S.%f'
 'Name', 'code' - имя и код пов акта
	Поведенческие акты (код - расположение элемента в массиве начиная с 1)
	s = ['push_right', 'approach_right', 'around_left', 'around_right', 'grooming',
         	'sit', 'approach_left', 'push_left', 'feeder', 'approach_wallwithlever',
         	'approach_feeder', 'around_feeder', 'around_wallwithlever', 'around_door', 'around_emptywall',
         	'rearing_sup', 'rearing_nosup', 'walk', 'look_around', 'look_down']

'duration', 'time_start', 'time_finish' - длительность, время начала и окончания  в секундах


create_csv — (create csv file from txt file) - подготовка данных,
main — time series (analysis period between being at the feeder) - анализ временных рядов, 
graph (create behavior graph) - граф поведения, 
coordinaresftf (matrix cos sim) - косинусное сходство: матрица
