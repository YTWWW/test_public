
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.pyplot import MultipleLocator

import numpy as np

test_data = np.array([np.array([  75.52, 72.3 , 67.8, 64.3 , 61.2 , 58,    55.5,  53.4,  51.5, 48.7, 47.1]),
                        np.array([75.52, 77.72, 73.4, 71.02, 69.77, 67.88, 65.37, 63.97, 62, 60.65, 59.09]),  
                        np.array([75.52, 74.72, 70.4, 68.02, 64.77, 60.88, 60.37, 58.97, 57, 55.65, 50.09])
                        ])

def draw_top1_accu(data, label_name, line_color, fill_color):
    '''
    data size: [3, N]-----[[data_past], [data_new], [data_avg]]
    '''

    data_seqLength = data.shape[1]

    fig, ax = plt.subplots()

    x = np.arange(0,data_seqLength,1)
    past = data[0]/100
    new = data[1]/100
    avg = data[2]/100

    plt.grid(linestyle="-.")  # 设置背景网格线为虚线

    ax.plot(x, past, linewidth=2, linestyle=":", color=line_color)
    ax.plot(x, new, linewidth=2, linestyle="--", color=line_color)
    ax.plot(x, avg, linewidth=2, linestyle="-", marker='8', color=line_color)
    plt.fill_between(x,new,past,where=(new>past)&(past>new)|(x>=0),facecolor=fill_color, alpha=1)

    # 设置x，y轴范围
    plt.xlim(0, data_seqLength-0.7)
    plt.ylim(0, 1)
    # 设置y轴百分比显示
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
    # 设置x轴间隔
    x_major_locator=MultipleLocator(1)
    ax.xaxis.set_major_locator(x_major_locator)

    # 设置label
    plt.plot(-1,-1,label=label_name, linestyle='-', color=line_color)
    plt.legend(loc=1)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('Incremental state', fontsize=15)
    plt.ylabel('Top-1 accuracy', fontsize=15)
    plt.show()


draw_top1_accu(test_data, label_name='labelname', line_color='orange', fill_color='moccasin')
