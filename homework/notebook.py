# %%
# Carga de datos
import glob


def load_data(input_directory):

    sequence = []
    files = glob.glob(f"{input_directory}/*")
    for file in files:
        with open(file, "rt", encoding="utf-8") as f:
            raw_text = f.read()
            sequence.append((file, raw_text))
    return sequence


sequence = load_data(input_directory="../files/input")
for file, text in sequence:
    print(f"{file}  {text[:70]}")


#%%

# Clean text
import re


def clean_text(sequence):
    cleaned_sequence = []
    for file, text in sequence:
        cleaned_text = re.sub(r"\n", " ", text)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)
        cleaned_text = cleaned_text.strip()
        cleaned_text = cleaned_text.lower()
        cleaned_sequence.append((file, cleaned_text))
    return cleaned_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
for file, text in cleaned_sequence:
    print(f"{file}  {text[:70]}")

# %%
# Tokenization
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def tokenize(sequence):
    tokenized_sequence = []
    for file, text in sequence:
        tokens = word_tokenize(text)
        tokenized_sequence.append((file, tokens))
    return tokenized_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
for file, text in tokenized_sequence:
    print(f"{file}  {' '.join(text)[:70]}")
    


#%%



import textwrap

for file, text in tokenized_sequence:
    print(textwrap.fill(' '.join(text)))
    print()
    print()




#%%

# Remoción de datos ruidosos (Opcion A)
def filter_tokens_a(sequence):
    """Esta solucion puede perder tokens que contienen caracteres no alfabeticos"""
    filtered_sequence = []
    for file, tokens in sequence:
        filtered_tokens = [token for token in tokens if token.isalpha()]
        filtered_sequence.append((file, filtered_tokens))
    return filtered_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
filtered_sequence = filter_tokens_a(tokenized_sequence)
for file, text in filtered_sequence:
    print(f"{file}  {' '.join(text)[:75]}")
    
#%%  
    
    
for file, text in filtered_sequence:
    print(textwrap.fill(' '.join(text)))
    print()
    print()    
    
    

#%%   
    
    
# Remoción de datos ruidosos (Opcion B)
def filter_tokens_b(sequence):
    """Esta solucion puede perder tokens que contienen caracteres no alfabeticos"""
    filtered_sequence = []
    for file, tokens in sequence:
        filtered_tokens = [re.sub(r"[^a-zA-Z\s]", " ", token) for token in tokens]
        filtered_tokens = [re.sub(r"\s+", " ", token) for token in filtered_tokens]
        filtered_tokens = [token.strip() for token in filtered_tokens]
        filtered_tokens = [token for token in filtered_tokens if token != ""]
        filtered_sequence.append((file, filtered_tokens))
    return filtered_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
filtered_sequence = filter_tokens_b(tokenized_sequence)
for file, text in filtered_sequence:
    print(f"{file}  {' '.join(text)[:70]}")
    
    
    
    
#%%   
    
    
    
for file, text in filtered_sequence:
    print(textwrap.fill(' '.join(text)))
    print()
    print()
    
    
    
    
    
    
    
    
# Remove the stopwords
nltk.download("stopwords")


def remove_stopwords(sequence):
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_sequence = []
    for file, tokens in sequence:
        filtered_tokens = [token for token in tokens if token not in stop_words]
        filtered_sequence.append((file, filtered_tokens))
    return filtered_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
filtered_sequence = filter_tokens_b(tokenized_sequence)
filtered_sequence = remove_stopwords(filtered_sequence)
for file, text in filtered_sequence:
    print(f"{file}  {' '.join(text)[:70]}")
    
# %%
# Save to disk
import os
import textwrap


def save_data(output_directory, sequence):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file, tokens in sequence:
        file = file.replace("\\", "/")
        with open(
            f"{output_directory}/{file.split('/')[-1]}",
            "wt",
            encoding="utf-8",
        ) as f:
            f.write(textwrap.fill(" ".join(tokens), width=70))


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
filtered_sequence = filter_tokens_b(tokenized_sequence)
filtered_sequence = remove_stopwords(filtered_sequence)
save_data(output_directory="../files/output", sequence=filtered_sequence)
# %%
