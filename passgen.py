# passgen.py
Random code that you may freely use for
Password Generator(1.0)
import random

names=['Liam', #adjust on what type of names you need
'Noah',
'William',
'James',
'Logan']
print('PASSWORD CREATOR 1.0')
print('How long do you want your password to be?')
password_length=0
while password_length < 6:
  print('Please input a number of 6 or higher!')
  password_length=int(input())

password1=random.choice(names)    

while password_length < len(password1):
  password1 = random.choice(names)

while password_length > len(password1):
  if password_length == len(password1):
      break
  password1 += str(random.randint(0,9))

print(password1)


Password Generator(2.0)
import string
import random

print('PASSWORD CREATOR 2.0[SST(super secure technology)]')
print('Length of password?(PLEASE INPUT ONLY INTENGER NUMBERS HERE!!!!!)')

length_p = abs(int(input()))
length_1 = 0
randomiser = 0
password = []

while length_1 <= length_p:
  length_1 += 1
  randomiser = random.randint(1,2)
  if randomiser == 1:
    password.append(random.randint(1,9))
  elif randomiser == 2:
    password.append(random.choice(string.ascii_letters)) #adjustable-ascii_letters->ascii_lowercase or ascii_uppercase to switch between lower or upper case letters respectively.

fn_pass = ""
for i in password:
  fn_pass += str(i)

print(fn_pass)


Password Generator(2.1)
import string
import random

print('PASSWORD CREATOR 2.1[SST(super secure technology)]')
print('Length of password?(PLEASE INPUT ONLY INTENGER NUMBERS HERE!!!!!)')

length_p = abs(int(input()))
length_1 = 0
password = []
LtnNr = string.ascii_letters + string.digits

while length_1 <= length_p:
  length_1 += 1
  password.append(random.choice(LtnNr))

fn_pass = ""
for i in password:
  fn_pass += str(i)

print(fn_pass)


Password Generator(2.5)
import random
import string

print('PASSWORD CREATOR 2.5(Friends Version)')
print('Length of password?(PLEASE INPUT ONLY INTENGER NUMBERS HERE!!!!!)')

def randomString(x):
      LtnNr = string.ascii_letters + string.digits
      return "".join(random.choice(LtnNr) for i in range(x))

length_p = abs(int(input()))
randomString(length_p)
