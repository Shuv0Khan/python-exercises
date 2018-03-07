# declared using "def"
# python uses "snake_case" for naming. pun intended.

def sum(x=0,y=0):
    print("{}+{}={}".format(x,y,x+y));

# now call it
sum(); # will use default value
sum(1,3);

# function doc?
def sub(x=0,y=0):
    """
    SUBTRACTS TWO NUMBERS.
    BY DEFAULT RESULT IS 0.
    """
    print("{}-{}={}".format(x,y,x-y));

sub(1,2);

# want to return?
def mult(x=0,y=0):
    return "{}*{}={}".format(x,y,x*y);
print(mult(2,3));

# MAGIC. guess what this will do
sum("2","3");
# how to do it porperly? type()!
def int_sum(x=0,y=0):
    if type(x)==type(y)==type(0):
        return x+y;
    else:
        return 0;
print(int_sum(2,3));
print(int_sum("2","3"));

# Lamda expression. and Filter
# suppose need to find all the numbers that aren't 0 from a list like bellow
seq = [0,1,1,2,0,4,3,0];
out = [];
for element in seq:
    if element!=0:
        out.append(element);
print(out);

#let's use function
def check_number(x):
    return x!=0;
out = [];
for element in seq:
    if check_number(element):
        out.append(element);
print(out);

# but it's more work. use Filter, a generator
out = filter(check_number,seq);
print(list(out));

# don't want to use that silly little function? use Lambda
out = filter(lambda x:x!=0,seq); # much like (x!=0)?x:False
print(list(out));
