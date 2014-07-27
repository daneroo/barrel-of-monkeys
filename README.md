# Barrel of Monkeys<sup>&reg;</sup>

![Monkeys](images/BarrelOfMonkeys.gif "Monkeys!")


Do you remember the classic Barrel of Monkeys<sup>&reg;</sup> game?

Imagine a long chain of such monkeys where each monkey is coloured
either blue (B), red (R), yellow (Y) or green (G).

**Find the most frequently occurring color pattern of a given length (*k*).**

For example, in the chain  `BGGRYBRYGGRY`, the pattern `GGRY` appears twice.

*Hint:*
The different patterns can be obtained by sliding a window along the original chain.

*For a chain of length `n` and pattern length `k`, there will be `n-k+1` of these*

```python
chainOfMonkeys = 'BGGRYBRYGGRY'
n = len(chainOfMonkeys)
k = 4

for i in range(len(chainOfMonkeys)-k+1):
    pattern = chainOfMonkeys[i:i+k]
```
*Hint:*
We can refactor this pattern traversal with a generator function.
```python
def patterns(chain):
    for i in range(len(chain)-k+1):
        yield chain[i:i+k]

for pattern in patterns(chainOfMonkeys):
    print 'examining %s' % pattern
```


*Hint:*
*Brute force*; for each such pattern we could simply count the number of occurences by traversing the entire chain again.

```python
for pattern in patterns(chainOfMonkeys):
    count=0;
    for posibleMatch in patterns(chainOfMonkeys):
        if pattern==posibleMatch:
            count+=1;
    print 'Found %d occurences of %s' % (count,pattern)
```
