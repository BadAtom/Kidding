import requests
# Make a GET request here and assign the result to kittens:
kittens = requests.get("http://placekitten.com")
print(kittens.text[558:1050])

print(requests.utils.__version__)
print(kittens.status_code)
