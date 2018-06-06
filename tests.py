import json
from main import html

# Получение json из файла
with open('source.json') as json_file:
  json = json.load(json_file)

def TestOrderTegsHtml(html, json):

  for key in json[0]:
    
    try:
      html[:3].index(key)
      print('Test Ok')
    except ValueError:
      print('Test Error')
    
    break
  
TestOrderTegsHtml(html, json)