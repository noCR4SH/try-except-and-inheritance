import json

data = [
    ['door', 3, 7, 0],
    ['sand', 12, 5, 1],
    ['brush', 22, 34, 5],
    ['poster', 'red', 8, 'stick']
]

# Writting JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file)
