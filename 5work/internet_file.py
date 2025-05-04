import  requests

# url = "https://www.olx.ua/uk/"
#
# response = requests.get(url)
# print(response.text)
# with open("ukr.html", mode='w') as file:
#     file.write(response.text)
# pass

url = "https://tpc.googlesyndication.com/simgad/17106483937998903578?"
response = requests.get(url)
content = response.content

with open("spin.pdf", mode="w") as file:
    file.write(content)
