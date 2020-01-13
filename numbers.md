# Numbers

Numbers are most common entities you will use when interacting with the computer. 
We represent numbers using numerical text in the editors, but store the numbers in variables.

Python is a dynamically typed language. We do not have declare a type of a variable before assigning any value to it.

## Problem and Solution.

Let's start with a simple exercise of finding if a year is a leap year

* A normal year has 365 days
* A leap year has 366 days.

A Leap year is a year 

* That is exactly divisible by 4. (2016, 2020, 2024)
** If divisible 100, then it is not. (2100, 2200, 2300)
*** If it is divisible by 400, then it is. (2000, 2400)

Refer to [Maths is Fun](https://www.mathsisfun.com/leap-years.html) for more information on leap years.


### Write tests first


```python

def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True
```


### Exercise Tests - 1

If we run pytest on this.

```

    def test_is_leap_year():
>       assert is_leap_year(2016) == True
E       NameError: name 'is_leap_year' is not defined

numbers/leap_year_1.py:3: NameError
=======================================
```

### Fix tests - 1

The NameError means that we have not defined our method yet. The error message clearly says that `is_leap_year` is
 not defined. So, let us define it.

```
def is_leap_year(param):
    pass


def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True
```

### Exercise tests - 2

Let us exercise the tests again.

```
$ pytest numbers/leap_year_2.py

    def test_is_leap_year():
>       assert is_leap_year(2016) == True
E       assert None == True
E        +  where None = is_leap_year(2016)

numbers/leap_year_2.py:6: AssertionError

```

This time the error message  means that our output is not equal to the expected value.

### Fix tests - 2

```

def is_leap_year(year: int) -> bool:
    """
    :param year Given year to test, whether it is a leap year
    :return: True if leap year, False otherwise
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    return False


def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True
```

### Exercise Tests - 2

```
$ pytest numbers/leap_year_3.py 
numbers/leap_year_3.py .                                              
```

Our tests are successful.

### Refactor

There are ways in which we could short-circuit the conditions. In this book, I want to emphasize that refactor for
code-repeatability, but keep the code as you understand it best. If you the conditions reflect what you are looking
for the code is complete.


## Final code

Here is the final code for the test leap year.

```python
def is_leap_year(year: int) -> bool:
    """
    :param year Given year to test, whether it is a leap year
    :return: True if leap year, False otherwise
    """

    # divisible by 4, True
    if year % 4 == 0:
        # divisible by 10, False
        if year % 100 == 0:
            # divisible by 400, True
            if year % 400 == 0:
                return True

            return False

        return True

    return False


def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

    assert is_leap_year(2019) == False
```

