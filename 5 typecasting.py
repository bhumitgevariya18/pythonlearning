print (int(9.6))
print (int(-6.4))
print (int(True))
print (int(False))
print (int("25"))
print (int("-95"))
#print (int("45.78")) its a float written as string, gives error
print (int("46") + 75)
#print (int(4 + 5j))

print (float(47))
print (float (True))
print (float("42"))
print (float("21.45") , 21.45)

print (str("345.453"))

a = str(-3.78)
print (a , type(a))

a = str(False)
print (a , type(a))

a = bool(4)
print (a , type(a))

a = bool(-7.24)
print (a , type(a)) #boolean just check magnitude, just zero or non zero thats why shows true , even in float and negative

a = bool("False")
print (a , type(a)) # also shows true because of non empty value in case of sring also for 0

a = bool("")
print (a , type(a))

a = bool(None)
print (a , type(a))

# task 
# we take a deccimal input from user 
# convert it into an integer 
# convert it into string 
# print it 5 times

a = float(input("Enter a decimal input : "))
b = (int(a))
print (str(b)*5)

