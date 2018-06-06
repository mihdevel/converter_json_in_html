import json

# Получение json из файла
with open('source.json') as json_file:
	json = json.load(json_file)


# Здесь получается, что ключи (теги) могут меняться местами,
# а нам это как я понимаю не нужно,
# поэтому можно либо сортировать ключи так как нам надо,
# либо, придумать друой подхход получения ключей, который я пока не придумал,
# кстати, на этот порядок тегов я написал тест.

def Main(json):
	html = ''
	
	for section in json:
		for key in section:
			html += '<'+key+'>' + section[key] + '</'+key+'>'
			

	return html


html = Main(json)
print(html)