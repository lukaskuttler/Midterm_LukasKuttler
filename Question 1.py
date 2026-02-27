import random

random_numbers = []

# create list with 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# go through list using index
for i in range(len(random_numbers)):

    # if number is greater than 50
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)

    # if number is 50 or lower
    else:
        random_numbers[i] = "XX"

# print final list
print(random_numbers)

#This code creates a list of 10 random numbers between 1 and 100.
# Then it goes through the list and replaces numbers greater than 50 with a random number between 20 and 30,
# and numbers lower than 50 with "XX". Finally, it prints the updated list.