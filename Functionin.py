#  Function is use for code reusability 
 ###### SYNTAX of funtion #########
# def Function_name (parameter):  #function initialize
#     |
#     |funnction_body           #function declaration
#     |
#     |return Value 

# Function_name(argument) #function calling

# def Add(x,y):
#     print(x+y)
# print(Add(10,5))
# Add(5,8)

# def Add(x,y):
#     return(x+y)
# print(Add(10,5))
# Add(5,8)

# def Add(x,y):
#     print(x+y)
# z=Add(10,5)
# print(z)
# print("Hello")
# print(z)

        #### Print Evene Number using function #####

# def Even(n):
#     for i in range(1,n+1):
#         if(i%2==0):
#             print(i)
# n=int(input("Enter the number :"))
# Even(n)

       ########## Leap year questions ###########

# def Leapyear(n):
#       if((n%4==0 or n%400==0) and n%100!=0):
#           # if(n%100!=0):
#           print("It is leap year")
#       else:
#           print("not")
      
# n=int(input("Enter the year :"))
# Leapyear(n)

  ####### Relation B/T Parameters & Arguments--->

# positional Arguments
# Keyword Arguments
# Default Arguments
# positional length / variables length argument
# Keyword length /Keyword variables length argument

########## Positional Arguments #######
# def Add(x,y):
#     print(x,y)
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add(a,b)
# print(z)

#febbonachi code --->
# def my_fibo(n):
#     a=0
#     b=1
#     for i in range(1,n+1):
#         c=a+b
#         if i<n:
#             print(c,end=',')
#         else:
#             print(c)
#         a,b=b,c
# x=10
# my_fibo(x)

  ######## Key word arguments #####
  
# def Add(x,y):
#     print(x,y)
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add(x=a,y=b)
# print(z)

 ######## Default Arguments #########


# def fibo(x=0,y=0,z=0):
#     print(x,y,z)
# p=10
# q=20
# r=30
# fibo()
# fibo(p)
# fibo(p,q)
# fibo(p,q,r)


# def Add(x=0,y=0):
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add()
# print(z)

  ######### Variable length Positional Arguments ######
#as pr documentation args hota hai perameter,,,
# * sari value ko accept karta hai ,,,,
# def add(*n):
#   print(n)
#   print(type(n))

# add(2,4,5,6,7,8,9,2,1,3,5,6,4 )
# add(10)


# def add(*n):
#   sum=0
#   for i in n:
#     sum=sum+i
#   return sum
# x=add(2,4,5,6,7,8,9,2,1,3,5,6,4 )
# print(x)

  ####### Assign multiple values in arguments ######
# def add(*n):   # *args
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#     return sum
# n=eval(input("Enter all values"))
# z=add(n)
# print(z) 


  ######### Key word variables length arguments ########
####  ** ye dictonery ke format me data save karta hai ,,,,, kwargs 
# def show(**n):    # **kwargs
#     print(n)
#     print(type(n))
    # for i,j in n.items():  #keys values dono ke liye 
    # for i in n.values(): # only value ke liye
    # for i in n.keys():   # only keys  ke liye       
        #  print(i,j)

# show(name="Dharmendra",age=20)


#### function ke argunment me agr dusra function pass karna hai to is cenerio ko ham higer order function kahte hai ,,,
### example --->>>
#ye sabhi higer order function hote hai --->>
#map()
#filter()
#reduce()
#decorator()
#generator()
#lamda()


#pthon tutor google platform 

####### Decorator :------>>>>>
#decorator ak spatial higer order function hai jo kisi v function ka internal behaviour change karta hai ,, 
#mtlb ye kisi bhi function ke andr ke code ko bina change kiye huye uska behaviour badal dena decorator kahlata hain  

#decorator ak spatial higer order function hai jo ki ak function return karta hai or as a argunment bhi wo function pass karta hai 
#      or as a perameter wo function hi accept karta hai ,,,,

# python me decorator ko ham @ se represent karte hai,,,

####  SYNTEX---->>>>
              
              #def outer_fun(fun_name):
                    #def inner.fun():
                          #fun_name()
                    #return inner.fun       #   function name return karna hai
                 
              #x=outer_fun(fun_name)
              #x()


# def outer_fun(a):
#     def inner_fun(x):
#         x=x+5           #(modification)
#         return x
#     return inner_fun
# def add(a,b):
#     return a+b
# x=outer_fun(add)           ## function pass ,,
# print(x)
# z=x(4,5)
# print(z)
