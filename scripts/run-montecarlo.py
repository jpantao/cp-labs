#!/usr/bin/env python3

import subprocess
import time
import pandas
import matplotlib.pyplot as plt

ITERATIONS = [10000000, 100000000, 1000000000, 10000000000]
THREADS = [1, 2, 4, 8, 16]
N_RUNS = 5

OUT_DIR = "../observations/montecarlo"

def joint_plot(figname, title, *y_axis):
    plt.figure()
    for axis, label in y_axis:
        plt.plot(THREADS, axis, label=label)
    plt.xlabel('Number of threads')
    plt.ylabel('Execution time (s)')
    plt.legend()
    plt.title(title)
    # plt.show()
    plt.savefig(f'{OUT_DIR}/{figname}')


def process_experiment(data_file):
    dataframe = pandas.read_csv(data_file)
    dataframe = dataframe.groupby(['N_POINTS', 'N_THREADS'])

    results = dict()
    for p in ITERATIONS:
        exec_times = list()
        for t in THREADS:
            exec_times.append(dataframe.get_group((p, t))['EXEC_TIME'].mean())
        results[p] = exec_times

    return results


def run_experiment(file, command):
    with open(file, 'w') as f:
        f.write(f'N_POINTS,N_THREADS,EXEC_TIME\n')
        for it in ITERATIONS:
            for t in THREADS:
                for r in range(N_RUNS):
                    start = time.time()
                    subprocess.run(f'{command} -p {it} -t {t}', shell=True)
                    exec_time = time.time() - start
                    f.write(f'{it},{t},{exec_time}\n')


if __name__ == '__main__':
    # datafiles
    data_p01 = '{OUT_DIR}/data_p01.csv'
    data_p02 = '{OUT_DIR}/data_p02.csv'
    data_p03 = '{OUT_DIR}/data_p03.csv'

    # run experiments and generate csv files
    run_experiment(data_p01, 'java -jar ../p01-montecarlo/target/p01-montecarlo.jar')
    run_experiment(data_p02, '../p02-montecarlo/cmake-build-debug/p02_montecarlo')
    run_experiment(data_p02, '../p03-montecarlo/cmake-build-debug/p02_montecarlo')

    # process results
    results_p01 = process_experiment(data_p01)
    results_p02 = process_experiment(data_p02)
    results_p03 = process_experiment(data_p03)

    # generate plots
    for p in ITERATIONS:
        p01 = (results_p01[p], 'Java')
        p02 = (results_p02[p], 'C pthreads')
        p03 = (results_p03[p], 'C openmp') 
        joint_plot(f'nPoints_{p}.png', f'Number of points = {p}', p01, p02, p03)
