"""
Names are case-sensitive (month is not the same as Month).

A name begins with a letter or an underscore, followed by letters, digits or underscores (e.g., user_name, score1, _count).

A name cannot start with a digit (for example, 2q is invalid).

A name must not be a keyword.
"""
month = 12
print(type(month))  # <class 'int'>

month = "December"
print(type(month))  # <class 'str'>

a = 10
b = a  # b is 10

# data types
# float, double
# int, boolean, array
array = [1, 2, 3, 4]
num = 12.23
