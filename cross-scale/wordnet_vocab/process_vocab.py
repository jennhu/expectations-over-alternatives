import pandas as pd
import nltk

VOCAB_SIZE = 1000

def readlines(f):
    with open(f, "r") as fp:
        lines = [l.strip("\n") for l in fp.readlines()]
    return lines

print("Reading frequency data")
freqs = {}
freq_data = readlines("en_full.txt")
for line in freq_data:
    word, freq = line.split()
    freqs[word] = int(freq)

TAGS = {
    "adj": "JJ",
    "adv": "RB",
    "verb": "VB"
}
    
for pos in ["adj", "adv", "verb"]:
    print("="*80 + "\n" + pos + "\n" + "="*80)
    f = f"conv.data.{pos}"
    words = readlines(f)
    print(f"Before filtering: {len(words)} words")
    vocab = sorted(list(set(words)))
    print(f"Num unique words: {len(vocab)}")
    pos_verified_vocab = []
    for word in vocab:
        res = nltk.tag.pos_tag([word])
        pos_tag = res[0][1]
        if pos_tag == TAGS[pos]:
            pos_verified_vocab.append(word)
    print(f"Num words tagged as {TAGS[pos]}: {len(pos_verified_vocab)}")
    vocab_freq = {w: freqs[w] for w in pos_verified_vocab if w in freqs}
    sorted_vocab = sorted(list(vocab_freq.keys()), key=vocab_freq.get, reverse=True)
    final_vocab = sorted_vocab[:VOCAB_SIZE]
    with open(f"vocab_{pos}.txt", "w") as fp:
        for v in final_vocab:
            fp.write(v+"\n")
