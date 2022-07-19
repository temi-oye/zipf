import re

word_frequency = {}

def get_word_frequency(word_dict, string, stop_words=[]):

  words = re.split(r"\W+", string)
  words = list(filter(None, words)) #filter returns an iterator that must be converted back to a list

  for word in words:
    if(word.lower() in word_dict and word not in stop_words):
      word_dict[word.lower()] += 1
    elif word not in stop_words:
      word_dict[word.lower()] = 1

get_word_frequency(word_frequency, "")

