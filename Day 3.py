Strings are bits of text. We can define that using single or double quotes.

We can do many operations on string as described below.

my_string = "Hello InterviewBit"
print(len(my_string)) #prints 18
Finds length of string using built-in len() method.

my_string = "Hello InterviewBit"
print(my_string.index("l"))
# prints 2
Finds the first index of character ‘l’. Notice how there are actually two l’s in the phrase - this method only recognizes the first.

my_string = "Hello InterviewBit"
print(my_string.count("e"))
This counts the number of e’s in the string. Therefore, it should print 3.

my_string = "Hello InterviewBit"
print(my_string[2:7])
# prints "llo I"
This prints a slice of the string, starting at index 2, and ending at index 6.

my_string = "Hello InterviewBit"
print(my_string[2:7:2])
# prints "loI"
This prints the characters of string from 2 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].

my_string = "Hello InterviewBit"
print(my_string.upper())
print(my_string.lower())
These make a new string with all letters converted to uppercase and lowercase, respectively.
