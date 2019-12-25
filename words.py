from build_dict import download_dict
import pandas as pd
import random
import os.path

file = 'dict.csv'
if not os.path.isfile(file):
  download_dict()
df = pd.read_csv(file)
lemmes = df.words

def nb_words(difficulty):
  nb_words = [100, 500, 1000, 5000]
  return nb_words[difficulty-1]

def pick_random_words(difficulty=1):
  # Take 100, 500, 1000 or 5000 most frequent words
  # depending on difficulty
  all_words = lemmes[0:nb_words(difficulty)].copy()
  # pick randomly 25 words among them
  random.shuffle(all_words)
  words = all_words[0:25].copy()
  return words

def split_words_by_player(words):
  random.shuffle(words)

  player_1 = words[0:8]
  player_2 = words[9:15]
  forbidden = [words[16]]
  return [player_1, player_2, forbidden]

if __name__ == '__main__':
  print(pick_random_words(1))
