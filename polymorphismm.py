#polymorphism----->>>>>>>

#kisi bhi ak function ka ak se jyada form hona polymorphism kahlata hai
#


s='python'
l=['python','java']
t=('python','java')

print(max(s))
print(max(l))
print(max(t))


#ak hin function ka ak se jyada form hone example----->
class student:
    def __init__(self):                # python recomended ak hi constructor use karna hai overlode nhi karna hai
        print('from 1st constrectory')
    def __init__(self,x,y,z):               #is cenerio ko ham overloding karte hai or python overlod support nhi karta hai
                                             #ise ham cunstructtor overlode bhi bolte hai
        print('from 2nd constrectory')

obj=student()        #  ye bydefault 2nd function ko call karega