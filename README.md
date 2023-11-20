# PythonPasswordGenerator
A Python Password Generator based on Secrets and Strings

Based on https://docs.python.org/3/library/secrets.html#recipes-and-best-practices

and https://docs.python.org/3/library/string.html

In default configuration requires 1 upper, 1 lower, 1 numeric, and 1 character. 

Modification example: change to this code to require 3 or more numeric characters. 
```python
...
and sum(c.isdigit() for c in password) >= 3
...
```
