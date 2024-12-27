fruits = ["Apple", "Cars", "Phones"]

# loop
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    # print(fruits)

print(fruits)


student_score = [156, 98, 48, 123, 111, 122]

# another way for a loop 
total = sum(student_score)
print(total)

# its a better way than using it in manual like below

sum = 0
for score in student_score:
    sum += score
print(sum)


max_score = 0
for score in student_score:
    if score >= max_score:
        max_score = score

print(max_score)

print(max(student_score))


# the range is a way for a loop without a list
for number in range(1,11,3): # it will start in 1, it will end in -1 means in 10, 3 is for the step long in here 3 steps 
    print(number)


# a task for find the sum of numbers from 1 to 100 
sum = 0
for number in range(1,101):
    sum += number

print(sum)


# You are going to write a program that automatically prints the solution to the FizzBuzz game. 
# These are the rules of the FizzBuzz game
'''Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"'''

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 5 == 0 :
        print("Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    else:
        print(number)
