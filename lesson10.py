# INTERPOLATION

# without intrpolation
first_name = 'Joffrey'
greeting = 'Hello'

print(greeting + ", " + first_name + "!")  # => 'Hello, Joffrey!'
# with intrepolation Exm 1
first_name = 'Joffrey'
greeting = 'Hello'

print(f'{greeting}, {first_name}!')  # => 'Hello, Joffrey!'

# Exm 2
school = 'Hexlet'

what_is_it = f'{school} - online courses'
print(what_is_it)  # => 'Hexlet - online courses'

# Multi-line exm
text = '''Example of a text
consisting of
several lines
'''
print(text)

# LABS
# Task:Display two lines on the screen: Do you want to eat, <name>?  Yes, I'm hungry, mom.
# where instead of <name>, the <stark> variable must be used

strak = 'Arya'
text = f'''Do you want to eat, {strak}?
Yes, I'm hungry, mom.'''
print(text)
