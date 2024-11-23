import random

print('This is your password: ')
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+|<>?'
password =''
for x in range (16):
    password += random.choice(chars)

    print(password)