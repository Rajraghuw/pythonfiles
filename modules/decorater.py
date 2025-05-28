#kisi bhi function ke andr jo v code likha hua h uske code 
# ko bina change kiye huye uska behaviour change karne ke liye decorater ka use karte hai fun

def decor(z):
    def inner(x,y):
         print(x+y)
         print(z)
    return inner
def mainfun():
    print("main function")

x=decor(10)
p=5
q=8
x(p,q)

