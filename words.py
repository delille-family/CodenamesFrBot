import io
import random
import requests
import pandas as pd

# Get dictionnary from lexique.org
url = 'http://www.lexique.org/databases/Lexique382/Lexique382.tsv'
s=requests.get(url).content
dictionnary=pd.read_csv(io.StringIO(s.decode('utf-8')), sep='\t')

# Or locally
# dictionnary = pd.read_csv('dict.tsv')

# Keep only names (not verbs, adverbs, etc)
# sorted by frequence (Descending)
dictionnary_sorted_by_freq = dictionnary[dictionnary['cgram'] == 'NOM'].sort_values('freqlivres', ascending=False)
lemmes = dictionnary_sorted_by_freq['lemme'].unique()

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
