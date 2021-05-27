import sys

for line in sys.stdin:
    line = line.strip()
    (word, doc_id), (count, words_per_doc) = eval(line)
    print("\"{}\", {}".format(word, line.strip()))
