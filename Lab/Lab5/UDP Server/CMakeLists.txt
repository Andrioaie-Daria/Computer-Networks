cmake_minimum_required(VERSION 3.19)
project(UDP_Server)
link_libraries(ws2_32 wsock32)
set(CMAKE_CXX_STANDARD 14)


add_executable(UDP_Server main.cpp)