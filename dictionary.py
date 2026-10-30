emp = {"name":"rahul", "age":35, "sal":50000, "dept":"IT"}

print("the dictionary is: ",emp)

#accessing
print("name: ",emp["name"])
print("age: ",emp["age"])
print("salary: ",emp["sal"])
print("department: ",emp["dept"])

#add, update, delete
emp["ph no"] = 9988776655
print("after adding : ",emp)

emp["sal"] = 60000
print("after updating : ",emp)

del emp["dept"]
print("after deleting : ",emp)

#methods
print("keys: ")
print(emp.keys())

print("values: ")
print(emp.values())

print("items: ")
print(emp.items())

print("name: ",emp.get("name"))
print("dept: ",emp.get("dept","not available"))

emp.update({"age":36,"ph no":8567849043})
print("after update")
print(emp)

#frequency

text = input("enter the string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch]+1
    else:
        frequency[ch] = 1

print("character frequency")
for ch, count in frequency.items():
    print(ch,":",count)


