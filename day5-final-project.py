import random

word = random.randint(ord('A'), ord('Z'))
print(chr(word))

# Up letters
for letter in range(ord('A'), ord('Z')+1):
    print(chr(letter))

# Small letter
for letter in range(ord('a'), ord('z')+1):
    print(chr(letter))
