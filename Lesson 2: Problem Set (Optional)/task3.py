#!/usr/bin/python

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def higher(a,b):
    if a > b: return a
    else: return b

def highest(a,b,c):
    return higher(a,higher(b,c))
    
def lower(a,b):
    if a > b: return b
    else: return a

def lowest(a,b,c):
    return lower(a,lower(b,c))
    
def set_range(a,b,c):
    l = lowest(a,b,c)
    h = highest(a,b,c)
    return h - l
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6

