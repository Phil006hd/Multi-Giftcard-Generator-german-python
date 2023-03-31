#!!!Wichtig das script ist zum generieren von random codes / giftcards. das ist nur eine vorlage die codes werden für die optionen nicht funktionieren.



#benötigte dinge fürs script
import time
import random 

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"        #das ist die liste woraus der code bestehen soll. Kannst du ändern
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result
print("Version 0.1")            #version vom script
print("---Multiple Gift Card Generator---")       #Überschrift. kann geändert werden
print("")                                         #1 zeile abstand
print("What Giftcard do you want to Generate?")   # Text kann geändert werden

tt = input("\n1-Amazon\n2-Roblox\n3-Webkinz\n4-Fortnite\n5-Disney+\n6-Ebay\n7-Netflix\n8-iTunes\n9-Paypal\n10-Visa\n11-PokemonTGC\n12-Playstation\n13-Steam\n14-Xbox\n14-PlayStore\n15-Minecraft\n\nName? >>") #auslistung von den dingen,
                                                                                                                                                                                                               #die generiert werden können. könnte ihr ändern muss aber unten mit den namen gleich geändert werden.
t = tt.lower()
print("")
print("How many do you want to Generate?") #text änderbar
nn = input(">>")  
print("")
n = int(nn)

#wichtiger teil vom script 
#das sind alle namen die eingegeben werden können zu generieren.
#die namen können angepasst werden

if t == "minecraft":    #name ist änderbar
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))      #das ist die anzahl wie lang der code sein soll also 1234-1234-1234 ist als größe (4) im script 3 mal angegeben. das könnt ihr auf z.b print(g(6)+"-"+g(6)+"-"+g(6)) ändern dan kommt als code 123456-123456-123456 raus. ihr könnt auch unterschiedliche code machen wie print(g(2)+"-"+g(1)+"-"+g(7)).
		
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
		print(g(16))   #hier ist der code 16 nummern oder buchstaben lang ohne bindestrich. könnt ihr ändern je nachdem wie lang der code sein soll.
		
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
print("-----Generation completed  (100%)-----")  #das ist der text wenn alle codes fertig Generiert wurden.
time.sleep(120)     #das ist die zeit bis sich das fenster automatisch schließt also 120 sekunden.
