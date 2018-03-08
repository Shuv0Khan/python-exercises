class temp():
    pass

x = temp();
print(type(x));
# <class '__main__.car'>

class Car():
    # class object attributes. always same for all objects
    no_0f_wheels = 4;

    def __init__(self,name,model,color):
        self.name = name;
        self.model = model;
        self.color = color;

mycar = Car("toyota","2015","white");
print(mycar.name);
print(mycar.model);
print(mycar.color);

hiscar = Car(color="Red",name="BMW",model="2010");
print(hiscar.name);
print(hiscar.model);
print(hiscar.color);

print(mycar.no_0f_wheels);
print(hiscar.no_0f_wheels);

class SmartPhone():
    os = "Android";
    def __init__(self,os="Android",imei="",price=""):
        self.os = os;
        self.imei = imei;
        self.price = price;

    def update(self,os):
        self.os = os;

galaxy_s8_plus = SmartPhone("Android 7.1.1","123rojefio2j","800");
print(galaxy_s8_plus);

print("os:",galaxy_s8_plus.os);
print("imei:",galaxy_s8_plus.imei);
print("price:",galaxy_s8_plus.price);

galaxy_s8_plus.update("Andoid 7.1.2");
print("os:",galaxy_s8_plus.os)
