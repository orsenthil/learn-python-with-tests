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
2. Otherwise, calculate Reminder R of A divided by B. (R = A mod B). 
3. Find out GCD(B, R), that is subsitute B for A, R and R for B, go to step 1 which calculates GCD.

The explanation of this euclid algorithm explained well by Alexander Bogomolny in his [cut the knot](http://www.cut-the-knot.org/blue/Euclid.shtml)

Problem Credits: Think Python Exercise, SICP, and 
[Euclid's Algorithm](https://mathcs.clarku.edu/~djoyce/java/elements/bookVII/propVII2.html).

### Write tests first.

We will skip past the undefined `NameError` and for an undefined `gcd` function and write a `gcd` function that
 returns a 0.
 
```python

def gcd(A :int, B : int) -> int:
    return 0


def test_gcd():
    gcd(12, 16) == 4, "GCD was incorrect."
```
 
### Exercise tests.

Exercising this test, we get the AssertionError.

```python

Traceback (most recent call last):
  File "gcd/gcd_test1.py", line 10, in <module>
    test_gcd()
  File "gcd/gcd_test1.py", line 6, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
AssertionError: GCD was incorrect.

```

### Fix tests.

Let's follow the Euclid's algorithm to fix the tests.

```python

def gcd(A :int, B : int) -> int:
    if A % B == 0:
        return B

    R = A % B

    while R != 0:
        A = B
        B = R
        R = A % B
        if R == 0:
            return B
```

The program follows our understanding of the Euclid's algorithm.

And exercising the test showed that the program worked properly.


```
$ python gcd/gcd_test2.py  -v
$
```

### Refactor

There are a few avenues for refactor in the above code.
The first one is, return statement.

```
if R == 0:
   return B
```

If the variable `R`  is 0, then our `while` loop will exit and we could utilize that fact to return our result.

```python

def gcd(A : int, B : int) -> int:
    if A % B == 0:
        return B

    R = A % B

    while R != 0:
        A = B
        B = R
        R = A % B

    return B
```

And then, if we observe carefully, the first statement can be removed. Because we are calculating `A % B` and comparing
it with 0.


```python

def gcd(A :int, B : int) -> int:
    R = A % B
    while R != 0:
        A = B
        B = R
        R = A % B

    return B
```

Could we refactor this further?  Yes, our verification for for step 1 can be made in the while statement itself.

```python

def gcd(A :int, B : int) -> int:
    while (A % B) != 0:
        A = B
        B = R
        R = A % B

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"

```

Exercising this will result in an Error.


```
/home/senthil/anaconda3/envs/xtoinfinity/bin/python /home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py
Traceback (most recent call last):
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 17, in <module>
    test_gcd()
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 12, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 5, in gcd
    B = R
UnboundLocalError: local variable 'R' referenced before assignment
```

The error indicates that we use the variable `R` ahead of its assignment.  Our logical usage is incorrect as well.
We can correct the code as per the algorithm above.

```python

def gcd(A :int, B : int) -> int:
    while (A % B) != 0:
        R = A % B
        A = B
        B = R

    return B
```

And exercise this code results in a success.

At this moment, I decided to stop because any further refactoring, like calculating `A % B` only once will lead to
 edge cases, which can be confusing.
 
The code follows our algorithm to the dot, and easy to remember.


## Final Code

The final solution looks like this. And this works for number in any order.

```python

def gcd(A :int, B : int) -> int:
    while (A % B) != 0:
        R = A % B
        A = B
        B = R

    return B


def test_gcd():
    assert gcd(16, 12) == 4, "GCD was incorrect"
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"
    assert gcd(2, 4) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()
```
