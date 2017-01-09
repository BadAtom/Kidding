from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError

request = Request("http://placekitten.com")

try:
    response = urlopen(request)
    kittens = str(response.read())
    kittens = kittens[575:1110].split("\\n")
    for line in kittens:
        print(line)
except URLError as e:
    print("No kittenz here:", e)
