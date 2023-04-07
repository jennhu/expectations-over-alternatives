import pandas as pd
from tqdm import tqdm
import torch
import argparse
from transformers import BertTokenizer, BertForMaskedLM

def load_mt(model_name="bert-base-uncased", cache_dir="/om2/user/jennhu/cache"):
    tokenizer = BertTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    print(f"Successfully loaded tokenizer ({model_name})")
    model = BertForMaskedLM.from_pretrained(model_name, cache_dir=cache_dir).to(DEVICE)
    print(f"Successfully loaded model ({model_name})")
    return model, tokenizer

if __name__ == "__main__":
    # Set some constants.
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
    SCALE = "some-all"
    
    parser = argparse.ArgumentParser(description="Compute surprisal of strong scalemate under BERT")
    parser.add_argument("--model_name", default="bert-base-uncased", type=str)
    parser.add_argument("--sentences", default=f"./data/{SCALE}/sentences_for_model.csv", type=str)
    parser.add_argument("--strong_scalemate", type=str, default="all", 
                        choices=["each", "every", "few", "half", "many", "most", "much", "all"])
    args = parser.parse_args()
    
    # Read stimuli.
    WEAK = SCALE.split("-")[0]
    df = pd.read_csv(args.sentences)
    print(df.head())

    # Load model and tokenizer.
    model, tokenizer = load_mt(model_name=args.model_name)

    # Get token id of strong scalemate that we are testing.
    STRONG_token_id = tokenizer(
        [args.strong_scalemate], add_special_tokens=False, return_tensors="pt"
    ).input_ids.squeeze().item()
    print(f"token_id of `{args.strong_scalemate}`:", STRONG_token_id)

    df = df.dropna()
    n_rows = len(df.index)
    for i, row in tqdm(df.iterrows(), total=n_rows):
        if SCALE == "some-all":
            sent_sbna = row.Sentence.replace("some", "some, but not [MASK],")
            inpt = sent_sbna

        # Forward pass in model.
        inpts = tokenizer(inpt, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
             logits = model(**inpts).logits

        # Retrieve index corresponding to [MASK].
        mask_token_index = (inpts.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
        predicted_token_logits = logits[0, mask_token_index]
        predicted_token_id = predicted_token_logits.argmax(axis=-1)
        predicted_token_logprobs = torch.nn.functional.log_softmax(predicted_token_logits, dim=-1)
        try:
            STRONG_surprisal = -predicted_token_logprobs[0, STRONG_token_id] # get surprisal of strong scalemate
        except:
            continue

        # Update dataframe.
        df.loc[i, "surprisal_at_strong"] = STRONG_surprisal.item()
        df.loc[i, "predicted_token"] = tokenizer.decode(predicted_token_id)

    file_name = f"data/{SCALE}/model_output/{args.model_name}_{args.strong_scalemate}.csv"
    df.to_csv(file_name, index=False)