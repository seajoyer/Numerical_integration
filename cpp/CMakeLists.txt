cmake_minimum_required(VERSION 3.10)
project(numerical_integration_example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_executable(numerical_integration_example
    src/main.cpp
)

# Copy gnuplot script to build directory
configure_file(
    ${CMAKE_SOURCE_DIR}/scripts/plot_errors.gnu
    ${CMAKE_BINARY_DIR}/scripts/plot_errors.gnu
    COPYONLY
)

# Create scripts directory in build directory
add_custom_command(
    TARGET numerical_integration_example POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory
    ${CMAKE_BINARY_DIR}/scripts
)

# Copy gnuplot script after build
add_custom_command(
    TARGET numerical_integration_example POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/scripts/plot_errors.gnu
    ${CMAKE_BINARY_DIR}/scripts/plot_errors.gnu
)
