import io
import requests
import pandas as pd

def download_dict():
  # Get dictionnary from lexique.org
  url = 'http://www.lexique.org/databases/Lexique382/Lexique382.tsv'
  s = requests.get(url).content
  dictionnary = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='\t')


  # Keep only names (not verbs, adverbs, etc)
  # sorted by frequence (Descending)
  names = dictionnary[dictionnary['cgram'] == 'NOM']
  names_sorted = names.sort_values('freqlivres', ascending=False)
  sanitized_names = names_sorted['lemme'].unique()
  pd.DataFrame({'words': sanitized_names}).to_csv('dict.csv', index=False)
