About = {
    "Alekhya": "Me",
    "Tanuja": "My Best friend from School",
    "Teena": "My Best friend from college",
    "Boyfriend": 0
}
print(len(About)) # 4

print(About.items()) 
# dict_items([('Alekhya', 'Me'), ('Tanuja', 'My Best friend from School'), ('Teena', 'My Best friend from college'), ('Boyfriend', 0)])

print(About.keys())
# dict_keys(['Alekhya', 'Tanuja', 'Teena', 'Boyfriend'])

print(About.values())
# dict_values(['Me', 'My Best friend from School', 'My Best friend from college', 0])

About.update({"Alekhya": "I became my best friend", "Relatives": "Snakes"})

print(About.get("Anu")) # None
print(About["Anu"]) # error