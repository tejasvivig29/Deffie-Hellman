import random
value_p = input("Enter the value of p ")
value_g = input("Enter the value of g ")
p = int(value_p)
g = int(value_g)
SA = random.randint(1,10)
SB = random.randint(1,10)
print("\n")
print("The value of SA ",SA)
print("The value of SB ",SB)
print("\n")
print("The value of p ",p)
print("The value of g ",g)
TA = (g**SA)%p
TB = (g**SB)%p
print("The value of TA ",TA)
print("The value of TB ",TB)
secretkeya = (TB**SA)%p
secretkeyb = (TA**SB)%p
if(secretkeya == secretkeyb):
	print("We found the secret key ",secretkeya)
else:
	print("We haven't found the secret key")




