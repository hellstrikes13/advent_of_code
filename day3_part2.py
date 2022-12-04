import string
import itertools
low = { v:i for i,v in enumerate(string.ascii_lowercase,start=1) }
up = { v:i for i,v in enumerate(string.ascii_uppercase,start=27) }
low.update(up)
lst = []
n = 3
with open('rucksaws','r') as f:
    for line1,line2,line3 in itertools.zip_longest(*[f]*n):
        try:
            lst2 = []
            lst2.append(set(line1.strip()))
            lst2.append(set(line2.strip()))
            lst2.append(set(line3.strip()))
            lst.append(low[lst2[0].intersection(lst2[1].intersection(lst2[2])).pop()])
        except:
            pass
print(lst,'Total of priority: ',sum(lst))
