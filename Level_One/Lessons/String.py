"""
============================================================
############## String manipulation #########################
# Python version: 3.9.7
============================================================
"""

# Strings are used in Python to record text information, such as name. Strings
# in Python are actually a *sequence*, which basically means Python keeps track
# of every element in the string as a sequence. For example, Python understands
# the string "hello' to be a sequence of letters in a specific order. This means
# we will be able to use indexing to grab particular letters (like the first
# letter, or the last letter).
#
# This idea of a sequence is an important one in Python and we will touch
# upon it later on in the future.
#
# In this lecture we'll learn about the following:
#
#     1.) Creating Strings
#     2.) Printing Strings
#     3.) String Indexing and Slicing
#     4.) String Properties
#     5.) String Methods
#     6.) Print Formatting
#     7.) Some other String manipulation methods

# Creating a String
# To create a string in Python you need to use either
# single quotes or double quotes. For example:

# Import rich for terminal decoration which is just for fun, but rich is more than that
from rich.console import Console
from rich.table import Table

console = Console()

# Single word
'hello'

# Entire phrase
'This is also a string'

# We can also use double quote
"String built with double quotes"


# Be careful with quotes!
# ' I'm using single quotes, but will create an error'


# The reason for the error above is because the single quote in I'm stopped the
# string. You can use combinations of double and single quotes to get the complete statement.

"Now I'm ready to use the single quotes inside a string!"


# Now let's learn about printing strings!

# ## Printing a String
#
# Using the REPL with just a string in a cell will automatically output
# strings, but the correct way to display strings in your output is by using a print function.

# We can simply declare a string
'Hello World'

# note that we can't output multiple strings this way
'Hello World 1'
'Hello World 2'


# We can use a print statement to print a string.

print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')


# String Basics

# We can also use a function called len() to check the length of a string!

len('Hello World')


############################# STRING INDEXING AND SLICING #################################

# We know strings are a sequence, which means Python can use indexes to call
# parts of the sequence. Let's learn how this works.
#
# In Python, we use brackets [] after an object to call its index. We should
# also note that indexing starts at 0 for Python. Let's create a new object
# called s and the walk through a few examples of indexing.

# Assign s as a string
s = 'Hello World'

table = Table()
table.add_column('String indexing and slicing', justify="justify", style="bright_yellow", no_wrap=True)
table.add_row(s)
console.print(table)

# Let's start indexing!

# Show first element (in this case a letter)
print('First char of Hello World is ', s[0])

# Next element
print('Second char of Hello World is ', s[1])

# Next Element
print('Third char of Hello World is ', s[2])


## For the slicing, you must understand how things gonna work out here. This is the most important thing here ##
# We can use a : to perform *slicing* which grabs everything up to a designated point. For example:

# Grab everything past the first term all the way to the length of s which is len(s)
# It will return ello World
# It's like you are telling the slicing function where to go, 1 means it should go from 1 to len-1
print('Slice everything from index 1 to end: ', s[1:])

print('Slice everything from index 3 to end: ', s[3:])

# Note that there is no change to the original s
print('After slicing, there is no change to the original string: ', s)

# Grab everything UP TO the 3rd index
# And you can write it as s[0:3] which is just the same with s[:3]
print('First 3 chars of Hello World are: ', s[:3])


# Note the above slicing. Here we're telling Python to grab everything from
# 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in
# Python, where statements and are usually in the context of "up to, but not including".

# Everything
s[:]


# We can also use negative indexing to go backwards.
# Last letter (one index behind 0 so it loops back around)
# s[-1:] is actually this s[-1]
print('Last char of the string is: ', s[-1])

# Grab everything but the last letter
print('Grab everything but the last char is gone: ', s[:-1])


# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example:

# As you many know that, string is like an array in Python, char will be indexed just like array
# Grab everything, but go in steps size of 1
print('\n')
print('Print string forwards with step of 1', s[::1])
# String will be printed with step of 2 so indexes should go 0 2 4 ... 
print('Print string forwards with step of 2', s[::2])

# Print the string forwards but the first char
print('The first char is gone', s[1::1])

# We can use this to print a string backwards with step of 1
print('Reverse string: ', s[::-1])

print('\n')
# ## String Properties
# Its important to note that strings have an important property known as
# immutability. This means that once a string is created, the elements within
# it can not be changed or replaced. For example:

# Let's try to change the first letter to 'x'
# s[0] = 'x'

# Notice how the error tells us directly what we can't do,
# change the item assignment!
#
# Something we can do is concatenate strings!
s

# Concatenate strings!
s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

# We can use the multiplication symbol to create repetition!

letter = 'z'

letter*10


# ## Basic Built-in String methods
#
# Objects in Python usually have built-in methods. These methods are functions
# inside the object (we will learn about these in much more depth later) that
# can perform actions or commands on the object itself.
#
# We call methods with a period and then the method name. Methods are in the form:
#
# object.method(parameters)
#
# Where parameters are extra arguments we can pass into the method.
# Don't worry if the details don't make 100% sense right now. Later on we will
# be creating our own objects and functions!
#
# Here are some examples of built-in methods in strings:

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')

# There are many more methods than the ones covered here.

########################
### Print Formatting ###
########################

# We can use the .format() method to add formatted objects to printed string statements.
#
# The easiest way to show this is through an example:

'Insert another string with curly brackets: {}'.format('The inserted string')

# Using the string .format() method
# The best way to format objects into your strings for print statements is using
# the format method. The syntax is:
#
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
#
# Lets see some examples:


print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(
    a=1, b='two', c=12.3))


# That is the basics of string formatting!

##########################
### Some other methods ###
##########################
print('\n')

s = 'Hello World'
# Startswith / Endswith
# This will return Boolean type correspond with statement
print(s.startswith("H"), ' because Hello World starts with H')
print(s.endswith("H"), ' because Hello World does not end with H')

#Replacing
# I use print here to avoid our s from being replace with something else
print(s.replace("Hello", "Goodbye"))

#Strip
# This method will help you remove any character from both ends of the string
# There are 3 types: 
# strip(<parameter>) to remove a form of string from both ends
# lstrip(<parameter>) to remove a form of string from left side and forwards
# rstrip(<parameter>) to remove a form of string from right side and backwards

# override s 
s = ',,,,,rrttgg.....banana....rrr'

print('Stripping the input format from both sides of the string: ', s.strip('.,grt'))
print('Stripping the input format from left side of the string: ', s.lstrip('.,grt'))
print('Stripping the input format from right side of the string: ', s.rstrip('.,grt'))

# Some String Testing
s = 'Hello World'
print(
    s.isalnum(), #check if all char are alphanumeric 
    s.isalpha(), #check if all char in the string are alphabetic
    s.isdigit(), #test if string contains digits
    s.istitle(), #test if string contains title words
    s.isupper(), #test if string contains upper case
    s.islower(), #test if string contains lower case
    s.isspace() #test if string contains spaces
)