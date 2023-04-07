#!/bin/bash

TEMPLATE=$1
DATASET="vt16"
# grab the files, and export it so the 'child' sbatch jobs can access it (export)
FILES=($(ls -1 ../test_suites/${DATASET}/template${TEMPLATE}))

# get size of array
NUMFILES=${#FILES[@]}

# now subtract 1 as we have to use zero-based indexing (first cell is 0)
ZBNUMFILES=$(($NUMFILES - 1))

# now submit to SLURM
if [ $ZBNUMFILES -ge 0 ]; then
    sbatch --array=0-$ZBNUMFILES run_sg_vt16.batch gpt2 gpt2 $TEMPLATE
fi