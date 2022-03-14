cmake_minimum_required(VERSION 3.19)
project(Problem1SumOfArray C)

set(CMAKE_C_STANDARD 99)

link_libraries(ws2_32 wsock32)

add_executable(Problem1SumOfArray server.c)