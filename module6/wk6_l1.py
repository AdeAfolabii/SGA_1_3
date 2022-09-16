import numpy as np
#check
print('done successfully')


#Creating a list of integers between numbers from 5.5 to 20.5
numbers = [int(i) for i in np.arange(5.5, 20.5)]
print([*(numbers)])
print(len(numbers))

#getting the count of odd numbers in the list 
odd_num = [*filter(lambda i: (i%2 != 0), numbers)]
print(len(odd_num))

#getting the count of even numbers in the list 
even_num =[*filter(lambda i: (i%2 == 0), numbers)]
print(len(even_num))

#getting the square and cubeof every number in the list
s_c = [*map(lambda x: (x, x*x, x*x*x), numbers)]
print(s_c)