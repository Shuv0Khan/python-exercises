# tuples == immutable sequences like enum
# sets == unordered collection of unique items
# booleans == booleans

print(True and False);
print(not False and True);

my_tuple = (1,2,3,"Shuvo");
print(my_tuple[3]);

myset = set();
myset.add(1);
myset.add(2);
myset.add(4);
myset.add(2.4);
print(myset);

myset.add(2);
print(myset);

mylist = [1,3,4,5,5,5,6,7,3];
print(set(mylist));
