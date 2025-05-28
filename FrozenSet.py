#collection of unorderd unic elements.
#represented through frozenset () with comma sepreted elements.
#indexing not suppurted.
#slicing not supported.
#inmutable in nature.

#example--->
#list ko frozenset me change karna --->>


l=[1,2,3,4,5]
x=frozenset(l)
print(x)
print(type(x))
print(len(x))
print(sum(x))
print(min(x))
print(max(x))

#isme ham structure change karne wali methoud use nhi kar sakte kyoki ye inmutable hai 

#jo applicable hongi wo methoud hai jo structure change nhi karti --->
# union()
# intersection()
# diffence()


l=[1,2,3,4,5]
l2=[20,45,32,55,85]
fs1=frozenset(l)
fs2=frozenset(l2)
print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issuperset(fs2))
print(fs1.issubset(fs2))

#note--->>> deta types ko empty represent karne ke liye ham ye karte hai 
#int()--->
#str()--->'' ,"",
#list()---->[]