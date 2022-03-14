cmake_minimum_required(VERSION 3.19)
project(H1_commandExecution_c_server)

set(CMAKE_CXX_STANDARD 14)
link_libraries(ws2_32 wsock32)

add_executable(H1_commandExecution_c_server server.c)