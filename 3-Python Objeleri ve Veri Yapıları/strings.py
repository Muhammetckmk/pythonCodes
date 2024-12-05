name = 'Muhammet'
surname = 'Çakmak'
age = 32

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting)

print(greeting)
print(greeting[0])
print("b : ", greeting[3])
print(greeting[length-1])
print("a : ",greeting[-1])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:3])