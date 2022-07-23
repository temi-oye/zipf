import re
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import operator
import numpy as np
import os
import math

def get_word_frequency(string, stop_words=[]):

  word_dict = {}
  words = re.split(r"\W+", string)
  words = list(filter(None, words)) #filter returns an iterator that must be converted back to a list

  for word in words:
    if(word.lower() in word_dict and word not in stop_words):
      word_dict[word.lower()] += 1
    elif word not in stop_words:
      word_dict[word.lower()] = 1

  return word_dict

def make_most_frequent_words_barchart(word_dict):
  top_words_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:30])

  words = list(top_words_dict.keys())
  frequencies = list(top_words_dict.values())
  ranks = np.arange(1, len(frequencies)+1)

  frequencies_log = list(map(log, frequencies))
  ranks_log = list(map(log, ranks))

  plt.style.use("ggplot")

  plt.title("Zipf's law in 'The Adventures of Shelock Holmes'")

  plt.xlabel("Rank")
  plt.ylabel("Frequency")
  plt.bar_label(plt.bar(ranks, frequencies), words)
  plt.xticks(ranks)

  plt.show()

def log(num):
  return math.log(num)

def get_words_from_file(file_name):
  str_of_words = ""
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  with open(os.path.join(__location__, file_name), 'r', encoding="utf8") as file:
    for line in file:
      str_of_words+=line.strip()
  return str_of_words

words = get_words_from_file("adventures of sherlock holmes.txt")
word_frequency = get_word_frequency(words)
make_most_frequent_words_barchart(word_frequency)
