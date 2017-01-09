from xml.dom import minidom as md

try:
    with open("pets.txt") as file:
        pets = md.parseString(file.read()).getElementsByTagName('pet')
except FileNotFoundError:
    print("File doesn't exist:", FileNotFoundError)
else:
    s_pets = {}
    get = lambda dom_el, name: dom_el.getElementsByTagName(name)[0].firstChild.nodeValue
    for pet in pets:
        s_pets[get(pet, 'name')] = get(pet, 'species')

    print(s_pets)
