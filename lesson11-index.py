# LESSON 11 INDEX

# first_name = 'Alexander'

# print(first_name[8])  # => r

first_name = 'Alexander'
index = 0

print(first_name[3])  # => x

# LABS
# Task:You have three variables with the last names of different people. Compose and display a word from the characters in this order:
#
# The third character from the first line
# The second character from the second line
# The fourth character from the third line
# The fifth character from the second line
# The third character from the second line
# Try using interpolation. Inside curly brackets, you can place not only variables, but also individual characters of the string extracted by index (using square brackets).

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
