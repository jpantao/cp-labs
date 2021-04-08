#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <time.h>

#define RADIUS 1
#define SEED 0

long N_THREADS = 1;
long N_POINTS = 100000000;
long *RESULTS;


typedef struct thread_data {
    long points;
    long thread_id;
} thread_data;

void *calculate_sector(void *data) {
    thread_data *t_data = (thread_data *) data;
    unsigned int seed = time(0);

    long total = 0;
    for (long i = 0; i < t_data->points; i++) {
        double x = (double) rand_r(&seed) / ((double) RAND_MAX / RADIUS);
        double y = (double) rand_r(&seed) / ((double) RAND_MAX / RADIUS);
        if (x * x + y * y <= 1) total++;
    }
    RESULTS[t_data->thread_id] = total;

    pthread_exit(0);
}

long argparse(int argc, char *argv[]) {
    for (long i = 0; i < argc; i++)
        if (argv[i][0] == '-')
            switch (argv[i][1]) {
                case 't':
                    N_THREADS = atol(argv[++i]);
                    break;
                case 'p':
                    N_POINTS = atol(argv[++i]);
                    break;
                default:
                    fprintf(stderr, "Usage: %s [-option] [number]\n", argv[0]);
                    fprintf(stderr, "Option: -p [number-of-points]\n");
                    fprintf(stderr, "Option: -t [number-of-threads]\n");
                    exit(EXIT_FAILURE);
            }
    return 0;
}

/**
 * Assumptions:
 * 1. The number of points is even;
 * 2. The number of points is greater than the number of threads.
 *
 * @param argc
 * @param argv
 * @return
 */
int main(int argc, char *argv[]) {
    argparse(argc, argv);


    RESULTS = malloc(sizeof(long) * N_THREADS);

    pthread_t threads[N_THREADS];
    thread_data t_data[N_THREADS];
    long iterations = N_POINTS / N_THREADS;

    for (long i = 0; i < N_THREADS; i++) {
        t_data[i].points = iterations;
        t_data[i].thread_id = i;
        pthread_create(&threads[i], NULL, calculate_sector, &t_data[i]);
    }

    for (long i = 0; i < N_THREADS; i++)
        pthread_join(threads[i], NULL);

    double M = 0;
    for (long i = 0; i < N_THREADS; i++)
        M += (double) RESULTS[i];

    printf("Pi: %f\n", M / (double) N_POINTS * 4.0);
    free(RESULTS);

    return 0;
}
