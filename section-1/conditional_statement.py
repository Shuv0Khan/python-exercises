# Both of the bellow works
if 1<2: # Without First Bracket
    print("First Block");
if (2<3): #With First Bracket
    print("Second Block");

#Indentation
# ; doesn't matter actually. it's all about Indentation
if(1<2):
    print("First Block");
    if(20<3):
        print("Second Block");
    #if(20<3):
        #Must have at least one indented line?
    #print("Third Block");

# if-elseif-else
num = 0;
if(1<num):
    print("if");
elif(2<num):
    print("elseif");
else:
    print("else");
