""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """



""" day_of_week = input("what day is it? ")
if day_of_week == "Friday" or "friday":
    print("correct")
else:
    print("incorrect") """
    

tip = input("How was your experience today? ")
bill = input("What was your total price? ")
if tip == "bad":
    print("Here is your final total:", bill)
if tip == "ok":
    print("Here is your final total:", (float(bill)*1.15))
if tip == "good":
    print("Here is your final total:", (float(bill)*1.20))
if tip == "great":
    print("Here is your final total:", (float(bill)*1.25))


