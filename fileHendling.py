# Character           # Meaning

# 'r'                 open for reading (default)

# 'w'                 open for writing, truncating the file first

# 'x'                 create a new file and open it for writing

# 'a'                 open for writing, appending to the end of the file if it exists

# 'b'                 binary mode

# 't'                 text mode (default)

# '+'                 open a disk file for updating (reading and writing)

#  Syntex : variable = open("fileName", "mode")

# f=open("fileHendling.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


# f=open("fileHendling.txt","r")
# data=f.read(5)             # Read first 5 characters
# print(data)
# print(type(data))
# f.close()


# f=open("fileHendling.txt","r")
# line1=f.readline()   # Read first line
# # line2=f.readline()   # Read second line
# print(line1)
# print(type(line1))
# f.close()



# Writing to a file

# "w" write

# f = open( "demo.txt", "w")

# f.write("this is a new line")  #overwrites the entire file

# f = open( "demo.txt", "a")

# f.write("this is a new line") #adds to the file



f=open("fileHendling.txt","w")
f.write("this called raja raghuwanshi")
f.close()

f=open("fileHendling.txt","a")
f.write("  and my student id is 123456789")
f.close()