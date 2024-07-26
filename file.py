f=open('thisfile.txt','r')          # Open the file in read mode
for i in range (2):       
    text5=f.readline()              # Read and print the first two lines of the file
    print(text5)
text1=f.read()
text2=f.readline()
text3=f.readlines()
text6=f.readline(4)                 # Read the first 4 characters from the file
f=open('thisfile.txt','r+')         # Open the file in read and write mode
num=f.write('hello world')         #you cant write anything in read mode i.e first open file in read and write mode(r+)
num2=f.read()

print(num2)
f.close()
