import re
import pickle

#=========File Interaction=========#
def save(obj, file):
    f = open(file, 'wb')
    pickle.dump(obj, f)
    f.close
    
def load(file):
    f = open(file, 'rb')
    data = pickle.load(f)
    f.close()
    return data

#=========Parse text files into sentences=========#
#takes filename as input, returns list of strings
def parseTxt(file):
    f = open(file, encoding="utf-8")
    string = f.read()
    f.close()
    patterns = [re.compile('\\n'), re.compile('[^ \w\s\.\?!-]'), re.compile('[A-Z]\w*[.,]?\s(?:(?!Mr|Ms|Dr|Jr|Sr|[.?!]).|Jr\.|Sr\.|Mr\.|Ms\.|Dr\.)*(?:(?!Mr|Ms|Dr|[.?!]).|Mr\.|Ms\.|Dr\.)*[\"!?:.]')]
    string = re.sub(patterns[0], " ", strOrig)
    string = re.sub(patterns[1], "", string)
    matches = re.findall(patterns[2], string)
    sentences = []
    for m in matches:
        sentences.append(m)  
    return sentences

#=========Class definitions=========#
class Sentence(object):
    def __init__(self, string, dict):
        self.string = string
        words = []
        if string[-1] in '?.!':
            string = string[0:-1]
        i=0
        for w in re.split('\W+', string):
            words.append(dict.add(w, i))
            i += 1
        self.words = words
        dict.sentences.append(self)

class Word(object):
    def __init__(self, string, position):
        self.string = string
        self.data = [position]
    
class CustomDict(object):
    def __init__(self, name = "not given"):
        self.words = []
        self.sentences = []
        self.name = name
        
    def find(self, word):
        found = False
        i = 0
        for w in self.words:
            if word.lower() == w.string:
                found = True
                return i
            i += 1
        if not found:
            return -1
        
    def add(self, word, position):
        result = self.find(word)
        if result == -1:
            theWord = Word(word.lower(), position)
            self.words.append(theWord)
            return theWord
        else:
            self.words[result].data.append(position)
            return self.words[result]
        
    def addSent(self, sentence):
        self.sentences.append(Sentence(sentence, self))
        
    def addFile(self, file):
        sents = parseTxt(file)
        for sent in sents:
            self.addSent(sent)

    def sort(self):
        switched = True
        while switched:
            v = self.words
            for i in range(len(v)-1):
                w1 = v[i]
                w2 = v[i+1]
                l1 = w1.string
                l2 = w2.string
                print("===================")
                print(l1 + " vs " + l2)
                scope = min([len(l1), len(l2)])
                for n in range(scope):
                    print("comparing " + l1[n] + " to " + l2[n])
                    if l1[n] > l2[n]:
                        self.words[i] = w2
                        self.words[i + 1] = w1
                        switched = True
                        break
                    elif l1[n] == l2[n]:
                        print("share " + str(n) + "th letter")
                        if n + 1 not in range(len(l2)):
                            self.words[i] = w2
                            self.words[i + 1] = w1
                            switched = False
                            break
                        elif n + 1 not in range(len(l1)):
                            switched = False
                            break
                    else:
                        switched = False
                        break
                print("\n")
            if v == self.words:
                switched = True
                    
#========Console interaction functions========#
def manualSelect():
    while True:
        print("Specify option to select ([f]ile, [c]lear:")
        select = get()
        if select == 'f':
            print("Enter path:")
            dataFile = get()
            break
        elif select == 'c':
            dataFile = ''
            break
        else:
            print("Please enter f for file, or c to clear.")
    return dataFile

def get():
    print(">> ", end="")
    return input("")
