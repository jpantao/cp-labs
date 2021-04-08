#!/bin/bash

ITEREATIONS="1000 10000 100000 1000000 10000000 100000000"
THREADS="1 2 4 8 16"
NRUNS="5"
OUT_FILE="data_java.csv"

echo 'N_POINTS,N_THREADS,EXEC_TIME' > $OUT_FILE
for IT in $ITEREATIONS; do
  for TH in $THREADS; do
    for R in $(seq 1 $NRUNS); do
      java -jar target/p01-montecarlo.jar -p $IT -t $TH
    done
  done
done >> $OUT_FILE