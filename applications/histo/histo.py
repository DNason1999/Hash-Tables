# Implement me.
import re

def histo(filename):
    data = None
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except Exception as e:
        return None
    
    print("regexing")

    data = re.sub("[\"\:;,\.\-\+=/\\\|\[\]\{\}\(\)\*\^&]", "", data)

    print("printing")
    data = data.split()
    
    counts = {}
    for x in data:
        x = x.lower()
        if x not in counts:
            counts[x] = 0
        counts[x] += 1

    counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)
    counts = {x[0]:x[1] for x in counts[:20]}

    for key, value in counts.items():
        print(key, end='\t\t')
        for x in range(0,value):
            print('#', end='')

        print()

filename = 'robin.txt'
histo(filename)
