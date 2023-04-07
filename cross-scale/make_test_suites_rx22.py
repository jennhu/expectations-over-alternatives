import pandas as pd
from test_suite_helpers import *

TO_EXCLUDE = ["or", "damage"]
maps = {
    "begin": "began",
    "try": "tried",
    "believe": "believes",
    "dislike": "dislikes",
    "like": "likes",
    "match": "matches",
    "permit": "permits",
    "reduce": "reduced",
    "slow": "slowed",
    "start": "started",
    "survive": "survived",
    "want": "wants"
}

# Read data.
df = pd.read_csv("./human_data/rx22.csv")

# Exclude some scales based on sentence weirdness.
print("Performing exclusions:", TO_EXCLUDE)
df = df[~df.Weaker.isin(TO_EXCLUDE)]
print(f"{len(df.index)} rows")

# Add columns corresponding to scalar construction.
exp1 = pd.read_csv("./human_data/rx22_processed_exp1.csv")
df["scalar_construction"] = df.Item.apply(
    lambda i: exp1[exp1.Item==i].scalar_construction.values[0]
)
df["scale_id"] = df.Weaker + "/" + df.Stronger
print(df.head())

# Iterate through POS.
for pos in ["adj", "adv", "verb"]:
    vocab = get_vocab(pos)
    pos_df = df[df.pos==pos]

    # Ensure that all strong scalemates are in the vocabulary.
    for s in pos_df.Stronger:
        if s not in vocab:
            print(f"Adding '{s}' to vocabulary")
            vocab.append(s)
    print(f"Size of vocabulary (pos={pos}):", len(vocab))

    for i, row in pos_df.iterrows():
        items = []
        # Initialize new test suite for each item.
        result = {
            "meta": {"name": "RX22", "metric": "sum"},
            "predictions": [],
            "region_meta": {
                "1": "Prefix", 
                "2": "Weak scalemate", 
                "3": "Verb object",
                "4": "Scalar construction", 
                "5": "Alternative",
                "6": "EOS"
            }
        }
        # Add items based on full vocabulary.
        for word_idx, word in enumerate(vocab):
            item_data = dict(item_number=word_idx+1)
            conditions = [] # There's really only one condition.
            sentence = row.scalar_construction.replace(f" {row.Stronger}", f" {word}")
            weak = row.Weaker if row.Weaker not in maps else maps[row.Weaker]
            if word == weak:
                print(f"Skipping word={word} for weak scalemate={weak})")
                continue
            try:
                before_weak, after_weak = sentence.split(" "+weak)
            except:
                print(f"Splitting error! Sentence: {sentence} / Weak: {weak}")
                continue
            # Deal with optional direct object after verbal scales.
            obj, after_comma = after_weak.split(",")
            try:
                before_strong, after_strong = after_comma.split(word)
            except:
                print(f"Splitting error! Chunk: {after_comma} / Word: {word}")
                continue
            # Chunk sentence content into regions.
            regions = [
                dict(region_number=1, content=before_weak.strip()),
                dict(region_number=2, content=weak.strip()),
                dict(region_number=3, content=obj.strip()),
                dict(region_number=4, content="," + before_strong.rstrip()),
                dict(region_number=5, content=word),
                dict(region_number=6, content=after_strong.strip())
            ]
            conditions.append(dict(condition_name="sentence", regions=regions))
            item_data["conditions"] = conditions
            items.append(item_data)
        result["items"] = items

        scale_id = row.scale_id.replace("/", "_")
        suite_path = f"./test_suites/rx22/{scale_id}.json"
        dump_json(result, suite_path)
        print(f"Wrote test suite to {suite_path}")