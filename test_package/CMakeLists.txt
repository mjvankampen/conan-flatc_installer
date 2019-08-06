cmake_minimum_required(VERSION 2.8.11)

project(test_package CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(FlatBuffers MODULE REQUIRED)

build_flatbuffers("monster_test.fbs" flatbuffers_headers "" "${CMAKE_CURRENT_LIST_DIR}/generated/" "" "" "")

