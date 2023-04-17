import math

import matplotlib.pyplot as plot
import numpy as np

# y=a*x^2+b*x+c

filename = 'test.txt'
with open(filename, 'r') as file:
    line = file.readline().split()
    if not len(line) == 4:
        raise AttributeError("Пустой список")
    else:
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])

r = 50
x = np.arange(-r, r, 1 / 100)  # [-49, -48, ... 47, 48, 49]
# y = a * (x ** 2) + b * x + c # 1 билет
y = a * np.arctan(b * x) + c  # 2 билет
# y = a * np.sin(x) + b  # 3 билет
# y = a * np.log10(x) + b  # 4 билет

# ls = supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plot.axvline(0, c='black', ls='solid')  # adding horizontal line in data co-ordinates
plot.axhline(0, c='black', ls='solid')  # adding vertical line in data co-ordinates

plot.grid()  # показать сетку
plot.title("Билет 1: y=a*x^2+b*x+c")  # название графика
plot.xlabel("ось x")  # x легенда
plot.ylabel("ось y")  # y легенда

# plot.xticks(np.arange(min(x), max(x), 1/10))
# plot.xticks(np.arange(1, 10, 1/100))

# ограничение размеров графика
# plot.ylim(-20, 20)
# plot.xlim(-20, 20)
plot.minorticks_on()

plot.plot(x, y)
plot.show()
