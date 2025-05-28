#file_hendling-->
#store data permanentally
#operation-->
#open()
#read()/write()
#close()


# f=open('n1.py','x')
# print("file created")----->(error show file pehle se h)

# "x" creat mode-->

# f=open('n2.py','x')
# print("file created")
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# "w" write mode and creat file and overrite data -->

# f=open('n3.py','w')
# print("file created")
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# "r"readable mode and not creat file-->

# f=open('n3.py','r')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# "a" append and creat file--->

# f=open('x1.py','a')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)