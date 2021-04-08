#!/usr/bin/env python3

import pandas
import matplotlib.pyplot as plt

JAVA_FILE = 'data_java.csv'
C_FILE = 'data_c.csv'
FIGS_DIR = 'figures'
MAX_TIME = 0


def plotgen(x, c, java, xlabel, title, figname, scale):
    plt.figure()
    plt.plot(x, c, '-o', label='C')
    plt.plot(x, java, '-s', label='Java')
    plt.xscale(scale)
    #plt.ylim([0, MAX_TIME])
    plt.xlabel(xlabel)
    plt.ylabel('EXEC_TIME')
    plt.legend()
    plt.title(title)
    plt.savefig(f'{FIGS_DIR}/{figname}')


if __name__ == '__main__':
    data_java = pandas.read_csv(JAVA_FILE)
    data_c = pandas.read_csv(C_FILE)

    data_per_points_c = data_c.groupby(['N_POINTS', 'N_THREADS'])
    data_per_threads_c = data_c.groupby(['N_THREADS', 'N_POINTS'])
    data_per_points_java = data_java.groupby(['N_POINTS', 'N_THREADS'])
    data_per_threads_java = data_java.groupby(['N_THREADS', 'N_POINTS'])

    MAX_TIME = max(data_java.max()['EXEC_TIME'], data_c.max()['EXEC_TIME'])

    points = data_c['N_POINTS'].unique()
    threads = data_c['N_THREADS'].unique()

    # generate plots per points java vs c
    for p in points:
        x1 = list()
        y_c = list()
        y_j = list()
        for t in threads:
            x1.append(t)
            y_c.append(data_per_points_c.get_group((p, t))['EXEC_TIME'].mean())
            y_j.append(data_per_points_java.get_group((p, t))['EXEC_TIME'].mean())
        plotgen(x1, y_c, y_j, 'N_THREADS', f'N_POINTS = {p}', f'{p}_points.png', 'linear')

    # generate plots per threads java vs c
    for t in threads:
        x2 = list()
        y_c = list()
        y_j = list()
        for p in points:
            x2.append(p)
            y_c.append(data_per_threads_c.get_group((t, p))['EXEC_TIME'].mean())
            y_j.append(data_per_threads_java.get_group((t, p))['EXEC_TIME'].mean())
        plotgen(x2, y_c, y_j, 'N_POINTS', f'N_THREADS = {t}', f'{t}_threads.png', 'log')
