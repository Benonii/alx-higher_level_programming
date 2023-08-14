#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        t = (0, None)
    else:
        t = (len(sentence), sentence[0])
    return t[0], t[1]
