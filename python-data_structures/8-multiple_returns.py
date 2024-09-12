#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        tuple = (len(sentence), sentence[0])
    else:
        tuple = (0, None)

    return tuple
