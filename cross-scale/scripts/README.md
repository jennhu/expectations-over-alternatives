# Scripts

## Obtaining model surprisals for a given test suite

### Installing `syntaxgym` 

To obtain surprisal outputs from models, we use the `syntaxgym` command-line tools.
You can read more about `syntaxgym` at the official [documentation](https://cpllab.github.io/syntaxgym-core/commands.html).

You should install `syntaxgym` by running:
```bash
pip install -U syntaxgym==0.7a2
```
This specific version ensures compatibility with Huggingface, which we use to access GPT-2.

### Computing surprisals

If you have a test suite at `PATH_TO_TEST_SUITE.json`, want to evaluate GPT-2, 
and want to save model surprisals in TSV format to `PATH_TO_OUTPUT_FILE.tsv`,
then run the following command:
```bash
syntaxgym compute-surprisals \
    --tabular_results \
    huggingface://gpt2 \
    PATH_TO_TEST_SUITE.json > PATH_TO_OUTPUT_FILE.tsv
```

We've wrapped this up in the script `get_surprisals.sh`, which takes two arguments: 
the test suite path and output path. Use it by running `bash get_surprisals.sh <TEST_SUITE_PATH> <OUTPUT_PATH>`.
You can also use other Huggingface models by changing the model identifier at the top of the script.

## SLURM job arrays

WeI have also included sample scripts for running the models on all test suites in parallel,
based on the SLURM job array system. Of course, you would need to adapt these scripts
to your particular computing environment before running them, but we hope these provide
a useful starting point.

To launch these jobs, go to the `slurm` directory and run:
```bash
./submit_sg_jobs.sh <DATASET>
```
`<DATASET>` can be one of `rx22` (Ronai & Xiang, 2022), `pvt21` (Pankratz & van Tiel, 2021), or
`g18` (Gotzner et al., 2018). 

For the van Tiel et al. (2016) dataset, we wrote a separate script to deal with
the multiple sentence templates per scale. To launch these jobs, run:
```bash
./submit_sg_vt16_jobs.sh <TEMPLATE>
```
`<TEMPLATE>` can be one of `1`, `2`, or `3`.