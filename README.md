# Barrel of Monkeys<sup>&reg;</sup>

![Monkeys](images/BarrelOfMonkeys.gif "Monkeys!")


Do you remember the classic Barrel of Monkeys<sup>&reg;</sup> game?

Imagine a long chain of such monkeys where each monkey is coloured
either blue (B), red (R), yellow (Y) or green (G).

**Find the most frequently occurring color pattern of a given length (*k*).**

For example, in the chain  `BGGRYBRYGGRY`, the pattern `GGRY` appears twice.

#### *Hint:*
The different patterns can be obtained by sliding a window along the original chain.

*For a chain of length `n` and pattern length `k`, there will be `n-k+1` of these patterns*

```python
chainOfMonkeys = 'BGGRYBRYGGRY'
n = len(chainOfMonkeys)
k = 4

for i in range(len(chainOfMonkeys)-k+1):
    pattern = chainOfMonkeys[i:i+k]
```
#### *Hint:*
We can refactor this pattern traversal with a generator function. This makes our intention clearer, and makes the chain traversal reusable.

```python
def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

for pattern in patterns(chainOfMonkeys,k):
    print 'examining %s' % pattern
```


#### *Hint: Brute force approach*
In order to determine the frequency of each pattern,
we could simply count the number of occurences by traversing the entire chain again.

```python
for pattern in patterns(chainOfMonkeys):
    count=0;
    for posibleMatch in patterns(chainOfMonkeys):
        if pattern==posibleMatch:
            count+=1;
    print 'Found %d occurences of %s' % (count,pattern)
```

This approach has a few drawbacks. 
* If a pattern occurs more than once, we will actually scan the entire chain multiple times counting the same pattern.
* Secondly this has a complexity of `O(n<sup>2</sup>)`, and we can probably do better.

#### *Hint:*
If we used a dictionary, with the patterns as keys, we could count the number of occurences as we perform a single traversal.

```python
def patternFrequency(chain,k):
    counts = {}
    for pattern in patterns(chainOfMonkeys,k):
        if pattern in counts:
            counts[pattern] += 1
        else:
            counts[pattern] = 1
    return counts
```
 and then simply inspect the accumulated counts the find the maximally occuring patterns:
```python
frequencies = patternFrequency(chainOfMonkeys,k)
maxFreq = max(frequencies.values())
mostFrequentPatterns = [p for p in frequencies.keys() if frequencies[p]==maxFreq]

print 'The patterns %s each occur %d times' % (','.join(mostFrequentPatterns),maxFreq)
```

#### *Hint:*
If we wanted to avoid traversing the dictionary of pattern occurences, we could maintain the maximal observed frequency as we traverse the chain.

#### *Motivation:*
This problem has analogues in bioinformatics; where we might be interested in finding commonly occurring nucleotide patterns in a genome sequence. Think `GATTACA-AGTCGGTCGAACGA`

### *Final Solution:*
Our final solution has `O(n)` complexity in time. In terms of space the maximal size of the dictionary of counts is `min(O(4<sub>k</sup>),O(n))`

```python
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
```
 
This yields the following output
```bash
iterviewCake$ python 4-optimized.py
The patterns GRBY,RBYG each occur 3 times
```

