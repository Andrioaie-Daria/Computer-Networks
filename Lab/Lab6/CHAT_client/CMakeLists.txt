cmake_minimum_required(VERSION 3.19)
project(CHAT_client)

link_libraries(ws2_32 wsock32)
set(CMAKE_CXX_STANDARD 14)

add_executable(CHAT_client main.cpp)