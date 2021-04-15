# P02-montecarlo
Pi approximation by the Montecarlo method using **C pthreads**.

**Compiling:**
1. Generate the makefile
```bash
cmake CMakeLists.txt
```
2. Generate the executable file
```bash
make
```

**Running:**
```bash
./p02-montecarlo
```

| Option         | Description                   |
| -------------- | ----------------------------- |
| -p [N_POINTS]  | Number of points to generate  |
| -t [N_THREADS] | Number of threads to use      |