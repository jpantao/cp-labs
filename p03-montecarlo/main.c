#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define RADIUS 1

int N_THREADS = 1;
long N_POINTS = 100000000;

int argparse(int argc, char *argv[]) {
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

    double M = 0;

    double x, y;
    int i;
    omp_set_num_threads(N_THREADS);
    #pragma omp parallel for shared(N_POINTS) private(x, y, i) reduction(+:M) default(none)
    for(i = 0; i < N_POINTS; i++){
        x = (double) rand() / ((double) RAND_MAX / RADIUS);
        y = (double) rand() / ((double) RAND_MAX / RADIUS);
        if (x * x + y * y <= 1) M++;
    }

    printf("Pi: %f\n", M / (double) N_POINTS * 4.0);
    return 0;
}
