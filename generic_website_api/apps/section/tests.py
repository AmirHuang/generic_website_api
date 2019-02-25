
data = {'title': '中华人民f'}

for i in data['title'].split():
    print(i)

name = ''.join([i.capitalize() for i in data['title'].split()])
print(name)