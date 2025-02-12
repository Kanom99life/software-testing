#!/bin/bash

# echo "Remove old files"
rm -rf result.txt __pycache__ .pytest_cache .coverage test_mid*.xml

# for i in `seq 1 3`; do
#     echo "Running test cases in $i"
#     sleep 1
# done

for i in {1..6}; do
    pytest test_mid.py::test_mid$i --cov --cov-report=xml:test_mid$i.xml && echo "passed" >> result.txt || echo "failed" >> result.txt
done

python tarantula-skeleton.py 