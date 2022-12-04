d1 = { 'rock' : 'A' , 'paper':'B' ,'scissor' : 'C' }
d2 = { 'rock' : 'X' , 'paper':'Y' ,'scissor' : 'Z' }
'''
1 for Rock, 2 for Paper, and 3 for Scissors
Rock defeats Scissors,  a > z
Scissors defeats Paper, c > y
Paper defeats Rock.     b > x
'''
with open('rk','r') as f:
    data =  f.read()
    w = []
    l = []
    d = []
    for i in data.split('\n'):
        try:
            opp = i.split(' ')[0]
            me = i.split(' ')[1]
            if opp == d1['rock'] and me == d2['rock']:
                d.append(3+1)
            elif  opp == d1['rock'] and me == d2['scissor']:
                l.append(0+3)
            elif opp == d1['rock'] and me == d2['paper']:
                w.append(6+2)
            elif opp == d1['paper'] and me == d2['paper']:
                d.append(3+2)
            elif opp == d1['paper'] and me == d2['rock']:
                l.append(0+1)
            elif opp == d1['paper'] and me == d2['scissor']:
                w.append(6+3)
            elif opp == d1['scissor'] and me == d2['scissor']:
                d.append(3+3)
            elif opp == d1['scissor'] and me == d2['rock']:
                w.append(6+1)
            elif opp == d1['scissor'] and me == d2['paper']:
                l.append(0+2)
            else:
                print('gl')
        except:
            pass
    print('win: ',w , 'loose: ', l ,'draw: ',d)
    l.extend(d)
    w.extend(l)
    print('Part 1 ans: ',sum(w))
