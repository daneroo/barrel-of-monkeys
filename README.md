# Barrel of Monkeys<sup>&reg;</sup>

![Monkeys](images/BarrelOfMonkeys.gif "Monkeys!")


Do you remember the classic Barrel of Monkeys<sup>&reg;</sup> game?

Imagine a long chain of such monkeys where each monkey is coloured
either blue (B), red (R), yellow (Y) or green (G).

**Find the most frequently occurring color pattern of a given length (*k*).**

For example, in the chain  `BGGRYBRYGGRY`, the pattern `GGRY` appears twice.

*Hint:*

The different patterns can be obtained by sliding a window along the original chain.

*For a chain of length `n` and pattern length `k`, there will be `n-k+1` of these patterns*

```python
chainOfMonkeys = 'BGGRYBRYGGRY'
n = len(chainOfMonkeys)
k = 4

for i in range(len(chainOfMonkeys)-k+1):
    pattern = chainOfMonkeys[i:i+k]
```
*Hint:*

We can refactor this pattern traversal with a generator function. This makes our intention clearer, and makes the chain traversal reusable.

```python
def patterns(chain,k):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

for pattern in patterns(chainOfMonkeys,k):
    print 'examining %s' % pattern
```


*Hint:*

*Brute force approach*
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

*Hint:*
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
 
