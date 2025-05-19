# Heron's algorithm, explained, and shown in python.

Here's something they don't teach you at school, heron's algorithm.
The formula's very simple, really, but it's surprisingly efficient at approximating square roots.
The easiest way to explain it is with an example.
Lets say, you want to find the square root of 2. Assign 2 as x.
First, guess at what the square root is, say 1. Assign this to a variable. Let's call it 'a'.
Now, to get a better approximation, follow the formula (a + x / a) / 2.
Rinse, wash and repeat until you are satisfied with the approximation.

## Why does this work?

To simply put, what we're doing here, is taking the average of our guess, and the number we're trying to find the square root of divided by our guess.
This can only put out two possibilities, either it will be the average of a underestimation and an overestimation or vice versa.

### The code:

```python
from random import randint
from decimal import Decimal


def sqrt(x: Decimal, steps: int) -> Decimal:
    """
    Aproximate the square root of x using Heron's method, with more steps equivalent to more precision
    """

    approx = Decimal(randint(1, int(x + 1)))
    while steps != 0:
        approx = (approx + x / approx) / 2
        steps -= 1
    return approx


print(
    "Asserting that the function, when steps is 100, produces the same result for the square root of 2 as the decimal module."
)
assert sqrt(Decimal("2.0"), 100) == Decimal("2.0").sqrt()
print("Since this print statement was reached, the test passed.")
```

As you can see, Heron's method is so accurate that it produces the same result as the decimal module in only 100 steps.
Heron's method is used basically worldwide by almost every computer to compute square roots. And it's simplicity and accuracy is what makes it so popular.

[Previous Page](Entry9.md) [Next Page](Entry11.md)
