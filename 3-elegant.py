
chainOfMonkeys = 'BRGYYGRBYGYRGRBYGBYGRBYGBGBGRY'
k = 4

def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

def patternFrequency(chain,k):
    counts = {}
    for pattern in patterns(chainOfMonkeys,k):
        if pattern in counts:
            counts[pattern] += 1
        else:
            counts[pattern] = 1
    return counts

frequencies = patternFrequency(chainOfMonkeys,k)
maxFreq = max(frequencies.values())
mostFrequentPatterns = [p for p in frequencies.keys() if frequencies[p]==maxFreq]

print 'The patterns %s each occur %d times' % (','.join(mostFrequentPatterns),maxFreq)
