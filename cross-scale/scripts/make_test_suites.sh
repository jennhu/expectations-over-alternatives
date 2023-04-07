#!/bin/bash

for dataset in g18 pvt21 rx22 vt16; do
    python make_test_suites_${dataset}.py
done