import random

# Symbols
symbols = ['!','@','#','$','%','&','*','(',')','-','+']

letters = ['a','b','c','d','e','f','g','h','i',
           'j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','A', 
           'B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S',
           'T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

letters_loop = []
numbers_loop = []

for i in range(ord('A'), ord('Z')+1):
    letters_loop.append(chr(i))
for i in range(ord('a'), ord('z')+1):
    letters_loop.append(chr(i))
for i in range(0,10):
    numbers_loop.append(str(i))

print('Welcome to Passwords Generator!')

# num_up_letters = int(input('How many Up Letters?'))
# num_low_letters = int(input('How many Low Letters?'))
num_letters = int(input('How many Letters?'))
num_symbols = int(input('How many Symbols?'))
num_numbers = int(input('How many Numbers?'))

# up_word = random.randint(ord('A'), ord('Z'))
# low_word = random.randint(ord('a'), ord('z'))
# print(chr(word))

# for n in range(0,num_letters):
#     password.append(letters[random.randint(0,len(letters)-1)])
# for l in range(0,num_symbols):
#     password.append(symbols[random.randint(0,len(symbols)-1)])
# for i in range(0,num_numbers):
#     password.append(numbers[random.randint(0,len(numbers)-1)])


# Easy level

# password = ""

# for letter in range(0,num_letters):
#     password += random.choice(letters)
# for s in range(0,num_symbols):
#     password += random.choice(symbols)
# for num in range(0,num_numbers):
#     password += random.choice(numbers)

# word = random.shuffle(password)
# print(word)




# Hard level

password_list = []

for letter in range(0,num_letters):
    password_list.append(random.choice(letters_loop))
for s in range(0,num_symbols):
    password_list.append(random.choice(symbols))
for num in range(0,num_numbers):
    password_list.append(random.choice(numbers_loop))

random.shuffle(password_list)

word_list =''
for char in password_list:
    word_list += char

print(word_list)


# Up letters
# for letter in range(ord('A'), ord('Z')+1):
#     print(chr(letter))

# Small letter
# for letter in range(ord('a'), ord('z')+1):
#     print(chr(letter))

# Numbers
# for numbers in range(0,10):
#     print(numbers)
