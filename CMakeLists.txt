cmake_minimum_required(VERSION 3.10)
project(bloxburg-roblox-suite)

set(CMAKE_CXX_STANDARD 17)

add_executable(bloxburg-suite
    src/main.cpp
    src/game/Player.cpp
    src/game/Automation.cpp
)

target_include_directories(bloxburg-suite PRIVATE src)
target_link_libraries(bloxburg-suite PRIVATE RobloxAPI)