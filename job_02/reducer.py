import sys

words_per_doc = {}
lines = []

for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    doc_id, word_count = eval(line)

    if doc_id not in words_per_doc:
        words_per_doc[doc_id] = int(word_count[1])
    else:
        words_per_doc[doc_id] += int(word_count[1])

for line in lines:
    doc_id, word_count = eval(line)
    print("((\"{}\", {}), ({}, {}))".format(str(word_count[0]), doc_id, int(word_count[1]), int(words_per_doc[doc_id])))
