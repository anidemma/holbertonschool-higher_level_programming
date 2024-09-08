#!/usr/bin/python3
def uppercase(str):
    string = ''
    for let in str:
        asci = ord(let)
        if (asci < 123 and asci > 96):
            uppr = chr(asci - 32)
            string += uppr
        else:
            string += chr(asci)
        print("{}".format(string))
