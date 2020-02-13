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

def gcd(A :int, B : int) -> int:
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

Now, this brings the ultimate question, we are doing `A % B` twice and storing it in the variable `R`.  Can we
refactor this further so that we dont repeat ourselves here?

Yes, this is possible.

When will R *always be* 0 for the values of A and B?  We will call this condition as an (Invariant)[https://en.wikipedia.org/wiki/Invariant_(mathematics)]

1. When B divides A. 
    - This is the situation we already test for, and applies for infinite values of A, and B. So this cannot be an
     invariant.
     
2. When B is 0.

The '%' operation is about finding the remainder when B divides A. When B is 0, the division will result in
 `ZeroDivisionError` in Python. This is not a good condition to check.
 
Let's verify few examples.

```
>>> 10 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 152 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> -1 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 
```

3. When A is 0.
   - In the operation, A % B, when A is 0, the result always seems to be 0.

```
>>> 
>>> 0 % 1
0
>>> 0 % 100
0
>>> 0 % -1
0
>>> 

```

So, this seems like the answer for the question - "When will R *always be* 0 for the values of A and B?"

And the statements

```
    R = A % B
    while R != 0:
```

could be substituted with

```
    while A != 0:

```

And keeping the return value `B` same.

### Exercise Tests

Let's try the program now

```python

def gcd(A :int, B : int) -> int:
    while A != 0:
        A = B
        B = R
        R = A % B

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()

```

This will result in a error.

```
Traceback (most recent call last):
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 17, in <module>
    test_gcd()
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 12, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test6.py", line 5, in gcd
    B = R
UnboundLocalError: local variable 'R' referenced before assignment
```

We don't have R, and we used a variable `R` which is not bound to any value.
We get this Error because, we use `R` in the next step. If we had eliminated the usage of R.

```python

def gcd(A :int, B : int) -> int:
    while A != 0:
        A = B
        B = R
        A = A % B

    return B

```

We will get, a `NameError` instead.

```
/home/senthil/anaconda3/envs/xtoinfinity/bin/python /home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py
Traceback (most recent call last):
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 16, in <module>
    test_gcd()
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 11, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 4, in gcd
    B = R
NameError: name 'R' is not defined
```


Our R was supposed to be `A % B`. Let us fix tha error by substituting `R` with `A % B`.


```python
def gcd(A :int, B : int) -> int:
    while A != 0:
        A = B
        B = A % B
        R = A % B

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"
```

This should have eliminated the `UnboundLocalError` problem. And the variable `R` is unused.
But running the program now gives


```
python /home/senthil/github/learn-python-with-tests/gcd/gcd_test7.py
Traceback (most recent call last):
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test7.py", line 17, in <module>
    test_gcd()
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test7.py", line 12, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test7.py", line 6, in gcd
    R = A % B
ZeroDivisionError: integer division or modulo by zero
```

Perhaps, it was the redundant `R` ? Let's eliminate that.

```
def gcd(A :int, B : int) -> int:
    while A != 0:
        A = B
        B = A % B
    return B

def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"
```


And this will still give the same `ZeroDivisionError` at the line

```
python /home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py
Traceback (most recent call last):
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 16, in <module>
    test_gcd()
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 11, in test_gcd
    assert gcd(12, 16) == 4, "GCD was incorrect."
  File "/home/senthil/github/learn-python-with-tests/gcd/gcd_test9.py", line 5, in gcd
    B = A % B
ZeroDivisionError: integer division or modulo by zero
```

* `A % B` is giving us the ZeroDivisionError because B is zero.
*  `A = B` was present the previous step. So, A must be 0 too.
* The program would have exited, but when is A, but we failed ahead of that step.

What is really happening is, when we subsituted `R` in the previous step.

```
        A = B
        B = R
```

With

```
        A = B
        B = A % B
```

This was essentially

```
        A = B
        B = B % B
```

And B was 0. This was a costly mistake.

So, let us retrace our steps back, and try again for fixing the program with `UnboundLocalError` so that correct
 substitution happens.

```python

def gcd(A :int, B : int) -> int:
    while A != 0:
        A = B
        B = R
        R = A % B

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"


if __name__ == '__main__':
    test_gcd()

```

1. If A divided by B is 0, then GCD is B.
   - If A is 0, then GCD is B.
2. Otherwise, calculate Reminder R of A divided by B. (R = A mod B). 
3. Find out GCD(B, R), that is subsitute B for A, R and R for B, go to step 1 which calculates GCD.
   
   

```python

def gcd(A :int, B : int) -> int:
    while A != 0:

        R = A % B
        B = A
        A = R

    return B


def test_gcd():
    assert gcd(12, 16) == 4, "GCD was incorrect."
    assert gcd(4, 2) == 2, "GCD was incorrect"

```

This will give an error.

```

    assert gcd(12, 16) == 4, "GCD was incorrect."
AssertionError: GCD was incorrect.
```

This is because 12 is smaller than 16. and 12 % 16 will be 12.

We will always want to make sure in the calculation of `A % B`, that, A is smaller than B.

# Continue...


## Final Code

The final solution looks like this. And this works for number in any order.

```python

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def main():
    print(gcd(2, 4))
    print(gcd(4, 2))
    print(gcd(12, 16))
    print(gcd(16, 12))

if __name__ == '__main__':
    main()
```
