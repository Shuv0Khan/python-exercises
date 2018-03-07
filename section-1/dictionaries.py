# dictionary == hashtable/ objects in javascript(no Methods)
# key - value pairs
# no order

profile = {
    "name":"shuvo",
    "age":26,
    "Designation":"S.E.",
    "result":[2,3,4,5],
    "Contacts":{
        "home":88018,
        "office":88017,
        "tel":[4038,50268]
    }
};
print(profile);
print(profile["result"][3]);
print(profile["Contacts"]["tel"][1]);

profile["age"] = 27;
print(profile);

profile["Company"] = "REVE Systems";
print(profile);
