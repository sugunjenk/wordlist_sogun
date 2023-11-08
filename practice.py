import requests

api_key = '031950b6-43d8-4596-9cb8-5038837fd3bd'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions =res.json()

for definition in definitions:
   print(definitions) 