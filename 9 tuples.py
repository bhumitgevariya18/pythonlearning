# none premitive , it's like a series , immutable
# mutable means changable values and opposite for immutable

week_days = ("Sunday" ,"Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday") 

#example of immutable
# week_days[1] = "Friday" will give error

print (len(week_days))

#indexing

print (week_days[len(week_days) - 1]) # last element
print (week_days[- 1]) # also last element

print (week_days[- 3]) # last element

print (week_days.index("Monday"))

w = ("ab" ,"ab" ,"bc" ,"ab")
print (w.count("ab"))

#also

a , b , c = 1 , 2 , 3
print (b)
co_ordinates = a , c , c , b , a 
print (co_ordinates)
print (sum(co_ordinates) , max(co_ordinates) , min(co_ordinates))

#can also have integer, boolean, another tuple innside
aa = ("AB" , "BC" , True , False , 75 , "AAA" , ("A" , "B" , "C" , (1 , 2 ,3))) 
print(aa[-1])
print(aa[-1][3])
print(aa)

a = ("10")
print(a , type(a)) #it takes it as string not tuple a comma is needed

a = ("10",)
print(a , type(a)) #it is tuple