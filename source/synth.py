parameters = {
    
}
from lib import *
from random import randint

def score(w, i, sent = [], randFlag = False):
    score = 1
    if mode(w.data) == i:
        score = 5
    if i > 0 and len(sent) > 0 and sent[i - 1] in w.pre:
        print(str(i) + " pre found")
        score = score * 5
        score = score * w.data.count(i) * len(w.data)
        if randFlag:
            score = score * randint(1000, 1100)
    return score
    
def create(length, data, params = parameters):
    sent = []
    scorecard = []
    length = int(length)
    for i in range(length):
        poss = []
        for w in data.words:
            rmin = int(avg(w.data) - sdev(w.data))
            rmax = int(avg(w.data) + sdev(w.data))
            if i in range(rmin, rmax + 1):
                poss.append(w)
        maxScore = 0
        winner = ""
        for w in poss:
            n = score(w, i, sent, True)
            print(w.string + " " + str(n))
            if n > maxScore:
                print(w.string + " got a new high score==================")
                maxScore = n
                winner = w.string
        sent.append(winner)
        scorecard.append(n)
    sent = " ".join(sent)
    sent = sent.capitalize()
    sent += "."
    return [sent, scorecard]
        