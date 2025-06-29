#oops : real word 

#Class : class physicaly axest ni karti hain ye basically ak domy modal type hoti hai ye kisi v object ka disign ya dommy model class kahlata hai  ,,,
# object: class jb bhi physically axest karti hai wo object kahlata hai --->  
            

#class syntex:--> class name ka first letter capital rkhte hai
#class Class-name:
         #"doc string"  (discription)
        # variable  (properties) (jitni cheeje dikhai de rhi hai wo variable )
          # method   (behaviour)

# class First :
#     pass
# print(id(First))
# obj=First
# print(id(obj))
# obj1=First()
# print(id(obj1))


# #constructor : constructor ak method hai jo object creat karte hi otometic call ho jata hai constroctor 2 type ke hote hai ak user defined ak inbuild
# #   |--->> __init__
# class first:
#     "hellow"
#     pass
# print(dir(first)) # magic method isse ham object ko access kar sakte hai -->>
# print(first.__doc__) # doc string ko access karne ke liye ,,,

#self ak refrence variable hai jo current object ka address hold karta hai :
  #                ^
   #               | 
# class first:  #    |
#     def __init__(self):
#         print("constroctor call")
#         print(id(self))

# #obj=first
# obj=first()
# print(id(obj))




#methods -->>>
#instance methoud --->> iska pehla perameter self hota hai
#class methoud  --->> iska pehla perameter cls hota hai
#static methoud --->> 


#class methoud -->> iska use ham class variable ko update karne ke liye karte hai or ak naya variable creat karne ke liye,,,

# class student:
#     school='shss'
#     grad='10th'
#     def __init__(self,name):
#         self.n=name
#     def show_details(self):
#         print(self.n)
#         print(student.school)
#         print(self.grad)
#         print(student.city)
#     @classmethod                    #  @ - cls ko class ke name jodta hai,,,
#     def update_gread(cls,updated):
#           cls.grad=updated
# #new variable add karne ke liye -->
#     @classmethod                    
#     def add_new(cls,city):
#         cls.city=city

# obj=student('raja')   #class methoud me direct class ke name se function call karte hai or argunment pass karte hai
# # obj.show_details()
# student.update_gread('11th')
# obj2=student('raghuwanshi')
# # obj2.show_details()
# student.add_new('bhopal')
# obj2.show_details()




#static methoud--->> iska use ham generaly apni website pr user ko welcome or thank you bolne ke liye karte hai


# class student:
#     school='shss'
#     grad='10th'
#     def __init__(self,name):
#         self.n=name
#     def show_details(self):
#         print(self.n)
#         print(student.school)
#         print(self.grad)
#         # print(student.city)
#     @staticmethod                    #  @ - cls ko class ke name jodta hai,,,
#     def update_gread(cls,updated):
#           cls.grad=updated
# #new variable add karne ke liye -->
#     @staticmethod                    
#     def add_new(self,cls,city):
#         print(self)
#         print(cls)
#         print(city)

# obj=student('raja')
# # obj.show_details()
# # student.update_gread('11th')
# obj2=student('raghuwanshi')
# # obj2.show_details()
# student.add_new('bhopal','indore','gijraat')
# obj2.show_details()



#welcome and thankyou code static variables----->>>>
# class student:
#     school='shss'
#     grad='10th'
#     def __init__(self,name):
#         self.n=name
#     def show_details(self):
#         print(self.n)
#         print(student.school)
#         print(self.grad)
#         # print(student.city)
#     @staticmethod                    #  @ - cls ko class ke name jodta hai,,,
#     def update_gread(cls,updated):
#           cls.grad=updated
# #new variable add karne ke liye -->
#     @staticmethod                    
#     def welcome():
#         print('welcome')

# obj=student('raja')
# # obj.show_details()
# # student.update_gread('11th')
# obj2=student('raghuwanshi')
# # obj2.show_details()
# student.welcome()
# obj2.show_details()


#property------>>>>>>>>


# abstraction 
# inharitence
# polymorphism
# encapsulation

