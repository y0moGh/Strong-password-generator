import random
import string
import argparse

def parsing():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', default=8, help='Your password lenght. Default is 8')
    values = parser.parse_args()
    
    return values.length

def create_pass(length, chars):
    password = ""
    for i in range(int(length)):
        password += random.choice(chars)
    return password

chars = string.ascii_letters + string.digits + string.punctuation
length = parsing()
final_password = create_pass(length, chars)

print("Your password is " + final_password)