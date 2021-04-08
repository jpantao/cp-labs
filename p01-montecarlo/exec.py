#!/usr/bin/env python3

import subprocess
import time

ITERATIONS = [1000, 10000, 100000, 1000000, 10000000, 100000000]
THREADS = [1, 2, 4, 8, 16]
N_RUNS = 5
COMMAND = 'java -jar target/p01-montecarlo.jar'
OUT_FILE = 'data_java.csv'

if __name__ == '__main__':

    with open(OUT_FILE, 'w') as f:
        f.write(f'N_POINTS,N_THREADS,EXEC_TIME\n')
        for it in ITERATIONS:
            for t in THREADS:
                for r in range(N_RUNS):
                    start = time.time()
                    subprocess.run(f'{COMMAND} -p {it} -t {t}', shell=True)
                    exec_time = time.time() - start
                    f.write(f'{it},{t},{exec_time}\n')

