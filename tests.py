import json
from main import html

# Получение json из файла
with open('source.json') as json_file:
  json = json.load(json_file)


def TestOrderTegsHtml(html, json):
  """
  При правильной последовательности тегов выводит 'Test Ok'
  При не правильной последовательности тегов выводит 'Test Error'
  """
  for key in json[0]:
    
    try:
      html[:11].index(key)
      print('Test Ok')
    except ValueError:
      print('Test Error')
    
    break
  
TestOrderTegsHtml(html, json)