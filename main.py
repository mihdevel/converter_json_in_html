import json

# Получение json из файла
with open('source.json') as json_file:
	json = json.load(json_file)

# Check типа и добавление тегов списка
def CheckTrigerAndAddTeg(type_is_list, teg):
	if type_is_list:
		return teg
	else:
		return ''


def Main(json):
	html = ''
	
	# Проверка на тип list и сохранение тригера
	if type(json) is list:
		type_is_list = 1
	else:
		type_is_list = 0
	
	
	html += CheckTrigerAndAddTeg(type_is_list, '<ul>')
	
	# Проход по всему списку
	for section in json:
		
		html += CheckTrigerAndAddTeg(type_is_list, '<li>')
		
		for key in section:
			html += '<'+key+'>' + section[key] + '</'+key+'>'
		
		html += CheckTrigerAndAddTeg(type_is_list, '</li>')
	
	
	html += CheckTrigerAndAddTeg(type_is_list, '</ul>')


	return html


html = Main(json)
print(html)