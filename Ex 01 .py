# First test from hackerRank (Learning Python)
import math
import os
import random
import re
import sys

def reversewordSentence( phrase ):
    word = phrase.split()
    revlist = word[::-1]
    revphrase = " ".join(revlist)
    return revphrase.swapcase()


print('write it amigoo')
phrase = input()
print(phrase)
print(reversewordSentence(phrase))
