cmake_minimum_required(VERSION 3.19)
project(p04_gameoflife C)

set(CMAKE_C_STANDARD 99)

set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-fopenmp -O3 -lpcre -ansi -pedantic")

add_library(mem mem.c)
add_library(game game.c)
add_library(config config.c)

target_link_libraries(game mem)
target_link_libraries(config mem)

add_executable(p04_gameoflife main.c)
target_link_libraries(p04_gameoflife game)
target_link_libraries(p04_gameoflife config)
