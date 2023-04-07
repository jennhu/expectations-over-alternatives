import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./some_database.tsv", sep="\t")
    df = df[["Item", "Sentence"]].drop_duplicates()
    print(df.head())
    df.to_csv("./sentences_for_model.csv", index=False)
