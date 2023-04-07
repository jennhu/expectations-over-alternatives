# Variation across scales (scalar diversity)

This folder contains the code and data for our analyses of cross-scale variation ("scalar diversity").

## Obtaining model surprisals

We use the `syntaxgym` library to obtain surprisals from GPT-2. 
Before obtaining surprisals, we first need to prepare test suites
that conform to the SyntaxGym formatting requirements (see details below).

### Creating test suites

First, you need to create the alternative sets for each part of speech (adjective,
adverb, or verb). We refer to this as the "vocabulary". The vocabulary used in our paper can be found in the `wordnet_vocab` folder. You can regenerate the vocabulary by running `bash scripts/download_vocab.sh`.
However, note that we performed some manual cleaning of the vocabulary.

Run the command `bash scripts/make_test_suites.sh` to generate test suites for each scale
across the four datasets. All test suites are saved to the `test_suites` folder, in 
a subfolder corresponding to the original human dataset (`g18`, `pvt21`, `rx22`, or `vt16`). 
Each test suite JSON file follows the SyntaxGym format, where each sentence is split into regions 
(e.g., `Weak scalemate`, `Scalar construction`, and `Alternative`),
and we compute sum surprisal over the content in those regions.
You can learn more about this format in the ACL 2020 paper
([Gauthier et al., 2020](https://aclanthology.org/2020.acl-demos.10/)),
or at the online [documentation](https://cpllab.github.io/syntaxgym-core/architecture.html).

### Running models

Once test suites have been created, the models can be run. 
Instructions and scripts for obtaining model surprisals are in the `scripts` folder. 
Please refer to the `README` there for more details.

The region-by-region model surprisals are saved to the `model_results` folder.

## Analyzing results

Please run the notebook `cross-scale.ipynb` to reproduce figures from the paper.
Figures will be rendered to the `figures` folder.

### GloVe vectors for weighted average surprisal

To reproduce the weighted average surprisal results, you will need to download GloVe vectors.
We used the `glove.6B.300d.txt` file, which can be downloaded from this link: [https://nlp.stanford.edu/data/glove.6B.zip](https://nlp.stanford.edu/data/glove.6B.zip) 

The word vector file (`glove.6B.300d.txt`) should be placed in the root of this directory. You can read more about GloVe vectors [here](https://nlp.stanford.edu/projects/glove/).