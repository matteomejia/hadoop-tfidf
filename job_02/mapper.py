import sys
import os

for line in sys.stdin:
    line = line.strip()

    if line != '\n':
        word_docid, word_count = eval(line)
        print("({}, (\"{}\", {}))".format(word_docid[1], word_docid[0], word_count))
