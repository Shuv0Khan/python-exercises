# lists == Arrays
# similar to javascript Arrays

#creating list
my_list = [1,2,3];
print(my_list);
print(len(my_list));

my_list = [1,2.2,"shuvo",[1,2,3]];
print(my_list);
print(len(my_list));

#list Indexing and Slicing
print(my_list[0]);
print(my_list[-1]);
print(my_list[2:]);
print(my_list[:3]);
my_list[0] = 4;
print(my_list);

#basic methods
my_list.append([4,5,6]);
print(my_list);
my_list[4].extend([7,8,9]);
print(my_list);
last_item = my_list.pop();
print(my_list);
print(last_item);
second_item_of_nested_list = my_list[3].pop(1);
print(my_list);
print(second_item_of_nested_list);
my_list.reverse();
print(my_list);
my_list = [4,1,3,2];
my_list.sort();
print(my_list);

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
