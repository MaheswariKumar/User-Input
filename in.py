#Chapter-7
#User input and while loops 
#Simple input
msg = input("write something here: ")
print(msg)

#clear input
name = input("tell your name plz: ")
print("hi " + str(name) + " you passed the interveiw")

prompt = "if you tell your name i will check you passed the exam or not"
prompt += "\nname plz: "
msg = input(prompt)
print(msg)

#int() for numerical input => convert a string representation of number to the numerical representation
age = input("enter a age: ")
age = int(age) 
if age >= 18:
	print("you can vote")
else:
	print("you can't")

#Modulo Opertor => % it will give the remainder
num = 6
if num % 2 == 0:
	print("even")
else:
	print("odd")

#Ass-1
car = input("which car you want to buy: ")
print("this " + str(car) + " is available" )

#Ass-2
user = input("how many you ppl came: ")
user = int(user)
if user >= 8:
	print("sorry you should wait")
else:
	print("table is ready")

#Ass-3
num = int(input("enter a num: "))
if num % 2 == 0:
	print("even")
else:
	print("odd")