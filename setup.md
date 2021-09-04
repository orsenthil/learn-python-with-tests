# Setup

Setup Python for working with this book. 

In this book, we will setup the Python interpreter from source using python.org website.

## Linux

Here are different methods to setup Python for your linux distribution.

### Ubuntu

We make sure that source packages are enabled in the repo. The file `/etc/apt/sources.list` lists all the source 
packages.

For bionic, we enable it using the command.

```
deb-src http://archive.ubuntu.com/ubuntu/ bionic main
```

Then we install the source dependencies.

```
sudo apt-get update
sudo apt-get build-dep python3.8
```

Download Python from python.org

```
curl -O https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
tar xvf Python-3.8.1.tgz
```

Build Python

```
cd Python-3.8.1/
./configure
make
```

Check the version of Python

```
$ ./python --version
Python 3.8.1
```

Let us setup a virtual environment with the interpreter.

```
$ mkdir ~/pyvenvs
$ ./python -m venv --copies ~/pyvenvs/learn-python-with-tests
$ source ~/pyvenvs/learn-python-with-tests/bin/activate
(learn-python-with-tests) $ python --version
Python 3.8.1
```

Let us install the two utilities that will use in this book.

Let us install static type checker, `mypy`.

```
pip install --upgrade mypy
```

And install testing tool and the library `pytest` We wont be using `pytest` in this tutorial,
we will use it as test runner.

```
pip install --upgrade pytest
```


