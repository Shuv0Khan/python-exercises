# Strings

# Basics
print("*** Basics ***");

print('hello');
print("hello");
print("I'm Shuvo");

# Indexing
print("*** Indexing ***");

my_string = "abcdefg";
print(my_string[0]);
print(my_string[-1]);
print(my_string[3]);

# Slicing
print("*** Slicing ***");

print(my_string[2:]);#from index 2(included) prints the rest - cdefg
print(my_string[:3]);#from index 0 upto 3(excluded) - abc
print(my_string[2:5]);#from index 2(included) upto 5(excluded) - cde
print(my_string[::]);#full string
print(my_string[:]);#full string
print(my_string[::1]);#start at begining till end with step 1 - abcdefg
print(my_string[::2]);#start at begining till end with step 2 - aceg


# Basic Methods
print("*** Basic Methods ***");

print(my_string.upper());
print(my_string.lower());
print(my_string.capitalize());
print(my_string.split("e"));
print("my string".split());#by default splits on whitespace
print(len(my_string));#length of string

# String to list and vice-versa
print("*** String to List and vice-versa ***");

l = list(my_string);
l.reverse();
my_string = "".join(l);

# Print formatting
print("*** Print formatting ***");

my_string = "My Name is {}";
my_string = my_string.format("Shuvo");
print(my_string); # My Name is Shuvo

my_string = "Name : {}, Designation : {}";
my_string = my_string.format("Shuvo","Software Eng.");
print(my_string); # Name : Shuvo, Designation : Software Eng.

my_string = "Name : {y}, Designation : {x}";
my_string = my_string.format(x="Shuvo",y="Software Eng.");
print(my_string); # Name : Software Eng., Designation : Shuvo

my_string = "Name : {x}, Designation : {x}";
my_string = my_string.format(x="Shuvo",y="Software Eng.");
print(my_string); # Name : Shuvo, Designation : Shuvo
