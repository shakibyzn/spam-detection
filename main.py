
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
import string
import re
import wandb
import os
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
nltk.download('wordnet')
nltk.download('stopwords')


def clean_data(text: str) -> List:
   lower = text.lower()
   splitted = lower.split()
   re_punc = re.compile('[%s]' % re.escape(string.punctuation))
   tokens = [re_punc.sub('',w) for w in splitted]
   tokens = [word for word in tokens if word.isalpha()]
   stop_words = set(stopwords.words('english'))
   tokens = [w for w in tokens if not w in stop_words]
   lemmeted = [WordNetLemmatizer().lemmatize(w) for w in tokens]
   tokens = [word for word in lemmeted if len(word) > 2]
   return tokens


def load_data():
    df = pd.read_csv('SMSSpamCollection.txt', names=['class', 'text'], header=None, delimiter='\t')
    df['class'] = df['class'].rank(method='dense', ascending=False).astype(int)

    x_train, x_test, y_train, y_test = train_test_split(df['text'], df['class'])

    vocab = Counter()
    for row in x_train:
        vocab.update(clean_data(row))

    return x_train, x_test, y_train, y_test, vocab


def main() -> None:
    
    # wandb init
    wandb.init(entity=os.environ['WANDB_ENTITY'], project=os.environ['WANDB_PROJECT'])
    # load data
    x_train, x_test, y_train, y_test, vocab = load_data()

    # tf-idf
    v = TfidfVectorizer(vocabulary=vocab.keys())
    x_train_transformed = v.fit_transform(x_train)
    x_test_transformed = v.fit_transform(x_test)

    # model 
    model = BernoulliNB()
    model.fit(x_train_transformed, y_train)
    pred = model.predict(x_test_transformed)
    cls_report = classification_report(y_test, pred, output_dict=True)

    # logging
    wandb.log({
        'test/precision': cls_report['weighted avg']['precision'],
        'test/recall': cls_report['weighted avg']['recall'],
        'test/f1-score': cls_report['weighted avg']['f1-score']
    })


if __name__ == '__main__':
    main()