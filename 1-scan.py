
chainOfMonkeys = 'BRGYYGRBYGYRGRBYGBYGRBYGBGBGRY'
k = 4

for i in range(len(chainOfMonkeys)-k+1):
    pattern = chainOfMonkeys[i:i+k]

def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

for pattern in patterns(chainOfMonkeys,k):
    print 'examining %s' % pattern

