#!/usr/bin/env python3

import subprocess
import time
import pandas
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar

TESTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
GENERATIONS = 100
THREADS = [1, 2, 4, 8, 16]
N_RUNS = 5
OUT_DIR = '../data/gameoflife'


def joint_plot(figname, title, *y_axis):
    plt.figure()
    for axis, label in y_axis:
        plt.plot(THREADS, axis, '-o', label=label)
    plt.xlabel('Number of threads')
    plt.ylabel('Execution time (s)')
    plt.legend()
    plt.title(title)
    # plt.show()
    plt.savefig(f'{OUT_DIR}/{figname}')


def process_experiment(data_file):
    dataframe = pandas.read_csv(data_file)
    dataframe = dataframe.groupby(['BOARD', 'N_THREADS'])

    results = dict()
    for board in TESTS:
        exec_times = list()
        for t in THREADS:
            exec_times.append(dataframe.get_group((board, t))['EXEC_TIME'].mean())
        results[board] = exec_times

    return results


def run_experiment(file, command):
    n_experiences = len(TESTS) * len(THREADS) * N_RUNS
    bar = IncrementalBar(command, max=n_experiences, suffix='%(percent)d%% - %(elapsed)ds')
    with open(file, 'w') as f:
        f.write(f'BOARD,N_THREADS,EXEC_TIME\n')
        for board in TESTS:
            for t in THREADS:
                for _ in range(N_RUNS):
                    start = time.time()
                    subprocess.run(f'{command} {GENERATIONS} ../p04-gameoflife/tests/{board}.in -q -t {t}', shell=True,
                                   stdout=subprocess.DEVNULL)
                    exec_time = time.time() - start
                    f.write(f'{board},{t},{exec_time}\n')
                    bar.next()
    bar.finish()


if __name__ == '__main__':
    # datafiles
    data_p04 = f'{OUT_DIR}/data_p04.csv'

    # run experiments and generate csv files
    print('Running experiments:')
    run_experiment(data_p04, f'../p04-gameoflife/p04_gameoflife')

    # process results
    print('Processing results...')
    results_p04 = process_experiment(data_p04)

    # generate plots
    print('Generating plots...')
    for test in TESTS:
        p04 = (results_p04[test], 'C OpenMp')
        joint_plot(f'test{test}_{GENERATIONS}generations.png', f'Test {test} - {GENERATIONS} generations', p04)
