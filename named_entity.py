#! /usr/bin/env python3
import sys
import nltk
from nltk import word_tokenize

class nlp:
  def __init__(self,input):
    self.noun = ["NN","NNS","NNP","NNPS","DT"]
    self.verb = ["MD","RB","RBR","RBS","RP","VB","VBG","VBD","VBN","VBP","VBZ","JJ","JJR","JJS"]
    self.input = input
    self.tags = []
    self.results = []
  def download(self):
    try:
      nltk.download('punkt')
      nltk.download('averaged_perceptron_tagger')
      return True
    except Exception as e:
      return False
  def tokenize(self):
    try:
      self.tags = nltk.pos_tag(word_tokenize(self.input))
      return True
    except Exception as e:
      self.download()
      return False
  def entity(self):
    try:
      count = 0
      combine_1 = []
      combine_2 = []
      for branch in self.tags:
        words = branch[0]
        part = branch[1]
        if part in self.noun:
          if len(combine_2) > 0:
            self.results.append(" ".join(combine_2))
            combine_2 = []
          combine_1.append(words)
        if part in self.verb:
          if len(combine_1) > 0:
            self.results.append(" ".join(combine_1))
            combine_1 = []
          combine_2.append(words)
        count = count + 1
        if part not in self.verb and part not in self.noun:
          self.results.append(words)
          if len(combine_1) > 0:
            self.results.append(" ".join(combine_1))
            combine_1 = []
          if len(combine_2) > 0:
            self.results.append(" ".join(combine_2))
            combine_2 = []
        if count == len(self.tags):
          if len(combine_1) > 0:
            self.results.append(" ".join(combine_1))
          if len(combine_2) > 0:
            self.results.append(" ".join(combine_2))
      return True
    except Exception as e:
      return False
  def process(self):
    try:
      self.tokenize()
      self.entity()
      return ", ".join(self.results)
    except Exception as e:
      return "error occurred"

argv_length = len(sys.argv)
argv_frame = argv_length - 1
if argv_frame > 0:
  argv_log = ""
  for i in range(1,argv_length):
    argv_log += sys.argv[i] + " "
  obj = nlp(argv_log)
  print(obj.process())
  exit()
