# excercise 1
def array_check(all_nums):
    for index in range(0,len(all_nums)-2):
        if(all_nums[index]==1 and all_nums[index+1]==2 and all_nums[index+2]==3):
            return True;
    return False;
print(array_check([1,1,1,2,3,4]));
print(array_check([1,1,1,2,1,3,4]));



# excercise 2
def string_bits(str):
    return str[::2];

print(string_bits("Hello"));



# excercise 3
def end_other(a,b):
    a = a.lower();
    b = b.lower();
    # return a.endswith(b) or b.endswith(a);
    # return a[-len(b):]==b or b[-len(a):]==a;
    # with Slicing, Indexing out of range give full string_bits
    # a="HELLO"
    # a[-10:] ----> 'HELLO'
    # a[:10] ----> 'HELLO'
    if(len(a)>=len(b)):
        start_index = len(a)-len(b);
        if(a[start_index:] == b):
            return True;
    else:
        start_index = len(b)-len(a);
        if(b[start_index:] == a):
            return True;
    return False;

print(end_other("Hiabc","Abc"));
print(end_other("Abc","AbcHi"));
print(end_other("Hia","Abchia"));


# excercise 4
def double_char(str=""):
    return_str = "";
    for char in str:
        return_str=return_str+char+char;
        # return_str+= char*2;
    return return_str;

print(double_char("HELLO"));


# excercise 5
def no_teen_sum(x,y,z):
    x = fix_teen(x);
    y = fix_teen(y);
    z = fix_teen(z);
    return x+y+z;
def fix_teen(x):
    # if x in [13,14,17,18,19]:
    #     return x;
    # return 0;
    if(x>12 and x<20):
        if(x == 15 or x == 16):
            return x;
        else:
            return 0;
    return x;

print(no_teen_sum(0,0,0));
print(no_teen_sum(0,1,2));
print(no_teen_sum(15,16,15));
print(no_teen_sum(13,18,17));
print(no_teen_sum(1,2,18));



# excercise 6
def count_evens(nums):
    out = filter(lambda x:x%2==0,nums);
    return len(list(out));

print(count_evens([1,1,2,5,4,6,3]))



# excercise 7
def take_input():
    temp = input("Give something : ");
    print("you typed : {} of type {}".format(temp,type(temp)));
    temp = list(input("This will be converted to list : "));
    print(temp);

take_input();



# excercise 8
import random;
def random_seq_generator():
    my_list = [str(number) for number in range(10)];
    random.shuffle(my_list);
    print("my list after shuffle : {}".format(my_list));
    print(my_list[:3]);

random_seq_generator();
