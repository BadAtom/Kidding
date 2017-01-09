import json
import _json

pets = json.loads(open('pets2.txt').read())
print(pets)
print(type(pets))
print(type(pets['pets']))
