# METHOD	            DESCRIPTION
# capitalize()      	Converts the first character to upper case
# casefold()        	Converts string into lower case
# center()          	A centered string
# count()           	the number of times a specified value occurs in a string
# encode()          	an encoded version of the string
# endswith()        	true if the string ends with the specified value
# expandtabs()      	Sets the tab size of the string
# find()            	Returns the position of where value was found
# format()          	Formats specified values in a string
# format_map()      	Formats specified values in a string
# index()           	Returns the position of where value was found
# isalnum()         	True if all characters in the string are alphanumeric
# isalpha()         	True if all characters in the string are in the alphabet
# isdecimal()       	True if all characters in the string are decimals
# isdigit()         	True if all characters in the string are digits
# isidentifier()    	True if the string is an identifier
# islower()         	True if all characters in the string are lower case
# isnumeric()       	True if all characters in the string are numeric
# isprintable()     	True if all characters in the string are printable
# isspace()         	True if all characters in the string are whitespaces
# istitle()         	True if the string follows the rules of a title
# isupper()         	True if all characters in the string are upper case
# join()            	Joins the elements of an iterable to the end of the string
# ljust()           	a left justified version of the string
# lower()           	Converts a string into lower case
# lstrip()          	a left trim version of the string
# maketrans()       	a translation table to be used in translations
# partition()       	a tuple where the string is parted into three parts
# replace()         	a string where a specified value is replaced
# rfind()           	Returns the position of where value was found
# rindex()          	Returns the position of where value was found
# rjust()           	a right justified version of the string
# rpartition()      	a tuple where the string is parted into three parts
# rsplit()          	Splits the string (separator), and returns a list
# rstrip()          	a right trim version of the string
# split()           	Splits the string (separator), and returns a list
# splitlines()      	Splits the string at line breaks and returns a list
# startswith()      	true if the string starts with the specified value
# strip()           	a trimmed version of the string
# swapcase()        	Swaps cases
# title()           	Converts the first character of each word to upper case
# translate()       	a translated string
# upper()           	Converts a string into upper case
# zfill()           	Fills the string with 0 values at the beginning




# name = "sagaaar"
# print(len(name))
# print(name.translate(7))


# mydict = {83:  80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))


# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "t")
# print(txt.translate(mytable))

# # print(txt.maketrans("o","s"))

# a= "Mr. Sagar"
# b=a.swapcase()
# print(b)
# mR. sAGAR

# name = "my name is alana"
# a=name.startswith("my")
# print(a)


# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)
# ['Thank you for the music', 'Welcome to the jungle']

# txt = "I could eat bananas all day, bananas are my favorite fruit"

# x = txt.rpartition("all")

# print(x)
# ('I could eat bananas ', 'all', ' day, bananas are my favorite fruit')


# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

    
# print(x) 

# string_a = "Hello"
# string_b = "Cena"

# # Index based:
# print("{0}, John {1}"
#       .format(string_a, string_b))
# # Object based:
# print("{greeting}, John {last_name}"
#       .format(greeting=string_a, last_name=string_b))


string =  "Add Grepper Answer"
print(string.count(''))
