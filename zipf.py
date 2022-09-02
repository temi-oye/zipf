import re
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import operator
import numpy as np
import os
import math
from nltk.stem import WordNetLemmatizer

#lemmatization groups together different inflected forms of a word into a single word eg rocks -> rock
lemmatizer = WordNetLemmatizer()

def get_word_frequency(string, stop_words=[]):

  word_dict = {}
  words = re.split(r"\W+", string)
  words = list(filter(None, words)) #filter returns an iterator that must be converted back to a list

  for word in words:
    word_lemmatized = lemmatizer.lemmatize(word)
    if(word_lemmatized.lower() in word_dict and word_lemmatized not in stop_words):
      word_dict[word_lemmatized.lower()] += 1
    elif word not in stop_words:
      word_dict[word_lemmatized.lower()] = 1

  return word_dict

def make_most_frequent_words_barchart(word_dict, num_words_to_graph):
  top_words_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:num_words_to_graph])
  MAX_NUM_BARS = 35

  words = list(top_words_dict.keys())
  frequencies = list(top_words_dict.values())
  ranks = np.arange(1, len(frequencies)+1)

  plt.style.use("ggplot")

  plt.title("Zipf's law in Sherlock Holmes")

  plt.xlabel("Rank")
  plt.ylabel("Frequency")

  if(num_words_to_graph > MAX_NUM_BARS):
    plt.bar_label(plt.bar(ranks, frequencies), words[:5], fmt="")
  else:
    plt.bar_label(plt.bar(ranks, frequencies), words)
    plt.xticks(ranks)
  
  plt.show()


def get_words_from_file(file_name):
  str_of_words = ""
  # gets file from within the same directory 
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  with open(os.path.join(__location__, file_name), 'r', encoding="utf8") as file:
    for line in file:
      str_of_words+=line.strip()
  return str_of_words

def zipf(words, num_words_to_graph):
  word_frequency = get_word_frequency(words)
  make_most_frequent_words_barchart(word_frequency, num_words_to_graph)

words = get_words_from_file("sherlock holmes.txt")

zipf(words, 100)

