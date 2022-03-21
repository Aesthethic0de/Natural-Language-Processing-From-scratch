import re
import string
import numpy as np


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


def process_tweet(tweet):
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')

    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)

    tokenizer =  TweetTokenizer(preserve_case=False, strip_handles=True,reduce_len=True)

    tweet_token = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_token:
        if(word not in stopwords_english and word not in string.punctuation 
        and word not in ':)' 
        and word not in '…'):
            stem_word = stemmer.stem(word) 
            tweets_clean.append(stem_word)

    return tweets_clean

