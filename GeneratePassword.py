'''

Random Password Generator using Python

by Michael Aladejobi

'''

#import the necessary modules!

import random

import string

print('Hello!, Welcome to Password generator!')

#input the length of password

length = int(input('\nEnter the length of password: '))                      

#define data

lower = string.ascii_lowercase

upper = string.ascii_uppercase

num = string.digits

symbols = string.punctuation

#string.ascii_letters

#combine the data

all = lower + upper + num + symbols

#use random modules

temp = random.sample(all,length)

#create the password 

password = "".join(temp)

#display the password

print(password)
