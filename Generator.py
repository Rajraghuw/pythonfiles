#generator-->
#creat a collection in form of generator object
#it helds a collection of elements
#it use yield insted of return keyword

#syntex: def fun_name(perameters):
 #              yield value

# x=fun_name(argument)
#next(x)

#Examples:-->

# def even(n):
#     for i in range(1,n+1):
#         yield 2*i
# x=int(input("enter num"))
# y=even(x)
# print(y)
# print(list(y))
# for i in y:
#     print(i)
# print(next(y))
# print("hellow")
# print("hi")
# print(next(y))

#--------------->>>>>>>> 
 
# def even(n):
#      for i in range(1,n+1):
#          yield i
# x=int(input("enter num"))
# y=even(x)
# print(next(y))
# print("hellow")
# print("hi")
# print(next(y))

#------------->>>>>>>>>

# def table(n):
#      for i in range(1,n+1):
#          yield i
# x=int(input("enter num"))
# y=table(x)
# print(len(list(x)))
# z=next(y)
# for i in range(1,11):
#      print(z*i)

# z=next(y)
# for i in range(1,11):
#      print(z*i)

# z=next(y)
# for i in range(1,11):
#      print(z*i)

