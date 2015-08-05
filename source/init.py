from lib import *

file = 'data.txt'
sentence = "The quick brown fox jumps over the lazy dog."
data = CustomDict()

data.addSent(sentence)
save(data, file)