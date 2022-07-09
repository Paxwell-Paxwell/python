person = ["Bangkok", "Aungkoon", "Kongpet", "Male", 28]
person_dict = {"firstname":"Aungkoon", "address":"Bangkok", "lastname":"Kongpet", "gender":"Male", "age":"28"}
print(person_dict)

person_dict["firstname"] = "David" # edit data by key
print(person_dict["firstname"]) # get data by key
person_dict.pop("lastname") # remove data by key
print(person_dict)

print("///////////////////////////")

person_dict["tel"] = "1234567890" # add data to dict
print(person_dict)

"""for key in person_dict:
    print(person_dict[key])"""

for key , v in person_dict.items():
    print(v)

print("///////////////////////////")

person_dict = sorted(person_dict.items(), key=lambda x: x[1])
print(person_dict)
