import sys
import os
import re

stopwords = open('stopwords.txt').read().split('\n')
curr_file = ""
doc_id = 0

for line in sys.stdin:
    filename = os.getenv('map_input_file')
    if curr_file != filename:
        curr_file = filename
        doc_id += 1

    line = line.lower().strip()
    line = re.sub(r"[^\w\s]", "", line)
    words = line.split()

    for word in words:
        is_digit = any(str.isdigit(c) for c in word)
        if len(word) > 3 and not is_digit and word not in stopwords:
            print("((\"{}\", {}), 1)".format(str(word), int(doc_id)))
