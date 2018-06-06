import json

# Получение json из файла
with open('source.json') as json_file:
	json = json.load(json_file)



def Main(json):
	html = ''
	for list in json:
		html += '<h1>' + list['title'] + '</h1><p>' + list['body'] + '</p>'

	return html


Main(json)