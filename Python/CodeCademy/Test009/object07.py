from urllib.request import urlopen

kittens = urlopen('http://placekitten.com/200/400')

f = open('kittens.jpg', 'wb')
f.write(bytes(kittens.read()))
f.close()
