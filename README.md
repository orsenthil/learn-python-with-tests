# Learn Python with tests

This book introduces test driven development in Python. We follow a template while introducing the features of Python.

* Write tests first.
* Exercise tests.
* Fix tests.
* Refactor
* And Repeat

## Inspiration

This book is inspired from the work https://github.com/quii/learn-go-with-tests/ which introduces Go programming
 using similar pattern.
 
After reading this book, I felt that I could dwell into real-world go projects confidently. I wanted a similar book
 for Python, and thus, I decided to write this.

## Boiler plate code.

We want to learn Python without much overhead and dependencies. I wanted to make sure that section of the code
 can be copied to a filename and run with the python interpreter.
 
If the repetition annoys you, please excuse me, and skip ahead.

```python
# filename: test_hello.py

if __name__ == '__main__':
    pass
```

* `#` is the start of the comment.
* `#filename` indicates the filename for the snippet.
* The `if __name__ == '__main__' ` is a special secret that makes sure that python interpreter will execute the
  whatever comes after this line, only when invoked using `python` interpreter. We typically write the name of the
  tests after this to demonstrate it. 
   

## Hello, World

This first chapter can be studied with only python interpreter installed on your system. Please install the latest
 release of Python from https://www.python.org/downloads/ before we get started.
 
On my local system, the interpreter that I use is

```console
$ ./python 
Python 3.8.1 (default, Jan 10 2020, 06:25:32) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### Write tests first - 1

```python
# filename: test_hello.py

def test_hello() -> None:
    expected = "Hello, World!"
    actual = get_hello()
    assert actual == expected, "{actual} != {expected}".format(actual=actual, expected=expected)


if __name__ == '__main__':
    test_hello()
```


### Exercise tests - 1

* Run the tests

```

$ python test_hello.py 
Traceback (most recent call last):
  File "test_hello.py", line 11, in <module>
    test_hello()
  File "test_hello.py", line 6, in test_hello
    actual = get_hello()
NameError: name 'get_hello' is not defined
```

The `NameError` indicates we used a term that is not defined. We have not written our `get_hello` function yet
, so let us write it.

### Fix tests - 1

Let us write the `get_hello` method.

```python
def get_hello() -> None:
    pass


def test_hello() -> None:
    expected = "Hello, World!"
    actual = get_hello()
    assert actual == expected, "{actual} != {expected}".format(actual=actual, expected=expected)


if __name__ == '__main__':
    test_hello()
```

### Exercise tests - 2


```

$ python test_hello.py 
Traceback (most recent call last):
  File "test_hello.py", line 15, in <module>
    test_hello()
  File "test_hello.py", line 11, in test_hello
    assert actual == expected, "{actual} != {expected}".format(actual=actual, expected=expected)
AssertionError: None != Hello, World!
```

Now, we see a new error, `AssertionError`, which indicates our expected output and actual output were not matching.

### Fix tests - 2

Let us make sure that `get_hello` returns the string "Hello, World"

```python
def get_hello() -> str:
    return "Hello, World!"
```

The full test code will be

```python
# filename: test_hello.py


def get_hello() -> str:
    return "Hello, World!"


def test_hello() -> None:
    expected = "Hello, World!"
    actual = get_hello()
    assert actual == expected, "{actual} != {expected}".format(actual=actual, expected=expected)


if __name__ == '__main__':
    test_hello()
```

Running this will give no output indicating that our test was successful.

```
$ python test_hello.py 
```

### Refactor

This was a very simple introduction to writing a test and exercising it. We don't have anything to refactor. Rest of
 the book will present examples that will explain the need for refactoring the code after it is written.
 
## Chapters

* [Setup](setup.md)

