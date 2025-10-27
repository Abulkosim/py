from urllib.request import urlopen
import json 
with urlopen('https://jsonplaceholder.typicode.com/todos/1') as response:
  res = json.load(response)
  print(res)