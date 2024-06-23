import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import os
import statistics

nodes = ['push_right', 'approach_right', 'around_left', 'around_right', 'grooming',
         'sit', 'approach_left', 'push_left', 'feeder', 'around_left', 'approach_wallwithlever',
         'approach_feeder', 'around_feeder', 'around_wallwithlever', 'around_door', 'around_emptywall',
         'rearing_sup', 'rearing_nosup', 'walk', 'look_around', 'look_down']
def graf(name):
    data = pd.read_csv( name + '.csv', encoding='ISO-8859-1’', on_bad_lines='warn')
    full_length = len(data)

    set_edg = [0] * 441
    for x in range(0, 441):
        set_edg[x] = [0] * 3

    # определяем список рёбер
    k = 0
    for i in range(0, 21):
        for j in range(0, 21):
            set_edg[k][0] = nodes[i]
            set_edg[k][1] = nodes[j]
            set_edg[k][2] = 0
            k += 1
    print(set_edg)

    n = 1
    for i in range(0, full_length - 1):
        k = 0
        for j in range(0, 441):
            if set_edg[j][0] == str(data['Name'][i]).strip() and set_edg[j][1] == str(data['Name'][i + 1]).strip():
                set_edg[j][2] += 1
                k = 1
        if k == 0:
            print(n, data['Name'][i], data['Name'][i + 1])
            n += 1

    sum_ = 0
    ed = 0
    edg = [0] * 441
    for x in range(0, 441):
        edg[x] = [0] * 3

    for j in range(0, 441):
        sum_ += set_edg[j][2]
        if set_edg[j][2] !=0:
            edg[ed] = set_edg[j]
            #print(name, '  set  ' , edg[ed])
            ed = ed + 1

    del edg[ed:441]
    ev = sum_/ed
    #print(sum_, full_length)
    #set_edg = ['n1', 'n2', 'weight'] + set_edg
    df = pd.DataFrame(edg)
    df.columns = ['n1', 'n2', 'weight']
    #print(name, '  df ', df)
    return(df, ed, ev)


rats = ['my_r1_f','my_r1_l','my_r2_f','my_r2_l','my_r3_f','my_r3_l',
        'r1_f','r1_l','r2_f','r2_l','r3_f','r3_l']
mice =  ['my_m1_f','my_m1_l','my_m2_f','my_m2_l', 'my_m3_f','my_m3_l', 'my_m4_f','my_m4_l', 'my_m5_f','my_m5_l',
        'm2_f', 'm2_l']

ed_rats_f = []
ed_rats_l = []
ed_mice_f = []
ed_mice_l = []

current_directory_path = os.getcwd()
k = 1
plt.figure(figsize=[20, 60])
plt.suptitle("Граф. Крысы \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 35, weight = 'extra bold')
for n in rats:
    df, ed, ev = graf(n)
    plt.subplot(6, 2, k)
    if (k%2) == 0:
        ed_rats_f.append(ed)
    else:
        ed_rats_l.append(ed)
    k = k + 1
    G = nx.MultiDiGraph(directed=True)  # создаём объект графа
    G = nx.from_pandas_edgelist(df, 'n1', 'n2', edge_attr='weight')
    G.add_nodes_from(nodes)
    plt.title(n + " \nКол-во ребер: " + str(ed) + "\nСредняя ширина ребра: " + str(round(ev,1)))
    # добавляем информацию в объект графа
    G.add_nodes_from(nodes)
    #G.add_edges_from(set_edg)
    # рисуем граф и отображаем его
    options = {
        'node_color': 'yellow',  # color of node
        'node_size': 100,  # size of node
        'arrows': True,
        'arrowstyle': '->',
        # 'width': 1,                 # line width of edges
        'edge_color': 'blue',  # edge color
    }
    edge_width = [1 * G[u][v]['weight'] for u, v in G.edges()]
    pos = nx.circular_layout(G)
    # nx.draw_networkx_nodes(G, pos,alpha= 0.5)
    # nx.draw_networkx_edges(G, pos,arrows=True)
    nx.draw_networkx(G, pos, with_labels=True, width=edge_width, alpha=0.5, **options)
    ax = plt.gca()
    ax.collections[0].set_edgecolor("#000000")
    current_directory_path = os.getcwd()

plot_name = 'graph_rats.svg'
plot_path = os.path.join(current_directory_path, plot_name)
plt.savefig(plot_path)
plt.savefig('graph_rats.png')

current_directory_path = os.getcwd()
k = 1
plt.figure(figsize=[20, 60])
plt.suptitle("Граф. Мыши \nПервый день серии экспериментов и Последний день обучения",
             fontsize = 35, weight = 'extra bold')
for n in mice:
    df, ed, ev = graf(n)
    plt.subplot(6, 2, k)
    if (k%2) == 0:
        ed_mice_f.append(ed)
    else:
        ed_mice_l.append(ed)
    k = k + 1
    G = nx.DiGraph(directed=True)  # создаём объект графа
    G = nx.from_pandas_edgelist(df, 'n1', 'n2', edge_attr='weight')
    G.add_nodes_from(nodes)
    plt.title(n + " \nКол-во ребер: " + str(ed) + "\nСредняя ширина ребра: " + str(round(ev,1)))
    # добавляем информацию в объект графа
    # G.add_nodes_from(nodes)
    # G.add_edges_from(set_edg)
    # рисуем граф и отображаем его
    options = {
        'node_color': 'yellow',  # color of node
        'node_size': 100,  # size of node
        'arrows': True,
        'arrowstyle': '->',
        # 'width': 1,                 # line width of edges
        'edge_color': 'blue',  # edge color
    }
    edge_width = [1 * G[u][v]['weight'] for u, v in G.edges()]
    pos = nx.circular_layout(G)
    # nx.draw_networkx_nodes(G, pos,alpha= 0.5)
    # nx.draw_networkx_edges(G, pos,arrows=True)
    nx.draw_networkx(G, pos, with_labels=True, width=edge_width, alpha=0.5, **options)
    ax = plt.gca()
    ax.collections[0].set_edgecolor("#000000")
    current_directory_path = os.getcwd()

plot_name = 'graph_mice.svg'
plot_path = os.path.join(current_directory_path, plot_name)
plt.savefig(plot_path)
plt.savefig('graph_mice.png')

print("Число ребер графа. Мыши день 1:", ed_mice_f, "    Среднее = ", statistics.mean(ed_mice_f), "    Медиана = ", statistics.median(ed_mice_f))
print("Число ребер графа. Мыши последний день", ed_mice_l, "    Среднее = ", statistics.mean(ed_mice_l), "    Медиана = ", statistics.median(ed_mice_l))
print("Число ребер графа. Крысы день 1", ed_rats_f, "    Среднее = ", statistics.mean(ed_rats_f), "    Медиана = ", statistics.median(ed_rats_f))
print("Число ребер графа. Крысы последний день", ed_rats_l, "    Среднее = ", statistics.mean(ed_rats_l), "    Медиана = ", statistics.median(ed_rats_l))