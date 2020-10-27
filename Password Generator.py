
# =============================================================================
# PASSWORD GENERATOR
# =============================================================================



@author: gagashsan
"""
import random

num_of_pass = int(input('Enter the number of password you would like to get? :  '))
pass_length = int(input('Enter the length of the password you would like to get? :  '))

    
chars = 'abcdefghijklmnopqrstuvwxyz123456789!//\\'

for i in range(num_of_pass):
    password = ' '
    for p in range(pass_length):
        password += random.choice(chars)
        
        
    print(password)

    
