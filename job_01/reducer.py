import sys

last_key = None
curr_count = 0
curr_key = None

for line in sys.stdin:
    line = line.strip()
    if line != '':
        curr_key, count = eval(line)
        curr_key = "(\"{}\", {})".format(str(curr_key[0]), str(curr_key[1]))
        count = int(count)

        if last_key == curr_key:
            curr_count += count
        else:
            if last_key:
                print("({}, {})".format(str(last_key), int(curr_count)))
            curr_count = count
            last_key = curr_key

if last_key == curr_key:
    print("({}, {})".format(str(last_key), int(curr_count)))
