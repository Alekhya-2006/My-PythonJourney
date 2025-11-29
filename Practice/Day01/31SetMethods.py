s = { 3, "alekhya", 90, 90, 90, 7,0,9}
print(s, type(s))
# {0, 3, 'alekhya', 7, 9, 90} <class 'set'>

s.add("Tanuja")
print(s)
# {0, 3, 'alekhya', 7, 9, 90, 'Tanuja'}

s.remove(90)# updates the set s and removes 90 from s

print(len(s)) 
s.clear()  # clears the set

s1 = {0, 1, 3, 5, 7, 9}
s2 = {2, 4, 5, 6, 8, 9, 0}

print(s1.union(s2)) # combines s1 and s2 elements
print(s1.intersection(s2)) # common elements in s1 and s2
# Output:
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# {0, 5, 9}

print(s1 - s2) # {1, 3, 7}
print(s2 - s1) # {8, 2, 4, 6}

print({1, 3, 7}.issubset(s1)) # true
print({0, 5, 7}.issubset(s2)) # false

print(s2.issuperset({5,9})) # true

s1.clear()
print(s1)  # Output:set()