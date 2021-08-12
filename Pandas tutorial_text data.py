import pandas as pd
import numpy as np

"""
1) lower() & upper() - Converts the string in Series to lower and upper case
2) len() - Computes the string length
3) strip() - Excludes the white space before and after the words
4) split("") - split each string with the given pattern
5) cat(sep=" ") - Concatenates the string with the given seperator
6) get_dummies() - Returns the DataFrame with One-Hot Encoded values.
7) contains(pattern) - Returns a Boolean value True for each element if the substring contains in the element, else False.
8) replace(a,b) - replace a with b
9) repeat(value) - repeat each element specific number of times
10) startswith(pattern) - returns Boolean if the string starts with the given pattern
11) endswith(pattern) - returns Boolean if the string ends with the given pattern
12)find(pattern) - returns the position of the pattern located in the string. Returns -1 if the pattern is not present
13) findall(pattern) - returns a list of that pattern if found. Else returns an empty list
14) swapcase() - used to change the case of the string
15) islower() , isupper(), isnumeric() - used to check the respective conditions 
"""

d1=pd.Series(data=['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print(d1)
#lower case
print(d1.str.lower())
#upper case
print(d1.str.upper())
#length of each string
print(d1.str.len())
#split
print(d1.str.split(" "))
#get dummies
print(d1.str.get_dummies())
#check for a keyword
print(d1.str.contains("A"))
#replace a word
print(d1.str.replace('@','$'))
#repeat the values
print(d1.str.repeat(2))
#count
print("Number of m in each string is:\n {a}".format(a=d1.str.count('m')))



