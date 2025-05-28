  ########## Factor of any number ##########
# n=int(input("Enter the number "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=' ')

  ########## Character to ASCCI value #############
# s=input("Enter any String : ")
# for i in s:
#     # print(i)
#     # print(ord(i)+5)
#     # print(i,ord(i))

#     ####### ASCCI to Character #########
    
#     print(chr(ord(i)+5),end='')
 
 ######### Eval Take input in any data type
 
  ########## List Operation by eval ##########
# x= eval(input("Enter the data "))
# # print(type(x))
# l=[]
# for i in x:
#    l.append((i**2)+5)
# print(l)

   ########### Tuple operation by type casting ##########

# x=eval(input("Enter any tuple :"))
# x=list(x)
# l=[]
# for i in x:
#   l.append(i**0.5)
# print(tuple(l))

  ################# Dictionaries operation ##############
# a=eval(input("Enter any Dictionary :"))
# for i,j in a.items():
#   print(i,j)

     ############ Find minimium value in list ##################
# l=[10,20,4,3,24,16]
# minval=l[0]
# for i in l:
#   if i<minval:
#     minval=i
# print(minval)

     ############ Find maximium value in list ##################

# l=[10,20,4,3,24,16]
# maxval=l[0]
# for i in l:
#   if i>maxval:
#     maxval=i
# print(maxval)

#  to ask the user to inter name of there 3 favorate movies & store then a list....

# movie1=input("enter a first movie")
# movie2=input("enter a second movie")
# movie3=input("enter a third movie")

# list=[movie1,movie2,movie3]
# print(list) #ham append ka use kar sakte the 


#  to cheq if a list contains a pallindrom of elements ,

# list=[1,2,4,5,2,1]
# list1=list.copy()
# list1.reverse()

# if list==list1:
#     print("pallindrom")
# else:
#     print("not a pallindrom")


