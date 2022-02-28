import pandas as pd

import re
import sys
from nltk.stem.porter import PorterStemmer

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")

sa = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)



def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    return word


def preprocess_text(text):
    processed_text = []
    
    text = text.lower()

    # Replace 2+ or more dots with space
    text = re.sub(r'\.{2,}', ' ', text)
    
    # Strip space, " and '
    text = text.strip(' "\'')

    text = re.sub(r'\s+', ' ', text)
    words = text.split()

    for word in words:
      word = preprocess_word(word)
      processed_text.append(word)

    return ' '.join(processed_text)


def sentiment_analysis(text):
    "True if positive"
    p = sa(str(text))
    return pd.Series([p[0]["label"], round(p[0]["score"],2)])



