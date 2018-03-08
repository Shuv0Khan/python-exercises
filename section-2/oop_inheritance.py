"""
Inheritance
"""

class Animal():
    def __init__(self):
        print("Animal created");

    def who_am_i(self):
        print("Animal");

    def eat(self):
        print("Eating");

animal = Animal();
animal.who_am_i();
animal.eat();

class Dog(Animal):

    def __init__(self):
        # optionally call init of parent
        # Animal.__init__(self);
        print("Dog created");

    def bark(self):
        print("Woof");

    def eat(self):
        print("Dog Eating");

dog = Dog();
dog.who_am_i();
dog.eat();


"""
Special methods
"""

class Book():
    def __init__(self,title,author,pages):
        self.title = title;
        self.author = author;
        self.pages = pages;

    def __str__(self):
        return "Title : {} , Author : {} , Pages : {}".format(self.title,self.author,self.pages);

    def __len__(self):
        return self.pages;

    def __del__(self):
        print("Book deleted");

b = Book("Douluo Dalu","Tang san",300);
print(b);
print(len(b));
del b;
