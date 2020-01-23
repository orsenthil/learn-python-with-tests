# Syntax Errors

In this book, and with the approach we are taking with test driven development,
we cannot accomodate Syntax Errors.

Syntax Errors are are kind of errors that does not follow the Rules of valid
python program

For instance there are rules of variable names like

1. Cannot start with a number
2. Should only have alpha-numeric characters, and "_"
3. Should not be a keyword of the language.

If we have a variable name with any of these, program will result in a syntax
error.


## Tests for Syntax Errors

```python
1var = "invalid variable name"
```

The error message will be

```
$ python syntax_errors/invalid_variable_1.py 
  File "syntax_errors/invalid_variable_1.py", line 2
    1var = "invalid variable name"
       ^
SyntaxError: invalid syntax
```

Another example invalid syntax.


```python
$var = "invalid variable name"
```

The output

```
  File "syntax_errors/invalid_variable_2.py", line 1
    $var = "invalid variable name"
    ^
SyntaxError: invalid syntax
```

It is interesting to note that `$` might be an allowed character in variable names in other languages.

A syntax error where we end up using a reserved key-word.

```python
class = "invalid variable name"

```

This will end up with the same Syntax Error.

```
$ python syntax_errors/invalid_variable_3.py 
  File "syntax_errors/invalid_variable_3.py", line 1
    class = "invalid variable name"
          ^
SyntaxError: invalid syntax
```

### Errors while overriding builtins

Keywords are the building blocks of the language.  Besides keywords, python includes set of `builtins` terms that any
which are defined already by the interpreter. Python will not through a SyntaxError for overriding a `builtin`, but
it will result in a unexpected run-time error or sometimes mysterious behavior.

Here is example program wherein we have overridden the `builtin` variable `len`.

```python
print(len("a string"))

len = len("a string")

print(len("a string"))
```

This the error printed by the program.

```
$ python syntax_errors/using_builtin_variable_4.py 
8
Traceback (most recent call last):
  File "syntax_errors/using_builtin_variable_4.py", line 5, in <module>
    print(len("a string"))
TypeError: 'str' object is not callable

```

The first time, `len` is used, it will give the length of the string, the second time, the `len` is used, it will
give a `TypeError` and not `SyntaxError`.

## Fixing Syntax Errors

```python

# the numbers can occur places other than begining of the variable name.
var1 = "invalid variable name"
v2ar = "valid"

# Only _ is the special character allowed

var_ = "valid"
var_name = "valid name"

# We should not be using keywords

no_keywords = "valid"


# We should not be overwriting a builtin

len_of_sentence = len("something")

```

And exercising this program will not give any syntax errors.

```
 python syntax_errors/test_without_syntax_errors.py 
```


### Keywords and builtins

The list of reserved by python keywords can be examined using the `help()` command in the interpreter.

* Go to the interactive `help()`
* Type `keywords`


```
$ python
Python 3.8.1 (default, Jan 11 2020, 10:10:32) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> 

```

Similarly, the builtins can be listed using the interpreter using the `dir()` call on `__builtins__`.


```
$ python
Python 3.8.1 (default, Jan 11 2020, 10:10:32) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__',
'__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs',
'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min',
'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit',
'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

```

Our test driven programs will not have a SyntaxError or errors due to overwriting builtin names.
These errors are easiest to catch and should be fixed immediately.




