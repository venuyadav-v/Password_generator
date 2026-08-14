#Password Generator
import random
print("Welcome to the passsword generator!...")
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
           "P","Q","R","S","T","U","V","W","X","Y","Z",
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z']
spetial=["~","!","@","#","$","%","^","&","*","(",")"]
numbers=['0','1','2','3','4','5','6','7','8','9']
alp=int(input("How many letters would you like in your password?"))
spc=int(input("How many spetial charactors would you like in your password?"))
num=int(input("How many numbers would you like in your password?"))
password=[]
for i in range(1,alp+1):
    char=random.choice(alphabets)
    password +=char
for i in range(1,spc+1):
    char=random.choice(spetial)
    password+=char
for i in range(1,num+1):
    char=random.choice(numbers)
    password+=char
print(password)
random.shuffle(password)
print(password)
final_passpord=""
for i in password:
    final_passpord+=i
print(final_passpord)