1.find all occurence of substring in the given string?

In [5]:

str1="what we think we become,what it is"

str1.find("we")

Out[5]:

5

In [2]:

str1.rfind("we")

Out[2]:

24

In [4]:

str1.count("we")

Out[4]:

3

In [6]:

str1.find("what")

Out[6]:

0

In [7]:

str1.rfind("what")

Out[7]:

24

In [8]:

str1.count("what")

Out[8]:

2

In [11]:

str1.index("we")

Out[11]:

5

In [10]:

str1="what we think we become,what it is"

str1.find("we")

str1.rfind("we")

str1.find("what")

str1.rfind("what")

print(str1)

what we think we become,what it is

lower and upper functions

In [19]:

str1="python"

str2="programmer"

str3="letsupgrade"

str4="batchsix"

str1.upper()

Out[19]:

'PYTHON'

In [23]:

str5=str2.upper()

print(str5)

PROGRAMMER

In [15]:

str3.upper()

Out[15]:

'LETSUPGRADE'

In [20]:

str4.upper()

Out[20]:

'BATCHSIX'

In [21]:

str1.islower()

Out[21]:

True

lower functions

In [26]:

str1="PYTHON"

str2="PROGRAMMER"

str3="LETSUPGRADE"

str4="BATCHSIX"

str1.lower()

Out[26]:

'python'

In [27]:

str2.lower()

Out[27]:

'programmer'

In [28]:

str3.lower()

Out[28]:

'letsupgrade'

In [29]:

str4.lower()

Out[29]:

'batchsix'

In [30]:

str1.isupper()

Out[30]:

True