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
    

""" tip = input("How was your experience today? ")
bill = input("What was your total price? ")
if tip == "bad":
    print("Here is your final total:", bill)
elif tip == "ok":
    print("Here is your final total:", round(float(bill)*1.15, 2))
elif tip == "good":
    print("Here is your final total:", round(float(bill)*1.20, 2))
elif tip == "great":
    print("Here is your final total with tip:", round(float(bill)*1.25, 2))
else:
    print("That's not what I asked. Re-run it and be real.") """

""" number = int(input("Enter number: "))
if (number % 2) == (0):
    print((number), "is even")
if (number % 2) == (1):
    print((number), "is odd") """

""" print("Enter simple equation")
input1 = input()
input2 = input()
input3 = input()
if (input2) == "+":
    print("=", float(input1)+float(input3))
elif (input2) == "-":
    print("=", float(input1)-float(input3))
elif (input2) == "x":
    print("=", float(input1)*float(input3))
elif (input2) == "/":
    print("=", float(input1)/float(input3))
else:
    print("Sorry I can't do allat. ERROR") """


""" factornumber = int(input("Enter number: "))
factor = []
for i in range(1, factornumber+1):
    if factornumber % i == (0):
        factor.append(i)
if len(factor) < 3:
    print("This is a prime number. Its only factors are 1 and itself:")
print(factor) """
    

GCFnum1 = int(input("Enter number: "))
GCFnum2 = int(input("Enter another number: "))
factor = []
for i in range(1, GCFnum1+1):
    if GCFnum1 % i == (0) and GCFnum2 % i == 0:
        factor.append(i)
print(factor[-1])
    
