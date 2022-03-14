cmake_minimum_required(VERSION 3.19)
project(Problema2CountOfSpaces)

set(CMAKE_CXX_STANDARD 14)
link_libraries(ws2_32 wsock32)

add_executable(Problema2CountOfSpaces main.cpp)