cmake_minimum_required(VERSION 3.19)
project(p03_openmp C)

set(CMAKE_C_STANDARD 99)

# Compiler flags
SET(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-pthread -O3 -fopenmp")

add_executable(p03_openmp main.c)