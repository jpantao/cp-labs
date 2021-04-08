import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Main {

    private static final long RADIUS = 1;

    // defaults
    private static long N_POINTS = 100000000;
    private static int N_THREADS = 1;
    private static long[] RESULTS;


    private static void argparse(String[] args){
        for(int i = 0; i < args.length; i++)
            switch (args[i]){
                case "-t":
                    N_THREADS = Integer.parseInt(args[++i]);
                    break;
                case "-p":
                    N_POINTS = Long.parseLong(args[++i]);
                    break;
                default:
                    System.err.println("Unknown option");
            }

    }

    /**
     * Assumptions:
     * 1. The number of points is even;
     * 2. The number of threads is either one or a even number;
     * 2. The number of points is greater than the number of threads.
     *
     */
    public static void main(String[] args) throws InterruptedException {
        argparse(args);

        RESULTS = new long[N_THREADS];
        long sector = N_POINTS / N_THREADS;

        Thread[] threads = new Thread[N_THREADS];

        for(int i = 0; i < N_THREADS; i++) {
            int thread_id = i;
            (threads[i] = new Thread(() -> {
                long total = 0;
                for (long p = 0; p < sector; p++) {
                    double x = ThreadLocalRandom.current().nextDouble(RADIUS);
                    double y = ThreadLocalRandom.current().nextDouble(RADIUS);
                    if (x * x + y * y <= 1) total++;
                }
                RESULTS[thread_id] = total;
            })).start();
        }
        for (Thread t : threads) t.join();
        System.out.println("Pi: " + (double) Arrays.stream(RESULTS).sum() / N_POINTS * 4.0);

    }
}
