# a = ["a" , "b" ,"c" , "d" , "e"]
# print (a)
# print (a[2])

# a.append("hello")
# a.append("hiii")
# print (a)

# a.pop()
# c = a.pop(3)
# print (c)
# print (a)

# a.insert(3,"abcd")
# print (a)

# a.insert(-1,"abcd") #slight different , use len(a) for adding at end by insert
# print (a)

# a.remove ("abcd")
# print (a)

# a[-1] = "heyyy"
# print (a)  # also insert

# b = ["hi" , "I" , "am" , "Bhumit"]
# sentence = " ".join(b)
# print (sentence)
# print(sentence.split(" "))

# s = list("Hello")
# print (" ".join(s))

# g = str(b)
# print (g)
# print (g.split(" "))



#task 
#take an input of 3 names , seperated by commas to have a list of 3 elements
#change the middle element by negative indexing
#pop last element and insert in middle
#append new name and remove first name
#join them together with comma and print them

a = []
a.append(input("Enter first name : "))
a.append(input("Enter second name : "))
a.append(input("Enter third name : "))
print (a)

a[-2] = "Ajay"
print(a)

b = a.pop(2)
a.insert(1,b)
print(a)

a.append("Binod")
a.pop(0)
print(a)

print (",".join(a))