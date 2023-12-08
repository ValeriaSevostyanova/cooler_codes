import matplotlib.pyplot as plt
import numpy as np

import random

n = random.randint(1, 25) # необходимо поменять на кол-во кулеров менять
species = [str(i) for i in range(1, n + 1)] # запонение айди (нужно для графика) не менять
penguin_means = {
    'Water': [random.randint(1, 100) for _ in range(n)], # данные из таблицы (в процентах) менять
    'Cups': [random.randint(1, 100) for _ in range(n)],  # данные из таблицы (в процентах) менять
}

x = np.arange(len(species)) # кол-во делений по Оx не менять
width = 0.32 # ширина столбчатых диаграмм не менять (по желанию)
multiplier = 0 # ну это просто переменная она пригодится в цикле
fig, ax = plt.subplots(layout='constrained') # фигура и оси диаграммы не менять

for attribute, measurement in penguin_means.items(): # создаем столбчатые диаграммы не менять
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, align='edge') # устанавливаем с помощью align выравнивание диаграммам 
    ax.bar_label(rects, padding=1) #                                                чтобы они не вылезали за границы
    multiplier += 1


ax.set_ylabel('Percent') # названия устанавливаем
ax.set_xlabel('ID') #      тут тоже

ax.set_xticks(x + width, species) # расстояние между двумя разными диаграммами (по айди разными)
ax.legend(loc='upper right', ncols=3) # устанавливаем надпись cups и water (показываем что каким цветом обозначаем)
ax.set_ylim(0, 100) # предел по у
ax.set_xlim(0, n)   # предел по х

plt.savefig('result.png') # сохраняем диаграммы в файл result.png
#plt.show() # показываем диаграммы (можно и не показывать)
