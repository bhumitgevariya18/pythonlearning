#string

x = "heLLo pYthon"

print(x.upper())
print(x.lower())
print(x.title())
print(x)

x = "daghfllla fd ff ll"

print (x.count("l"))
print (x.count(""))
print (x.split("l"))
print (x.replace("f","$"))



a = "hii this is a parrot"
print(a.replace("this","that").replace("parrot","crow")) 
# by giving number value with replace fun, we can control the no of time we can replace

# print (a.reverse()) error will see this later

print (a.index("p"))
print (len(a))

print (a.startswith("h"))
print (a.startswith("H"))
print (a.startswith("a"))
print (a.startswith("hii "))

print (a.endswith("parrot"))

#slicing will be done later

pi = 3.14159265
print (f"The value of pi is {pi : .2f}")



#task
# take a full name input from user
# output total no of vowels
# print the index of first vowel
# split the name on most occuring vowel
# replace most used vowel with second most used vowel
# split on second most used vowel
# print out the length

n = input("Enter your name : ")
m = n.lower()
v1 = m.count("a")
v2 = m.count("e")
v3 = m.count("i")
v4 = m.count("o")
v5 = m.count("u")

vt = v1 + v2 + v3 + v4 + v5
print ("total no of vowels are",vt)

print (n.index("i"))
print (n.split("i"))
print (n.replace("i","a"))
print (n.split("a"))
print (len(n))
