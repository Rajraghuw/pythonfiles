#Ddictionary are used to store data values in key:value pairs,
#They are unorded,mutable(changeble) & don't allow duplicate keys,

# info = {
#     "name":"raja raghuwanshi",
#     "Age" : 22,
#     "subject":["python","c++","java"],
# }
# print(info["name"])
# print(info["Age"])        # key value access
# print(info["subject"])


# info["name"] = "raj"             #value change 
# info["surname"] = "raghu"        #key value pair add
# print(info["name"])
# print(info["surname"])


#nested dictonary creat,,,,

student = {
    "name":"raja",
    "Age" : 22,
    "subject" : {
          "phy":45,
          "che":65,
          "maths":58,
    }
}
print(student["subject"]["che"])


#Dictionary Methods---->>>
#myDict.keys()  return all keys
#myDict.values()  return all values
#myDict.items()  return all (keys,val) pairs as tupple
#myDict.get("key")  return the key according to value
#myDict.update(newDict)  insert the specified items to the dictionary



# info = {
#     "name":"raja raghuwanshi",
#     "Age" : 22,
#     "subject":["python","c++","java"],
# }
# print(info.keys(5))



