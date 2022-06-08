# The expressions in variables
# vars
rubles_per_dollar = 60
dollars_count = 50 * 1.25 # 62.5
rubles_count = dollars_count * rubles_per_dollar
# print(rubles_count)
# !!!! Concatenation. Fun str() turns a number into a string
print('The price is ' + str(rubles_count) +' rubles') # => The price is 3750.0 rubles

# what = "Kings" + "road"
# print(what) # => "Kingsroad"

first = "Kings"
what = first + "road"
print(what) # => Kingsrouad

# first = "Kings"
# last = 'road'
# what = first + last
# print(what)  # => "Kingsroad"

# print(60 * 50 * 4)
# first = 'brave'
# middle = 'new'
# last = 'world'
# space = ' '
# print(first + space + middle + last)

# LABS
# Task: It is necessary to write a program that takes the initial amount of euros recorded in the errors_count variable,
# converts euros into dollars and displays it on the screen
# Then the resulting value is converted to rubles and displays on a new line.
# Example for 100 eur  125.0  7500
# 1 EU = 1.25 UD
# 1 UD = 60 RUB

euros_count = 100
euros_per_dollar = euros_count * 1.25
print(euros_per_dollar)
dolar_per_rubles = euros_per_dollar * 60
print(dolar_per_rubles)
