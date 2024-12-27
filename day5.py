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
