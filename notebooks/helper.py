import numpy as np
import pandas as pd
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()

def remove_punctuations(text):
    text_punc = "".join([i for i in text if i not in string.punctuation])
    return text_punc

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urls_removed = url_pattern.sub("",text)
    return urls_removed

def remove_usernames(text):
    pattern = re.compile(r'@[a-zA-Z0-9_-]+')
    user_names_removed = pattern.sub("",text)
    return user_names_removed

def remove_numbers(text):
    pattern = re.compile(r'[0.0-9.0]+')
    numbers_removed = pattern.sub("",text)
    return numbers_removed

def remove_unwanted_whitespaces(text):
    pattern = re.compile(r'\s{2,}')
    whitespace_morethan_two_removed = pattern.sub(" ",text)
    return whitespace_morethan_two_removed

def stopwords_removal(text):
    output = [i for i in text if i not in stop_words]
    return output

def tokenization(text):
    tokens = word_tokenize(text)
    return tokens

def lemmatize(text):
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return text
