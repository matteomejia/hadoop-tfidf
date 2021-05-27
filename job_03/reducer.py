#!/usr/bin/python3

import sys
import math

df_t = {}
lines = []
all_doc_id = []

for line in sys.stdin:

    line = line.strip()
    word, ((word, doc_ID), (count, words_per_doc)) = eval(line)
    lines.append(line)

    if word not in df_t:
        df_t[word] = 1
    else:
        df_t[word] += 1

    if doc_ID not in all_doc_id:
        all_doc_id.append(doc_ID)

N = float(len(all_doc_id))

for line in lines:
    word, ((word, doc_ID), (count, words_per_doc)) = eval(line)

    tf_t_d = float(count)
    n_d = float(words_per_doc)
    df_t_val = float(df_t[word])

    tf_idf = ( tf_t_d / n_d ) * math.log10(N/df_t_val)

    print('(("%s", %s), %10.10f)' % (word, doc_ID, tf_idf))
