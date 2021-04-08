cmake_minimum_required(VERSION 3.17)
project(p02_montecarlo C)

set(CMAKE_C_STANDARD 99)

# Compiler flags
SET(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-pthread -O3")


add_executable(p02_montecarlo main.c)
