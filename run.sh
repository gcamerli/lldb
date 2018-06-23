#!/bin/sh
# ./run.sh

# Compile the .cpp file
clang++ -Wall -g test/source.cpp -o example

# Execute lldb with the binary example
lldb -- example
