import re
import matplotlib.pyplot as plt
import operator
import numpy as np


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
  top_words_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:20])

  words = list(top_words_dict.keys())
  frequencies = list(top_words_dict.values())

  ranks = np.arange(1, len(frequencies)+1)


  plt.style.use("ggplot")

  plt.xlabel("Rank")
  plt.ylabel("Frequency")
  plt.bar_label(plt.bar(ranks, frequencies), words)
  plt.show()

word_frequency = get_word_frequency("")
make_most_frequent_words_barchart(word_frequency)

print(word_frequency)

