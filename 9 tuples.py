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
