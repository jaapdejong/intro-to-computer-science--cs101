#!/usr/bin/python

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    result = chr(ord(letter)+1)
    if result > 'z': return 'a'
    return result


print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a

