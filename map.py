#map function ()--->>
#jha par input or output elements barabar hai wha map use hoga 

#syntex-->
#map (fun_name,collection)
#                  |__list,tupple,string,,
#map collection ki ak ak value utha kr uspr opeeration perform karta hai ,,,


#Question:- list me 5 add karna hai-->
# l=[1,2,3,4,5]
# def add5(n):
#     return n+5
# x=map(add5,l)
# print(x)
# print(tuple(x))

#Question:- dono list ke elements ko add karke ak new list show karni hai-->
# l=[1,2,3,4,5]
# l1=[6,7,8,9,1]
# def add5(n,m):
#     return n+m
# x=map(add5,l,l1)
# print(x)
# print(tuple(x))


# import functools
# l=[1,2,3,4,5]
# def Squar(n):
#     return (n**2)
# x=map(Squar,l)
# print(x)
# print(tuple(x))

#   ########## Multiply two collection using map function ######
# l1=[1,2,3,4,5]
# t1=(1,2,3,4,5)
# def Squr(m,n):
#     return (m*n) 
# x=map(Squr,l1,t1)
# print(list(x))

#  ##########################

# l=[1,2,3,4,5]
# def Even(n):
#     if(n%2==0):
#         return n

# x=filter(Even,l)
# print(tuple(x))

#  ############### reduce function ##############
#  #jaha pr output 1 element aa rha hai wha reduce lagega 
# l=[10,20,30,5,25,12,6]
# def Maxfun(x,y):
#       if(x>y):
#         return x
#       else :
#        return y
# x= functools.reduce(Maxfun,l)
# print(x)



#### filter function---->
#syntex--->
#filter (fun_name,collectin)

# l=[1,2,3,4,5,6,7,8,9,10]

# def even_no(n):
#     if n%2==0:
#         return n
# x=filter (even_no,l)
# print(x)
# print(list(x))
 

# 5 se bade number nikalne hai -->>>>
# l=[1,2,3,4,5,6,7,8,9,10]

# def graters(n):
#     if n>=5:
#         return n
# x=filter (graters,l)
# print(x)
# print(list(x))