# for loop

#same for tuples,sets,lists
print("Tuple");
seq = (1,2,"String");
for element in seq:
    print(element);

print("List");
seq = [1,2,3];
for element in seq:
    print(element);

print("Set");
seq = set();
seq.add(1);
seq.add(1);
seq.add(2);
seq.add(2);
for element in seq:
    print(element);

# dictionries are little different
print("dictionary");
my_dictionary = {
    "key1":"value1",
    "key2":"value2"
};
# will print only keys.
for element in my_dictionary:
    print(element);

# the real way
for element in my_dictionary:
    print(my_dictionary[element]);

# intermidiate level stuff for tuples. TUPPLE UNPACKING
seq = [(1,2),(3,4),(5,6)];
for elem1,elem2 in seq: # or with Bracket -- for (elem1,elem2) in seq:
    print("Tuple : {x} , {y} ".format(x=elem1,y=elem2));





#===============================================================================
# while loop
i = 1;
while i<3:
    print("i is : {}".format(i));
    # integers in python are immutable. so no ++/-- increment is made available.
    # want to increment? well then reassign.
    i+=1;






#===============================================================================
# now a bit of "intermidiate stuff"
# hey there are other ways which can do the job of ++/--
# enumerate()
# itertools.count()
#range

seq = ["a","b","c"];
# for(i=0;i<seq.length;i++)
for index,element in enumerate(seq):
    print("element at {} is : {}".format(index,element));
# want to start counting from any other number than 0?
# for(i=5;i<seq.length+5;++)
for index,element in enumerate(seq,5):
    print("element at {} is : {}".format(index,element));



from itertools import count;
print("count from 0");
# for(i=0;;i++)
for i in count(): # this way creates a infinite counter. so needs to break
    if i>3:
        break;
    print("i is : {}".format(i));


print("count from 1 with step 2. basically i+=2");
# for(i=1;;i+=2)
for i in count(1,2): # step size can also be declared
    if i>10:
        break;
    print("i is : {}".format(i));


# against using break to end looping?
print("Without break");
from itertools import islice;
#loops 5 times, with step 2
# this is not for(i=1;i<5;i+=2).
# it's for(i=1,j=0;j<5;i+=2,j++).

for i in islice(count(1,2),5):
    print("i is : {}".format(i));

# range function
print("Range to loop. 0 to 2. 3 times.")
# for(i=0;i<3;i++)
for i in range(3):
    print("i is : {}".format(i));
print("Range to loop. 1 to 5 with step size 2.");
# for(i=1;i<6;i+=2)
for i in range(1,6,2):
    print("i is : {}".format(i));
