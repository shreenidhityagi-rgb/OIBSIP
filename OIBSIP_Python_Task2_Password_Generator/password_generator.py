# Random Password Generator
# Oasis Infobyte Python Programming Internship - Task 2

import random
import string

print("Random Password Generator")

# Take password length from user
length = int(input("Enter the desired password length: "))

# Define character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display password
print("Generated Password:", password)
