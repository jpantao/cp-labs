# cp-labs
This repository contains some examples from my concurrency and parallelization course and is organized as follows:


```
.                    
├── data             # experiment data and reports
├── p00-montecarlo   # pi approximation by the montecarlo method (Kotlin - Coroutines)
├── p01-montecarlo   # pi approximation by the montecarlo method (Java - Threads)
├── p02-montecarlo   # pi approximation by the montecarlo method (C - pthread)
├── p03-openmp       # pi approximation by the montecarlo method (C - OpenMP)
├── scripts          # scripts to run the experiments
├── LICENSE
└── README.md        # this file
```

The **data** directory contains the data and evaluations of each experiment specifying the environment
in which they were performed.
The scripts to execute these experiments can be found in the **scripts** directory and the executable
files that were used are also provided along with the code. Note that the scripts take into consideration
the location of the executable files and they are meant to be executed from within the **scripts** directory. 

If you want to compile them by yourself there are instructions on how to do it in the **README** of the project's directory.

#### **Experiments:**

- Pi approximation by the Montecarlo method performance comparison ([data/montecarlo/README.md](./data/montecarlo/README.md));
- TODO: Game of Life.
