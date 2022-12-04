cnt = 0
with open('sections') as f:
    data = f.read()
    for i in data.split('\n'):
       try:
          a = int(i.split('-')[0])
          b = int(i.split('-')[1].split(',')[0])
          c = int(i.split('-')[1].split(',')[1])
          d = int(i.split('-')[-1])
#          print(a,b ,'----',c,d)
          s1 = set()
          s2 = set()
          for n in range(a,b+1):
              s1.add(n)
          for k in range(c,d+1):
              s2.add(k)
#          print('s1 Intersect s2 at: ',s1.intersection(s2))
          if (s1.intersection(s2)):
              cnt += 1
#          print('-----===------')
       except:
           pass
print('FINAL count: ',cnt)
