# Barrel of Monkeys <sup>&reg;</sup>

![Monkeys](images/BarrelOfMonkeys.gif "Monkeys!")


Do you remember the classic Barrel of Monkeys game?

Imagine a long chain of such monkeys where each monkey is coloured
either blue (B), red (R), yellow (Y) or green (G).

Find the most frequently occurring color pattern of a given length.
For example, in the chain  ‘BGGRYBRYGGRY’, the pattern ‘GGRY’ appears twice.

Pattern length: k=4

*Hint:*
The different patterns can be obtained by sliding a window along the original chain.

```python
s = "Python syntax highlighting"
print s
```

*Hint:*
*Brute force* scan the entire string again, for each pattern.
