def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))

fun2 = transmit_to_space("Burn the Sun!")

# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)

# print_msg(9)

# Exercise

# Make a nested loop and a python closure to make functions to get 
# multiple multiplication functions using closures. 
# That is using closures, one could make functions to create 
# multiply_with_5() or multiply_with_4() functions using closures.
print("Exercise")

# your code goes here
def multiplier_of(n):
    "This is the enclosing function"
    def multiplier(number):
         "The nested function"
         return number * n
    return multiplier
    
    

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