# inharitence 
# 1 singal level  ----> parent -----> childe 
# 2 multilevel   ------> grand parent ----> parent ----> childe 
# 3 multiple inharitence  -----> father mother -----> childe 
# 4 hierarichical  ---> parent ----__child1 , child2 
# 5 hybride  ---> parent ----____ child1,child2 -----> child


#(1) Single-level----> ak class ko dusri class me inherite karne ke liye,,,,,

# class Gperent:
#     def car(self):
#         print("can from gperent class")

# class Perent(Gperent) :    # inharitence kiya hai code resubilty bolte hai ise
#     x=10
#     def __init__(self,name):
#         self.name=name
#     def home(self):
#         print("home from perent class")
# class Child(Perent):     # yha pr perent class inheridence hai ,,,,
#     # pass
#     def home(self):
#         print("home from perent class")     #methoud overiding sem name ki do methoud python supported 
#         super().home()     # super ka use ham perent ke functions ko acces karne ke liye karte hai 
# obj=Child('python')  
# print(obj.x)
# print(obj.name)
# obj.home()
# obj.car() 






# class perent1:
#     def car(self):
#         print("can from gperent class")

# class Perent2 :    # inharitence kiya hai code resubilty bolte hai ise
#     x=10
#     def __init__(self,name):
#         self.name=name
#     def home(self):
#         print("home from perent class")
# class Child (perent1,Perent2):     # yha pr perent class inheridence hai ,,,,
#     # pass
#     def home(self):
#         print("home from perent class")     #methoud overiding sem name ki do methoud python supported 
#         super().home()     # super ka use ham perent ke functions ko acces karne ke liye karte hai 
# obj=Child('python')  
# print(obj.x)
# print(obj.name)
# obj.home()
# obj.car() 





# class Perent:    # inharitence kiya hai code resubilty bolte hai ise
#     x=10
#     def __init__(self,name):
#         self.name=name
#     def home(self):
#         print("home from perent class")
# class Child1(Perent):     # yha pr perent class inheridence hai ,,,,
#     # pass
#     def home(self):
#         print("home from perent class")     #methoud overiding sem name ki do methoud python supported 
#         super().home()     # super ka use ham perent ke functions ko acces karne ke liye karte hai 
# class Child2(Perent):
#     pass

# obj1=Child1('python')
# obj2=Child2('java')  
# obj1.home()
# obj2.home()
# print(obj1.x,obj2.x)



# class Student:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#         print("this is student class")
# s1=Student("raja raghuwanshi", 90)
# print(s1.name,s1.marks)
# s2=Student("sourabh joshi", 95)
# print(s2.name,s2.marks)


## Creat student class that takes name & marks 3 subject as argouments in constructor then creat a methoud to print the average  ### 

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("hy",self.name,"your average is",sum/len(self.marks))

# s1=Student("raja raghuwanshi", [90, 80, 70])
# s1.average()


#### use @staticmethoud decorator ####

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod
#     def hellow():
#         print("hellow")

#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("hy",self.name,"your average is",sum/len(self.marks))

# s1=Student("raja raghuwanshi", [90, 80, 70])
# s1.average()
# s1.hellow()  # static methoud ko class ke name se call karte hai
        
        
# ######private attribute and method #####

# class Account():
#     def __init__(self,account,password):
#         self.account=account
#         self.__password=password  # private attribute represented by __

# s1=Account("raja", "1234")
# print(s1.account)
# print(s1.__password)  # this will give an error because __password is private



###### inheritance methoud #####

# class car:
#     @staticmethod
#     def start():
#         print("car is started")
#     @staticmethod
#     def stop():
#         print("car is stopped")

# class toyota(car):
#     def __init__(self, name):
#         self.name=name

# s1=toyota("fortuner")
# s2=toyota("innova")

# print(s1.start())


#### multi level inheritance #####

class car:
    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class toyota(car):
    def __init__(self, brand):
        self.brand=brand

class fortuner(toyota):
    def __init__(self, type):
        self.type=type
        super().stop()  # super() function calling parent class method
        
s1=fortuner("diesel")
s1.start()  # calling parent class method
print(s1.type)

