# Strings

Strings are sequence of one or more characters in Python. Strings can be assinged to variables.

In python, strings 

1) Immutable 
2) Are objects that have methods associated with it.


Let us look at Python string properties through a problem statement.


## Problem Statement

Test if a given string is a palindrome.


### Write test - 1

```python
def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB")  == True
    assert is_a_palindrome("B") == Tru
```


### Exercise Test - 1

```
    def test_palindrome():
>       assert is_a_palindrome("ABBA") == True
E       NameError: name 'is_a_palindrome' is not defined


```

### Fix Test - 1

```python
def is_a_palindrome(term) -> bool:
    return False


def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB")  == True
    assert is_a_palindrome("B") == True
```

### Exercise Test - 2

```
    def test_palindrome():
>       assert is_a_palindrome("ABBA") == True
E       AssertionError: assert False == True
E        +  where False = is_a_palindrome('ABBA')

strings/palindrome_2.py:6: AssertionError
```


### Fix Test - 2

```
def is_a_palindrome(term) -> bool:
    reversed_term = term[::-1]
    if reversed_term == term:
        return True
    return False


def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB")  == True
    assert is_a_palindrome("B") == True
    assert is_a_palindrome("NOT") == False
```

### Exercise Tests - 2

```
strings/palindrome_3.py .                                                                                                                                                                                                                                         [100%]

1 passed in 0.01s 

```

### Refactor 

```
def is_a_palindrome(term) -> bool:
    return term == term[::-1]


def test_palindrome():
    assert is_a_palindrome("ABBA") == True
    assert is_a_palindrome("BOB") == True
    assert is_a_palindrome("B") == True
    assert is_a_palindrome("NOT") == False

```


