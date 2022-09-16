import numpy as np

# array of numbers between 1 and 100 with both numbers
number= [*range(1, 100)]
print(number)

# generate even numbers within the array
even_number= np.array([*filter(lambda x: x%2 == 0, number)])
print(even_number)

#find the LCM of the even numbers.
lcm_even_number = np.lcm.reduce(even_number)
print(lcm_even_number)
