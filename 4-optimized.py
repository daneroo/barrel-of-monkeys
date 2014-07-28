
chainOfMonkeys = 'BRGYYGRBYGYRGRBYGBYGRBYGBGBGRY'
k = 4

def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

def mostFrequentPatterns(chain,k):
    maxFreq=0
    mostFrequentPatterns = set()
    counts = {}
    for pattern in patterns(chainOfMonkeys,k):
        if pattern in counts:
            counts[pattern] += 1
        else:
            counts[pattern] = 1

        if counts[pattern] == maxFreq:
            mostFrequentPatterns.add(pattern)
        elif counts[pattern] > maxFreq:
            maxFreq = counts[pattern]
            mostFrequentPatterns = set([pattern])

    return maxFreq,mostFrequentPatterns

maxFreq, mostFrequentPatterns = mostFrequentPatterns(chainOfMonkeys,k)
print 'The patterns %s each occur %d times' % (','.join(mostFrequentPatterns),maxFreq)
