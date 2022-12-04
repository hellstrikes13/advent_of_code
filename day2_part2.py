d = { 'rock' : 'X' , 'paper':'Y' ,'scissor' : 'Z' }
val = { 'X': 1, 'Y': 2, 'Z': 3 }
'''
A Y
B X
C Z
Rock defeats Scissors,
Scissors defeats Paper,
Paper defeats Rock.
X lose, Y draw,  Z win
'''
with open('rocks','r') as f:
    data =  f.read()
    print(data)
    w1 = []
    l1 = []
    draw = []
    for j in data.split('\n'):
        try:
            opp = j.split(' ')[0]
            me = j.split(' ')[1]
            print('opp: ',opp,'me: ',me)
            if me == d['paper']:
                ''' Y: i m gonna draw this round '''
#                print('entered draw block')
                if opp == 'A':
                    me = d['rock']
                if opp == 'B':
                    me = d['paper']
                if opp == 'C':
                    me = d['scissor']
                v1 = val[me]
                print('v1: ',v1)
                draw.append(3+v1)
            elif me == d['rock']:
                '''X: i m gonna loose this round '''
#                print('entered loose block')
                if opp == 'A':
                    me = d['scissor']
                if opp == 'B':
                    me = d['rock']
                if opp == 'C':
                    me = d['paper']
                v2 = val[me]
                print('v2: ',v2)
                l1.append(0+v2)
            elif me == d['scissor']:
                '''Z: i m gonna win this round '''
#                print('entered win block')
                if opp == 'C':
                   me = d['rock']
                if opp == 'B':
                   me = d['scissor']
                if opp == 'A':
                   me = d['paper']
                v3 = val[me]
                print('v3: ',v3)
                w1.append(6+v3)
            else:
                 print ('gl')
        except:
            pass
#    print('win: ',w1 , 'loose: ', l1 ,'draw: ',draw)
    l1.extend(draw)
    w1.extend(l1)
    print('Part 2 ans: ',sum(w1))
