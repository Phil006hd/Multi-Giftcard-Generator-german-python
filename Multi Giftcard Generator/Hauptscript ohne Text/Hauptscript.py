import time
import random 

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result
print("Version 0.1")
print("---Multiple Gift Card Generator---")
print("")
print("What Giftcard do you want to Generate?")

tt = input("\n1-Amazon\n2-Roblox\n3-Webkinz\n4-Fortnite\n5-Disney+\n6-Ebay\n7-Netflix\n8-iTunes\n9-Paypal\n10-Visa\n11-PokemonTGC\n12-Playstation\n13-Steam\n14-Xbox\n14-PlayStore\n15-Minecraft\n\nName? >>")

t = tt.lower()
print("")
print("How many do you want to Generate?")
nn = input(">>")
print("")
n = int(nn)

if t == "minecraft":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "paypal":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "playstation":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))
		
if t == "amazon":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "netflix":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))
		
if t == "steam":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(5))
		
if t == "fortnite":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(4)+"-"+g(4))
		
if t == "robolox":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(3)+"-"+g(4))
		
if t == "itunes":
	for x in range(n):
		print("")
		print(g(16))
		
if t == "ebay":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "Disney+":
	for x in range(n):
		print("")
		print(g(10))
		
if t == "webkinz":
	for x in range(n):
		print("")
		print(g(8))
		
if t == "disney+":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(4)+"-"+g(3)+"-"+g(3))
		
if t == "playstore":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
		
if t == "xbox":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))

print("")
print("-----Generation completed  (100%)-----")
time.sleep(120)
