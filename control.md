# Control Statements

Control statements provide the facility to switch the flow of control in a program. Python provides a few control
 statements like `if-else`, `while` and `for`.
 
* `if-else` is for conditional switching of the control.

* `for` and `while` for doing something repeatedly.

Almost all programs utilize these control statements to accomplish the task at hand or to solve the given problem.

## Problem and Solution.

Let's demonstrate a while loop using Euclid's algorithm for finding the greatest common
divisor.

The greatest common divisor (GCD) of two numbers, is the largest number that divides both of them without leaving a
 remainder. As given in this example from [Math is Fun](https://www.mathsisfun.com/greatest-common-factor.html) the
  greatest common divisor of 12 and 16 is 4.
 
![gcd](https://i.imgur.com/BOIPxQu.png)
 

An efficient way to formulate GCD was given by Euclid.

To find the GCD of A, B, given A > B.

1. If A divided by B is 0, then GCD is B.
2. Otherwise, calculate Reminder R of A divided by B. (R = A mod B). Find out GCD(B, R)
3. When R is 0, terminate and return B. This is same as step 1.

The explanation of this euclid algorithm explained well by Alexander Bogomolny in his [cut the knot](http://www.cut-the-knot.org/blue/Euclid.shtml)

Problem Credits: Think Python Exercise, SICP, and 
[Euclid's Algorithm](https://mathcs.clarku.edu/~djoyce/java/elements/bookVII/propVII2.html).

### Write tests first.

```python

def gcd(A :int, B : int) -> int:
    return 0


def test_gcd():
    gcd(12, 16) == 4, "GCD was incorrect."
```
### Exercise tests.

### Fix tests.

```python
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
```

### Refactor

And Repeat


## Final Code


