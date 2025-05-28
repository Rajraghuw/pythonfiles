# #static variable--> (yese variable jo object badalne ke sath apni value nahi badalte hai static variable hote hai)
# #instance variavle-->(yese variable jo object badalne ke sath apni value badalte hai instance variable hote hai)

# class student:
#     school='shss'   #static/class variables
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         student.city='bhopal' #static/class variable
#     def add_more(self):
#         student.gread='10th' #static/class variable
#     def show_details(self):
#         print(student.school,student.city,student_city1,student.gread)

# object=student('raja',22)
# object.add_more()
# student_city1='indore' #static/class variable
# object.show_details
# # print(object.school)
# # print(student.school)
# # print(student.city,student.gread)



#local variable-->

q=50             #global variable 
class student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        z=10            #local variable
        print(z)
    def show(self):
        p=10
        print(p)       #local variable
        print(q)

object=student(10,20)
object.show()