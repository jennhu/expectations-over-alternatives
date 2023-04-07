#!/bin/bash

for STRONG in "each" "every" "few" "half" "many" "most" "much" "all"; do
    python run_bert.py \
        --model_name bert-base-uncased \
        --strong_scalemate $STRONG \
        --sentences data/some-all/sentences_for_model.csv
done