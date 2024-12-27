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
