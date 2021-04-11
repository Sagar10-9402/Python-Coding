
#functions practice

#1) char input last word print 
#2 odd even
#3 addition
#4 true false
#5 large no
#6 pelidrome sequaance 


def last_char(name):
	return name[-1]
	
print(last_char("sagar"))

def odd_even(num):
	if num%2==0:
		return "even"
	return "odd"	

print(odd_even(7))	

def is_even(num):
	if num%2==0:
		return True
	return False
print(is_even(2))	

def add_two(a,b):
	return a+b
print(add_two(2,3))	

#large no

def large_no(a,b):
	if a>b:
		return a
	else:
		return b

print(large_no(2,15))	

#pelindrome 


def is_pelindrome(name):
	name = input('enter a name ')
	reverce_word=name[::-1]
	if name==reverce_word:
		return True
	return False 	

print(is_pelindrome(""))

