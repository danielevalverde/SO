import datetime
from time import sleep
import plotly.express as px
from matplotlib import pyplot, animation
import pandas

dicts = [
    dict(Task="A", Start=0, End=4, Time=4, Overload=False),
    dict(Task="B", Start=4, End=8, Time=4, Overload=False),
    dict(Task="B", Start=8, End=9, Time=1, Overload=True),
    dict(Task="C", Start=9, End=11, Time=2, Overload=False),
    dict(Task="B", Start=11, End=14, Time=3, Overload=False),
]
time = 0


def get_range_list(start, end, last):
    for i in range(last):
        if i <= start:
            yield start
        elif i <= end:
            yield i
        else:
            yield end

    # lst = [i if i < end else end for i in range(start, end)]
    # return lst


def get_index(i, start, end):
    if i <= start:
        return i
    elif i <= end:
        return i
    else:
        return end


def animate(i):
    global time
    default_color = 'blue'
    colors = []
    params = []
    left = list(map(lambda x: x.get('Start'), dicts))

    for dic in dicts:
        colors.append('red') if dic.get('Overload') is True else colors.append(default_color)

        if time <= dic.get('Start'):
            params.append(0)
        elif time <= dic.get('End'):
            params.append(time-dic.get('Start'))
        else:
            params.append(dic.get('Time'))

    time += 1

    pyplot.barh([dic.get('Task') for dic in dicts], params, left=left, color=colors)


def run():
    df = pandas.DataFrame(dicts)

    proj_start = df.Start.min()
    proj_end = df.End.max()

    df['start_num'] = df.Start - proj_start
    df['end_num'] = df.End - proj_start
    df['start_to_end'] = df.end_num - df.start_num

    fig = pyplot.figure()
    axes = fig.add_subplot()
    axes.set_xlim(0, proj_end+1)

    anim = animation.FuncAnimation(fig, animate, interval=1000)

    plotted = pyplot.show()
