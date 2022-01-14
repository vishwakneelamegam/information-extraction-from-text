import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

class nlp:
  def __init__(self,input):
    self.noun = ["NN","NNS","NNP","NNPS","CD","JJ","JJR","JJS","DT"]
    self.verb = ["MD","VB","VBG","VBD","VBN","VBP","VBZ","RB","JJ","JJR","JJS","RBR","RBS","RP"]
    self.input = input
    self.tags = []
    self.results = []
  def download(self):
    try:
      nltk.download('punkt')
      nltk.download('averaged_perceptron_tagger')
      nltk.download('stopwords')
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
  def filter(self,word_list):
    try:
      result = [word.strip() for word in word_list if word.strip() not in stopwords.words('english')]
      return result
    except Exception as e:
      self.download()
      return []
  def recheck(self):
    try:
      self.results = [word.strip() for word in self.results if word.strip() != ""]
      return True
    except Exception as e:
      return False
  def entity(self):
    try:
      count = 0
      combine_1 = []
      combine_2 = []
      for branch in self.tags:
        words = branch[0]
        part = branch[1]
        if part in self.noun and part in self.verb:
          if len(combine_1) > 0:
            combine_1.append(words)
          if len(combine_2) > 0:
            combine_2.append(words)
          if len(combine_1) == 0 and len(combine_2) == 0 and count != len(self.tags):
            if self.tags[count + 1][1] in self.noun:
              combine_1.append(words)
            if self.tags[count + 1][1] in self.verb:
              combine_2.append(words)
        if part in self.noun and part not in self.verb:
          if len(combine_2) > 0:
            self.results.append(" ".join(self.filter(combine_2)))
            combine_2 = []
          combine_1.append(words)
        if part in self.verb and part not in self.noun:
          if len(combine_1) > 0:
            self.results.append(" ".join(self.filter(combine_1)))
            combine_1 = []
          combine_2.append(words)
        count = count + 1
        if part not in self.verb and part not in self.noun:
          self.results.append(words)
          if len(combine_1) > 0:
            self.results.append(" ".join(self.filter(combine_1)))
            combine_1 = []
          if len(combine_2) > 0:
            self.results.append(" ".join(self.filter(combine_2)))
            combine_2 = []
        if count == len(self.tags):
          if len(combine_1) > 0:
            self.results.append(" ".join(self.filter(combine_1)))
          if len(combine_2) > 0:
            self.results.append(" ".join(self.filter(combine_2)))
      return True
    except Exception as e:
      return False
  def process(self):
    try:
      self.tokenize()
      self.entity()
      self.recheck()
      return ", ".join(self.results)
    except Exception as e:
      return "error occurred"

obj = nlp("the black cat is under the table")
obj.process()
