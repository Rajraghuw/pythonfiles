#ord function cherecter ko asky value me convert karta hai----->>>  

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

######### Swaap first and last string value------------>>>>>>>>>>>
s='python'
l=list(s)
l[0],l[-1]=l[-1],l[0]
print(l)
s=''.join(l)
print(s)

########### Swaap first and last integer value------------>>>>>>>>>>>

# n=12345
# s=str(n)
# l=list(s)
# l[0],l[-1]=l[-1],l[0]
# print(l)
# s=''.join(l)
# n=int(s)0
# print(n)


######### Move all zeros al the last posigition---------->>>>>>>>>>>
# l=[2,0,1,0,3,0,7,0,5]
# l1=[]
# for i in l:
#     if i!=0:
#         l1.append(i)
# n=len(l)-len(l1)
# for i in range(n):
#     l1.append(0)
# print(l1)



############ total even number to start of this list and total odd number end of list---------->>>>>

# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
# # n=len(l)-len(l1)
# for i in l:
#     if i%2!=0:
#         l1.append(i)
# print(l1)



########## Find factor sum ---------->>>>>>>>>>


l=[1,2,5,0,6,0,4,0,2,0,4,0,5,0]
l1=[]
for i in l:
    if i!=0:
        l1.append(i)
n=len(l)-len(l1)
for i in range(n):
    l1.append(0)
print(l1)