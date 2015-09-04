#!/usr/bin/python

# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def isLetter(ch):
    if ch >= 'a' and ch <= 'z': return True
    if ch >= 'A' and ch <= 'Z': return True
    if ch == '!': return True
    if ch == '.': return True
    if ch == ',': return True
    return False

def findWord(s):
    i = 0
    start = 0
    end = 0
    while i < len(s):
        if s[i] == '<':
            while i < len(s) and s[i] != '>': i += 1
        elif not isLetter(s[i]): i += 1
        else: 
            start = i
            while i < len(s) and isLetter(s[i]): i += 1
            end = i
            return start, end
    return start, end
                
            
        
def remove_tags(s):
    result = []
    while True:
        start, end = findWord(s)
        if start == end: return result
        result.append(s[start:end])
        s = s[end:]
        

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags("<br />This line starts with a tag")

