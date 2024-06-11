a = input ("Enter your Name : ")
b = float (input ("Enter your Height in m : "))
c = float (input ("Enter your weight in kg : "))
i = round(c / b**2 , 2)
if i <= 0 :
 {
   print (f"{a}, Your bmi is {i} and it can't be negative, Enter valid inputs") 
 }
elif i <= 18.5 :
 {
   print (f"{a}, You are underweight with a bmi of {i}") 
 }
elif i > 18.5  and i <= 25 :
 {
   print (f"{a}, You are Normal with a bmi of {i}") 
 }
elif i > 25 and i <= 30 :
 {
   print (f"{a}, You are slightly overweight with a bmi of {i}") 
 }
else :
 {
   print (f"{a}, You are obese with a bmi of {i}") 
 }
