# tuples == immutable sequences like enum
# sets == unordered collection of unique items
# booleans == booleans

print(True and False);
print(not False and True);

my_tuple = (1,2,3,"Shuvo");
print("my_tuple[3] : {}".format(my_tuple[3]));
# tupples are accessed like list with [] braces
# they are created using () like a function
print("\n");

myset = set();
myset.add(1);
myset.add(2);
myset.add(4);
myset.add(2.4);
print("myset : {}".format(myset));

myset.add(2);
print("adding 2 to myset : {}".format(myset));

mylist = [1,3,4,5,5,5,6,7,3];
print("creating set from list {} : {}".format(mylist,set(mylist)));
