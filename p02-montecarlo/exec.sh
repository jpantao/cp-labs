#!/bin/bash

ITEREATIONS="1000 10000 100000 1000000 10000000 100000000"
THREADS="1 2 4 8 16"
NRUNS="5"
OUT_FILE="data_c.csv"

echo 'N_POINTS,N_THREADS,EXEC_TIME' > $OUT_FILE
for IT in $ITEREATIONS; do
  for TH in $THREADS; do
    for R in $(seq 1 $NRUNS); do
      ./cmake-build-debug/p02_montecarlo -p $IT -t $TH
    done
  done
done >> $OUT_FILE