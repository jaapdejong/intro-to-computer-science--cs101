#!/usr/bin/python

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l):
	if len(l) == 0: return None
	prev = l[0]
	currlen = 1
	maxlen = 1
	best = l[0]
	for i in range(1, len(l)):
		#print l[i], currlen
		if l[i] == prev: 
			currlen += 1
			if currlen > maxlen:
				maxlen = currlen
				best = prev
		else:
			currlen = 1
			prev = l[i]
	return best	



#For example,

#print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

#print longest_repetition([1,2,3,4,5])
# 1

#print longest_repetition([])
# None

print longest_repetition([2, 2, 3, 3, 3])

