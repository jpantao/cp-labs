import java.util.concurrent.ThreadLocalRandom
import kotlinx.coroutines.*

var N_POINTS: Long = 1_000_000_000
var N_THREADS: Int = 50

fun argparse(args: Array<String>): Int {
    for (index in args.indices) {
        when (args[index]) {
            "-t" -> N_THREADS = args[index + 1].toInt()
            "-p" -> N_POINTS = args[index + 1].toLong()
        }
    }
    return 0;
}


fun main(args: Array<String>) {
    argparse(args)

    val results = (0 until N_THREADS).map{
        GlobalScope.async {
            var total = 0
            println(Thread.currentThread().name)
            for (i in 0..N_POINTS/N_THREADS) {
                val x = ThreadLocalRandom.current().nextDouble()
                val y = ThreadLocalRandom.current().nextDouble()
                if (x * x + y * y <= 1) total++
            }
            total
        }
    }

    runBlocking {
        val m = results.sumOf { it.await().toLong() }
        println("Pi : ${m / N_POINTS.toDouble() * 4}")
    }

}