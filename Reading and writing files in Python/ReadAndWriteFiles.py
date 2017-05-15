# A program to read and write a file

#Create a file first

#Creating file object
#open a file to write
file = open('Sample.txt', 'w')
file.write('Hello World!\n')
file.write('Welcome to the Python World\n')
#Closing a file object
file.close()


#To read a file
file_read = open('Sample.txt', 'r')

#create variable to store the string which is read from Sample.txt
text = file_read.read()
print(text)