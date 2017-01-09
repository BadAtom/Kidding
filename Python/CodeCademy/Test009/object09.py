import requests
body = {'Name': 'Eric', 'Age': '26'}
# Make the POST request here, passing body as the data:
response = requests.post("http://codecademy.com/learn-http/", body)
# print(response.text)

response_file = open("response.html", "wb")
response_file.write(response.content)
response_file.close()

print(response.status_code)
