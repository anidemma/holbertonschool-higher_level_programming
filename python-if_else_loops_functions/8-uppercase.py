#!/usr/bin/python3
def uppercase(str):
    string = ''
    for let in str:
        asci = ord(let)
        if asci in range(97,123):
            uppr = chr(asci - 32)
            string += uppr
        else:
            string += chr(asci)
        print("{}".format(string))
