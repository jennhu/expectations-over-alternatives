#!/bin/bash

MODEL="gpt2"
TEST_SUITE_PATH=$1 # json file
OUTPUT_PATH=$2 # tsv file

syntaxgym compute-surprisals \
    --tabular_results \
    huggingface://${MODEL} \
    ${TEST_SUITE_PATH} > ${OUTPUT_PATH}