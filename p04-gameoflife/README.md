# P04-gameoflife
Adaptation of the game of life program, present [here](https://bitbucket.org/joaomlourenco/game_of_life_seq/src/master/).

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
./p04_montecarlo
```

| Option         | Description                                               |
| -------------- | --------------------------------------------------------- |
| -q             | Quiet mode (only print the last generation's board)       |
| -p [PAUSE]     | Number of milliseconds to wait before printing each board |
| -t [N_THREADS] | Number of threads to use                                  |