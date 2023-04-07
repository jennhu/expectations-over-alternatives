The `conv*` files were created by parsing the raw WordNet database files from `scripts/download_vocab.sh`.

We processed these files to generate `vocab*` using `process_vocab.py`. 
Then, we manually cleaned the adverb list (removing words like "now"), 
as well as the verb list (removing "do", "be"), resulting in the files in the folder `clean`.

We look at frequencies using counts from https://github.com/hermitdave/FrequencyWords.
Download the counts with the following command:
```bash
wget https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/en/en_full.txt
```