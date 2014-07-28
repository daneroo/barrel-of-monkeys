
chainOfMonkeys = 'BRGYYGRBYGYRGRBYGBYGRBYGBGBGRY'
k = 4

def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

for pattern in patterns(chainOfMonkeys,k):
    count=0;
    for posibleMatch in patterns(chainOfMonkeys,k):
        # print 'comparing %s and %s' % (pattern,posibleMatch)
        if pattern==posibleMatch:
            count+=1;
    print 'Found %d occurences of %s' % (count,pattern)
