cmake_minimum_required(VERSION 3.19)
project(p03_montecarlo C)

set(CMAKE_C_STANDARD 99)

# Compiler flags
set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-fopenmp -O3")


add_executable(p03_montecarlo main.c)
