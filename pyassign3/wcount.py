#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Huang Yang"
__pkuid__  = "1700011776"
__email__  = "1700011776@pku.edu.cn"
"""

import sys
import re
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines=lines.lower()
    x1=re.findall('[a-zA-Z\'\-]+', lines)
    y1=list(set(x1))
    y2=[]
    for i in range(len(y1)):
        y2+=[x1.count(y1[i])]
    for i in range(topn):
        a=y2.index(max(y2))
        print(y1[a],max(y2))
        del(y2[a])
        del(y1[a])

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)