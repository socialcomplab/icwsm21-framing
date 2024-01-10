# polarice.preprocessing.GERMAN_TWEET_PIPELINE

import texthero as hero
import pandas as pd
from dataclasses import dataclass
import pickle
import datetime

def remove_retweet_symbol(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"^rt"
    return s.str.replace(pattern, "")

def remove_hashtags(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"\#\S+"
    return s.str.replace(pattern, "")

def remove_mentions(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"\@\S+"
    return s.str.replace(pattern, "")

def remove_single_letters(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"\b[a-z]\b"
    return s.str.replace(pattern, "")

def remove_hashtags_at_the_end(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"(\#\S+\s*)*$"
    return s.str.replace(pattern, "")

def convert_hastags_to_text(s: pd.core.series.Series) -> pd.core.series.Series:
    pattern = r"\#(\S+)"
    return s.str.replace(pattern, r"\1")

GERMAN_STOPWORDS = hero.stopwords.nltk.corpus.stopwords.words('german')

def remove_german_stopwords(s: pd.core.series.Series) -> pd.core.series.Series:
    return hero.remove_stopwords(s, stopwords=GERMAN_STOPWORDS)

GERMAN_TWEET_PIPELINE = [
    hero.preprocessing.fillna,
    hero.preprocessing.lowercase,
    
    remove_retweet_symbol,
    remove_mentions,
    remove_hashtags_at_the_end,
    convert_hastags_to_text,
    hero.preprocessing.remove_urls,
    
    hero.preprocessing.remove_digits,
    hero.preprocessing.remove_punctuation,
    remove_german_stopwords,
    hero.preprocessing.remove_diacritics,
    remove_single_letters,
    hero.preprocessing.remove_whitespace
]

ENGLISH_TWEET_PIPELINE = [
    hero.preprocessing.fillna,
    hero.preprocessing.lowercase,
    
    remove_retweet_symbol,
    remove_mentions,
    remove_hashtags_at_the_end,
    convert_hastags_to_text,
    hero.preprocessing.remove_urls,
    
    hero.preprocessing.remove_digits,
    hero.preprocessing.remove_punctuation,
    hero.preprocessing.remove_stopwords,
    hero.preprocessing.remove_diacritics,
    remove_single_letters,
    hero.preprocessing.remove_whitespace
]

# polarice.PolarizationDataset

@dataclass
class PolarizationDataset:
    """Base Container Class for Polarization"""
    df: pd.DataFrame
    group_column: str
    text_column: str
    topic: str
    created: datetime.datetime = datetime.datetime.now()
        
    def save(self, fname):
        with open(fname, "wb") as f:
            pickle.dump(self, f)
            
    @staticmethod
    def load(fname):
        with open(fname, "rb") as f:
            return pickle.load(f)
        
    def grouped_text(self):
        return self.df.groupby(self.group_column)[self.text_column]
    
    # Get corpus on on group
    def get_group_data(self, group_name):
        return self.df[self.df[self.group_column] == group_name]
    
    # Get group names
    def get_groups(self):
        return self.df[self.group_column].unique()
