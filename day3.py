import string
low = { v:i for i,v in enumerate(string.ascii_lowercase,start=1) }
up = { v:i for i,v in enumerate(string.ascii_uppercase,start=27) }
low.update(up)
lst = []
with open('rucksaws','r') as f:
    data = f.read()
    for i in data.split('\n'):
        try:
            s1 = set(i[:int(len(i)/2)])
            s2 = set(i[int(len(i)/2):])
            lst.append(low[s1.intersection(s2).pop()])
        except:
            pass
print('Total of priority: ',sum(lst))
