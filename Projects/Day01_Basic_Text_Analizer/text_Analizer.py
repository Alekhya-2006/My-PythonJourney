"""
TEXT ANALYZER TOOL :

Features:
- Counts total characters
- Counts characters excluding spaces
- Counts total words
- Counts unique words
- Counts keyword occurrences (good, bad, happy, sad)

Concepts Used:
- Strings
- Lists
- Tuples
- Dictionaries
- Sets

"""

#  Input text
text = input("\nEnter your paragraph for analysis:\n\n> ")

#  Convert to lowercase for uniformity
processed = text.lower()

#  Split words into list
words = processed.split()

#  Convert to set → find unique words
unique = set(words)

#  BASIC TEXT STATISTICS 
total_characters = len(text)
characters_no_space = len(text.replace(" ", ""))
word_count = len(words)
unique_count = len(unique)

#  KEYWORD COUNTS USING TUPLE 
keywords = ("good", "bad", "happy", "sad")  # Editable for expansion

good = processed.count("good")
bad = processed.count("bad")
happy = processed.count("happy")
sad = processed.count("sad")

#  STORE IN DICTIONARY 
stats = {
    "Total Characters (with spaces)": total_characters,
    "Characters (without spaces)": characters_no_space,
    "Total Words": word_count,
    "Unique Words": unique_count,
    "good Count": good,
    "bad Count": bad,
    "happy Count": happy,
    "sad Count": sad
}

# --- RESULT OUTPUT (NO LOOPS) ---
print("\n TEXT ANALYSIS RESULT \n")
print("Characters With Spaces :", stats["Total Characters (with spaces)"])
print("Characters Without Space:", stats["Characters (without spaces)"])
print("Total Words             :", stats["Total Words"])
print("Unique Words Count      :", stats["Unique Words"])

print("\n Keyword Appearance ")
print("good  →", stats["good Count"])
print("bad   →", stats["bad Count"])
print("happy →", stats["happy Count"])
print("sad   →", stats["sad Count"])

print("\nUnique Words Found (set form):")
print(unique)

print("\n")
print("   Analysis Complete Successfully!")
print("\n")