# lists == Arrays
# similar to javascript Arrays

#creating list
my_list = [1,2,3];
print(my_list);
print(len(my_list));
print("\n");

my_list = [1,2.2,"shuvo",[1,2,3]];
print("my_list : ");
print(my_list);
print("my_list length : {}".format(len(my_list)));
print("\n");

#list Indexing and Slicing
print("my_list[0] : {}".format(my_list[0]));
print("my_list[-1] : {}".format(my_list[-1]));
print("my_list[2:] : {}".format(my_list[2:]));
print("my_list[:3] : {}".format(my_list[:3]));
my_list[0] = 4;
print("my_list[0] = 4 : {}".format(my_list));
print("\n");

#basic methods
my_list.append([4,5,6]);
print("append([4,5,6]) : {}".format(my_list));

my_list[4].extend([7,8,9]);
print("extend([7,8,9]) : {}".format(my_list));

last_item = my_list.pop();
print("list.pop() : {}".format(my_list));
print("popped item : {}".format(last_item));

second_item_of_nested_list = my_list[3].pop(1);
print("pop from nested list : {}".format(my_list));
print("popped item : {}".format(second_item_of_nested_list));

my_list.reverse();
print("list.reverse() : {}".format(my_list));

my_list = [4,1,3,2];
print("my_list before sort : {}".format(my_list));
my_list.sort();
print("my_list after sort : {}".format(my_list));
print("\n");

#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]];
first_col = [row[0] for row in matrix];
print(first_col);

# dazzling? what's happening here?
#break down with another example:
seq = [1,2,3,4];
out = [];
for element in seq:
    out.append(element**2);
print(out);

# same can be done without appending to "out"
# take element**2 and place it before for.
# element**2 for element in seq
# enclose whole thing in [] and assign to out
out = [element**2 for element in seq];
print(out);

"""
Built-in functions of list
"""
print("built-ins");
print(seq);
print("poped :",seq.pop());
print(seq);
print("appended 5");
seq.append(5);
print(seq);
print("cleared list");

# beaware of del
del seq[:]
print(seq);

a = [1,2,3];
b = a;
a = [];
# a will be empty
print(a);
# b will remain unchanged
print(b);

# but
a = [1,2,3];
b = a;
# inplace deleting
del a[:]
# a will be empty
print(a);
# b will also be empty
print(b);
