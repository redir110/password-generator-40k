import random

chars = "abcçdefghijklmnñopqrstuvwxyzABCÇDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!"

while 1:
    password_1en = int(input("How long would you like your password to be:"))
    password_count = int(input("How many passwords would you like to generate:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_1en):
            password_char = random.choice(chars)
            password    = password + password_char
        print("Here is password: ", password)