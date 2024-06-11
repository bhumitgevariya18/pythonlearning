print("hello a", 5 , 9.2 , True , sep="--")
print (34, "heyy", sep="")
print (34, "heyy", sep="\n" , end="\n")
print (34, "heyy", sep="")
fname = "Bhumit"
lname = "Gevariya"

fullname = "{} {}".format(fname , lname)

print("My name is " + fname + " " + lname)
print("My name is" , fname , lname)
print("My name is {} {}".format(fname , lname))
print("My name is" , fullname)

print("My \nname is \t{fname} {lname}.")
#\n new line \t tab \v newline \b backspace
print(f"My name is {fname} {lname}.")

print(r"My name is {fname} {lname}.") #row


#assignment

fname = "Bhumit"
lname = "Gevariya"
h = 6
a = 20
p = "Ahmedabad"
fullname = "{} {}".format(fname , lname)

print("My name is" , fullname)
print("My height is " , h , "feet")
print(f"I am {a} years old.")
print("I live in {}".format(p))

