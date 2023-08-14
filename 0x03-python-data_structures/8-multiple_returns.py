#!/usr/bin/python3
def multiple_returns(sentence):
    t = (len(sentence), sentence[0])
    if sentence is None:
        t = (len(sentence), None)
    return t[0], t[1]
