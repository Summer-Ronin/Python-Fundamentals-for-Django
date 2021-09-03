#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:

# Solution
# 'd'
print(s[:1])
# 'o'
print(s[-1:])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[-2:])

# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"

#Solution
l[2][2] = 'goodbye'
print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# Solution
d4 = {'hello1': d1['simple_key'], 'hello2': d2['k1']['k2'], 'hello3': d3['k1'][0]['nest_key'][1][0]}

print(d4)

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

# Solution
new_set = set(mylist)

print(new_set)


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {name} and he is {age} years old".format(name=name, age=age))
