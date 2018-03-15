# Python

Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. Python source code is automatically compiled into Python byte code by the CPython interpreter. Compiled code is usually stored in PYC (or PYO) files, and is regenerated when the source is updated, or when otherwise necessary.

## Built-in data types

### Boolean

```python
>>> # <class 'bool'>
>>> # Declaration:
>>> x = True
>>> y = False
```

### Numeric

#### Int 

```python
>>> # <class 'int'>
>>> # Non-limited length in Python 3.x
>>> 
>>> # Declaration:
>>> x = 1
```

#### Long

```python
>>> # <class 'long'>
>>> # Only python 2.x
>>> 
>>> # Declaration:
>>> x = 10L
```

#### Float

```python
>>> # <class 'float'>
>>> # Equivalent to C doubles
>>> 
>>> # Declaration:
>>> x = 10.0
```

#### Complex

```c
// In C :
typedef struct {
	double real;
	double imag;
} Py_complex;
```
```python
>>> # <class 'complex'>
>>> # Declaration:
>>> x = 2 + 3j
```

### Sequences

#### String

```python
>>> # <class 'str'>
>>> # Sequence of 8-bit characters in Python 2.x
>>> # Sequence of Unicode characters (ranges from U+0000 - U+10FFFF) in Python 3.x
>>> 
>>> # Declaration:
>>> x = "Hello World!"
```

#### Bytes

```python
>>> # <class 'bytes'>
>>> # Sequence of integers of 0-255 hexadecimal, Python 3.x only
>>> 
>>> # Declaration:
>>> x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
>>> # print(x.decode())
```

#### Bytearray

```python
>>> # <class 'bytearray'>
>>> # Like bytes but mutable, Python 3.x only
>>> 
>>> x = bytearray("Python Bytes", "utf8")
>>> # Or
>>> y = bytearray([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33])
```

#### List

```python
>>> # <class 'list'>
>>> # Mutable list of elements
>>>
>>> # Declaration:
>>> x = [10, "List", 9.9]
>>> # Empty list
>>> y = []
```

#### Tuple

```python
>>> # <class 'tuple'>
>>> # Immutable list of elements
>>>
>>> # Declaration:
>>> x = ("Winter", "Spring", "Summer", "Autumn")
>>> # Empty tuple
>>> y = ()
>>> # Singleton tuple
>>> z = ("Singleton tuple", )
```

### Sets

#### Set

```python
>>> # <class 'set'>
>>> # Unordered collection of unique and immutable objects
>>> # Although Sets are mutable
>>>
>>> # Declaration:
>>> x = set("Print this to see how a set is")
>>> # Or
>>> y = set([1, 2, "one", 3, 4, "two", 1, 2, "one"])
>>> # Empty set
>>> z = set()
```

#### Frozenset

```python
>>> # <class 'frozenset'>
>>> # Immutable Set
>>>
>>> # Declaration:
>>> alphabet = frozenset("abcdefghijklmnopqrstuvwxyz")
>>> # Or
>>> x = frozenset([1, 2, "one", 3, 4, "two", 1, 2, "one"])
>>> # Empty frozenset
>>> y = frozenset()
```

### Mappings

#### Dictionary

```python
>>> # <class 'dict'>
>>> # A dictionary is an Associative Array
>>>
>>> # Declaration:
>>> x = { "one":1 , "two":2 , "three":3}
>>> # Empty dictionary
>>> y = {}
```