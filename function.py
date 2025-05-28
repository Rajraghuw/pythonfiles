
# # function squrute methoud

# def sqrt(n):
#    # print(n**0.5)
#    return n**0.5
# n=int(input("enter a num"))
# z=sqrt(n)
# print(z)
# #sqrt(n)

#creat leep year program                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

# def cheqleapyear(year):
    
# n=int(input("enter any year"))
# cheqleapyear(n)

#relation blow perameters & argument -->
#1 position argument--> (normal perameters me value pass karte hai )
# def add(x,y):
#     return x+y
# p=5
# q=9
# z=add(p,q)
# print(z)


#2 keyword argunment--> (isme ham as a variable & key value asign krte hai)
# def add(x,y):
#     print("value of x:",x)
#     print("value of y:",y)
#     return x+y
# p=5
# q=9
# z=add(y=p,x=q)
# print(z)

#3 default argument--> (default ka mtlb hai perameters ki value pehle se set karke rkhi hai hamne)
# def add(x=0,y=0):
#     print("value of x:",x)
#     print("value of y:",y)
#     return x+y
# p=5
# q=9
# z1=add()
# print(z1)

# z2=add(p)
# print(z2)

# z3=add(x=q,y=p)
# print(z3)

# z4=add(p,q)
# print(z4)


#4 variable-lenght argunment-->()
# * star ka mtlb hota h all

# def add(*n):
#     print (n)
#     sum=0
#     for i in n:
#         for i in i:
#             sum=sum+i

#     return sum
# n=eval(input("enter a vlaue"))
# z=add(n)
# print (z)


# 5 keyword variable lenght argunment-->
#  *args,**kwangs
# def showdetails(**n):
#     print(n)
#     print(type(n))
#     for i,j in n.items():
#         print(f'my{i}is{j}')

# showdetails(name="raja",age=22)
