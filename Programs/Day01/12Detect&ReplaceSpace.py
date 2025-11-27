speech = "Alekhya is a good girl.  But she not such a beauty."

# We use find string function to detect anything in a string

print(speech.find("  ")) 
# the output will be the index value in the string.
# in this case. the output is 23.

# Replace the double space from above string with single space.
print(speech.replace("  ", " "))
print(speech)
# Strings are immutable which means that you cannot change them by running functions on them