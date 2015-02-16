__author__ = 'eric'

# ActiveCode 18 (seq_char_classification): string module goodies

# PIP book doesn't allow use of string module - but we can here after import

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
x = "a"
y = "A"
print(x in string.ascii_lowercase)  # True
print(x in string.ascii_uppercase)  # False
print(y in string.ascii_lowercase)  # False
print(y in string.ascii_uppercase)  # True
