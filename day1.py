with open('/Users/sudeep.melekar/elves','r') as f:
    data = f.read()
    lst = []
    maxy = []
    l = list(data.split('\n'))
    for i in l:
        if i != '':
            lst.append(i)
        else:
            print ('ho ho ho')
            maxy.append(sum(list(map(int,lst))))
            lst = []
    print('elves having highest calories: ',max(maxy))
    print('top 3 elves total calories:', sum(sorted(maxy)[-3:]))
