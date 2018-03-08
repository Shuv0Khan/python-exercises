"""
LEGB
 L: Local
 E: Enclosing function locals
 G: Global
 B: Built-in
"""


"""
Local scope :
"""
# Global variable x
x = 14;

def my_func():
    # Local variable x
    x = 23;
    return x;

# print(x);
# print(my_func());

# output - 14 23

# my_func();
# print(x);

# output - 14

"""
Enclosing function locals
"""
# Global name
name = "This is global";
# Local x in lambda function
print(filter(lambda x:x**2,[2,3,4]));

# enclosing function locals

def greet():
    name = "Shuvo";
    def hello():
        print("Hello",name); # another way to print. puts whitespace automatically
    hello();

print(name);
greet();
print(name);

# This is global
# Hello Shuvo
# This is global

"""
Built-in
"""
len([]);



"""
Global variable changed inside local scope
always avoid using "global" keyword (until compelled to)
"""
print(x);
def redefine():
    global x;
    x = 1000;
print(" before function call x:",x);
redefine();
print(" after function call x:",x);
