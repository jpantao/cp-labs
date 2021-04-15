#!/usr/bin/env python3

import subprocess
import time
import pandas
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar

ITERATIONS = [10000000, 100000000, 1000000000, 10000000000]
THREADS = [1, 2, 4, 8, 16]
N_RUNS = 5

OUT_DIR = "../data/montecarlo"

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
    dataframe = dataframe.groupby(['N_POINTS', 'N_THREADS'])

    results = dict()
    for p in ITERATIONS:
        exec_times = list()
        for t in THREADS:
            exec_times.append(dataframe.get_group((p, t))['EXEC_TIME'].mean())
        results[p] = exec_times

    return results


def run_experiment(file, command):
    n_experiences = len(ITERATIONS) * len(THREADS) * N_RUNS
    bar = IncrementalBar(command.ljust(60), max = n_experiences, suffix='%(percent)d%% - %(elapsed)ds')
    with open(file, 'w') as f:
        f.write(f'N_POINTS,N_THREADS,EXEC_TIME\n')
        for it in ITERATIONS:
            for t in THREADS:
                for r in range(N_RUNS):
                    start = time.time()
                    subprocess.run(f'{command} -p {it} -t {t}', shell=True, stdout=subprocess.DEVNULL)
                    exec_time = time.time() - start
                    f.write(f'{it},{t},{exec_time}\n')
                    bar.next()
    bar.finish()


if __name__ == '__main__':
    # datafiles
    data_p00 = f'{OUT_DIR}/data_p00.csv'
    data_p01 = f'{OUT_DIR}/data_p01.csv'
    data_p02 = f'{OUT_DIR}/data_p02.csv'
    data_p03 = f'{OUT_DIR}/data_p03.csv'

    # run experiments and generate csv files
    print('Running experiments:')
    run_experiment(data_p00, 'java -jar ../p00-montecarlo/build/libs/p00-montecarlo.jar')
    run_experiment(data_p01, 'java -jar ../p01-montecarlo/target/p01-montecarlo.jar')
    run_experiment(data_p02, '../p02-montecarlo/p02_montecarlo')
    run_experiment(data_p03, '../p03-montecarlo/p03_montecarlo')
    
    # process results
    print('Processing results...')
    results_p00 = process_experiment(data_p00)
    results_p01 = process_experiment(data_p01)
    results_p02 = process_experiment(data_p02)
    results_p03 = process_experiment(data_p03)

    # generate plots
    print('Generating plots...')
    for p in ITERATIONS:
        p00 = (results_p00[p], 'Kotlin Coroutines')
        p01 = (results_p01[p], 'Java Threads')
        p02 = (results_p02[p], 'C pthreads')
        p03 = (results_p03[p], 'C OpenMP')
        joint_plot(f'{int(p/1000000)}M_points.png', f'{int(p/1000000)}M points', p00, p01, p02, p03)
