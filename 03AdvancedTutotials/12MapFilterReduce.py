# Say I have a list (iterable) of my favourite pet names, 
# all in lower case and I need them in uppercase. 
# Traditonally, in normal pythoning, I would do something like this:

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# uppered_pets = list(map(str.upper, my_pets))
mapUpperedPets = list(map(str.upper, my_pets))

print(mapUpperedPets)

# Say I have a list of circle areas that I calculated somewhere, 
# all in five decimal places. 
# And I need to round each element in the list up to its position 
# decimal places, meaning that I have to round up the first element 
# in the list to one decimal place, the second element in the list to 
# two decimal places, the third element in the list to three decimal 
# places, etc. With map() this is a piece of cake. Let's see how.

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
print(circle_areas)
result = list(map(round, circle_areas, range(1,7)))
print(result)

result2 = list(map(round, circle_areas, range(1,3)))
print(result2)

#zip()
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results3 = list(zip(my_strings, my_numbers))

print(results3)

#The following is a list (iterable) of the scores of 10 students 
# in a Chemistry exam. Let's filter out those who passed with scores 
# more than 75...using filter.

# Python 3
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# Testing GIT