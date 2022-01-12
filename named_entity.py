import nltk
from nltk import word_tokenize

class nlp:
  def __init__(self,input):
    self.search = ["NN","NNS","NNP","NNPS","RB","RBR","RBS","RP","JJ","JJR","JJS","CD"]
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
      combine = []
      for branch in self.tags:
        words = branch[0]
        part = branch[1]
        if part in search:
          combine.append(words)
        if part not in search:
          if len(combine) > 0:
            self.results.append(" ".join(combine))
            combine = []
        count = count + 1
        if count == len(self.tags):
          if len(combine) > 0:
            self.results.append(" ".join(combine))
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

obj = nlp("the body temperature of vishwak is 100")
obj.process()
