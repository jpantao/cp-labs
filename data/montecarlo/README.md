# Pi approximation using the Montecarlo method

In the root of this repository you can find **p01-montecarlo**, 
**p02-montecarlo**, and **p03-montecarlo** which are implementations of 
the Montecarlo method to approximate Pi using different approaches to 
parallelization. This document presents a performance comparison between 
them.


#### **Implementation details:**
- **p01-montecarlo**, Java implementation;
- **p02-montecarlo**, C implementation using pthreads;
- **p03-montecarlo**, C implementation using OpenMP;


#### **Environment**:
```
OS          Arch Linux x86_64 
Host        XPS 13 9380 
Kernel      5.11.12-arch1-1 
CPU         Intel i7-8565U @ 4.600GHz 
Cores       4
Threads     8
Memory      16GB DD3
```

#### **Parameters:**
The experiment consisted in averaging the execution times of 5 runs for 
each combination of number of threads and points to generate.

The numbers of threads used were **1**, **2**, **4**, **6**, **8**, and **16**.

The numbers of points to generate were **10 M**, **100 M**, **1 000 M**, **10 000 M**.



#### **Results:**
![10M](nPoints_10000000.png =250x "10 M")


#### **Conclusions:**