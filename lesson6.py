print("Dragon's mother said \"No\"")

# Escaped sequences
print("- Are you hungry?\n-Aaaaaraagh!")
print("Gregor Clegane\nDunsen\nPolliver\nChiswyck")
print("Joffry loves using \\n")

# Concatenation
# The operator is the same as when adding numbers, but here it has a different meaning (semantics)
print('Dragon' + 'stone')
print('Kings' + 'wood')  # => Kingswood
print('Kings' + 'road')  # => Kingsroad
print("King's" + 'Landing')  # => King'sLanding

# We put space in the left part
print("King's " + 'Landing')  # => King's Landing
# We put space in yhe right part
print("King's" + ' Landing')  # => King's Landing

# LABS
# TASK
# Write a program that displays:
# - Did Joffrey agree?
# - He did. He also said "I love using \n".
# !! In this case, the program uses only one print(),
# but the result on the screen should look exactly as shown above

print("- Did Joffrey agree?\n- He did. He also said \"I love using \\n\"." ) # => PASS TEST 