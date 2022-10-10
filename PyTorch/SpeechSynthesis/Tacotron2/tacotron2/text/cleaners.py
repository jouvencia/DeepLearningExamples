""" from https://github.com/keithito/tacotron """

'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
'''

import re
from .numbers import normalize_numbers
from .unidecoder import unidecoder


# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

# List of (regular expression, replacement) pairs for abbreviations:
#_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
#  ('mrs', 'misess'),
#  ('mr', 'mister'),
#  ('dr', 'doctor'),
#  ('st', 'saint'),
#  ('co', 'company'),
#  ('jr', 'junior'),
#  ('maj', 'major'),
#  ('gen', 'general'),
#  ('drs', 'doctors'),
#  ('rev', 'reverend'),
#  ('lt', 'lieutenant'),
#  ('hon', 'honorable'),
#  ('sgt', 'sergeant'),
#  ('capt', 'captain'),
#  ('esq', 'esquire'),
#  ('ltd', 'limited'),
#  ('col', 'colonel'),
#  ('ft', 'fort'),
#]]

_abbreviations = [(re.compile('\\b%s\\.?\\b' % x[0], re.IGNORECASE), x[1])
                  for x in [
                      ('M', 'monsieur'),
                      ('Mlle', 'mademoiselle'),
                      ('Mlles', 'mesdemoiselles'),
                      ('Mme', 'Madame'),
                      ('Mmes', 'Mesdames'),
                      ('N.B', 'nota bene'),
                      ('p.c.q', 'parce que'),
                      ('Pr', 'professeur'),
                      ('qqch', 'quelque chose'),
                      ('rdv', 'rendez-vous'),
                      ('max', 'maximum'),
                      ('min', 'minimum'),
                      ('no', 'numéro'),
                      ('adr', 'adresse'),
                      ('dr', 'docteur'),
                      ('st', 'saint'),
                      ('co', 'companie'),
                      ('jr', 'junior'),
                      ('sgt', 'sergent'),
                      ('capt', 'capitain'),
                      ('col', 'colonel'),
                      ('av', 'avenue'),
                      ('av. J.-C', 'avant Jésus-Christ'),
                      ('apr. J.-C', 'après Jésus-Christ'),
                      ('art', 'article'),
                      ('c.-à-d', 'c’est-à-dire'),
                      ('etc', 'et cætera'),
                      ('ex', 'exemple'),
                      ('excl', 'exclusivement'),
                      ('boul', 'boulevard'),
                      ('h', 'heure')
                  ]]



def expand_abbreviations(text):
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text


def expand_numbers(text):
  return normalize_numbers(text)


def lowercase(text):
  return text.lower()


def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)


def convert_to_ascii(text):
  return unidecoder(text)

def replace_symbols(text):
  text = text.replace(';', ',')
  text = text.replace('-', ' ')
  text = text.replace(':', ',')
  text = text.replace('&', ' et ')
  return text

def remove_aux_symbols(text):
  text = re.sub(r'[\<\>\(\)\[\]\"]+', '', text)
  return text

def basic_cleaners(text):
  '''Basic pipeline that lowercases and collapses whitespace without transliteration.'''
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def transliteration_cleaners(text):
  '''Pipeline for non-English text that transliterates to ASCII.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


#def english_cleaners(text):
#  '''Pipeline for English text, including number and abbreviation expansion.'''
#  text = convert_to_ascii(text)
#  text = lowercase(text)
#  text = expand_numbers(text)
#  text = expand_abbreviations(text)
#  text = collapse_whitespace(text)
#  return text

def french_cleaners(text):
'''Pipeline for French text.'''
text = lowercase(text)
text = expand_abbreviations(text)
text = replace_symbols(text)
text = remove_aux_symbols(text)
text = collapse_whitespace(text)
return text
