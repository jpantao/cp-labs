# P00-montecarlo
Pi approximation by the Montecarlo method using **Kotlin's coroutines**.

**Compiling:**
```bash
./gradlew jar
```

**Running:**
```bash
java -jar build/libs/p00-montecarlo.jar 
```

| Option         | Description                  |
| -------------- | ---------------------------- |
| -p [N_POINTS]  | Number of points to generate |
| -t [N_THREADS] | Number of coroutines to use  |