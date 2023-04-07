# Variation within <some, all> scale (Degen, 2015)

This folder contains code and data for our analyses of variation within the <some, all> scale.

## Data

Please see the `data` folder for stimuli and model surprisal outputs.

## Obtaining model surprisals

The script `run_bert.py` is used to obtain surprisal at a particular strong scalemate from BERT.

To reproduce results from the paper, run the script `run_bert_alternatives.sh`.
This will obtain BERT surprisals for each alternative in our manually specified set.
The outputs will be saved to `data/some-all/model_outputs`. This should take about 5 minutes on a single GPU.

Our models are accessed through the Huggingface `transformers` library. 
Please refer to their [documentation](https://huggingface.co/docs/transformers/installation) 
for detailed installation instructions.

## Analyzing results

Please run the notebook `within-scale.ipynb` to reproduce figures from the paper.
Figures will be rendered to the `figures` folder.

### GloVe vectors for weighted average surprisal

To reproduce the weighted average surprisal results, you will need to download GloVe vectors.
We used the `glove.6B.300d.txt` file, which can be downloaded from this link: [https://nlp.stanford.edu/data/glove.6B.zip](https://nlp.stanford.edu/data/glove.6B.zip) 

The word vector file (`glove.6B.300d.txt`) should be placed in the root of this directory. You can read more about GloVe vectors [here](https://nlp.stanford.edu/projects/glove/).