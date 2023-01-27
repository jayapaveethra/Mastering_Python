#Data Types

#Strings
print("Hello"[0]) #Prints Capital H
print("123"+"456")

#Integer
print(123+456)

#Float
print(134.67+12.98)

#Boolean
#True
#False

#len function works only with strings, if we give len function to integer it will provide type error

#type checkinng
num_char = len(input("What is your name \n"))
print(num_char)
print(type(num_char))

#type conversion
new_num_char = str(num_char)
print(type(new_num_char))
print("your name as " +new_num_char+" characters") #This line of code will not give error as the new_num_char is string type
#if its in integer type it will throw error

print(str(78)+str(100)) #prints 78100
