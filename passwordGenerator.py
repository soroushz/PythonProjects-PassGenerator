import string 
import random 

print("Welcome to Password Generator")

# making sure user input the right format 
while True:
    length = input("Enter the length of your password: ")

    if length.isdigit():
        break 
    else:
        print("Invalid input. Please enter digits only.")

# Convert the valid input to an integer
user_number = int(length)

counter = 0
password = ""

while counter < user_number: 

    charachters = random.choice(string.ascii_letters)
    digits = random.choice(string.digits)
    punctuations = random.choice(string.punctuation)  

    options = [charachters, digits, punctuations]

    randomChoice = random.choice(options)
    
    if len(password) < user_number: 

        password += randomChoice

    counter += 1
    
print("Password is: ", password)
print("Length of the password is: ", len(password))