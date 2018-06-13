import json

# КОММЕНТАРИЙ
# Вроде сделал правильно, но оно не работает, может что-то не понимаю.
# Долго сидел дебажил на pycharm-e, но переменная html сбрасывается в какой-то момент

# Получение json из файла
with open('source.json') as json_file:
	json = json.load(json_file)


# Check типа и добавление тегов списка
def CheckTrigerAndAddTeg(type_is_list, teg):
	if type_is_list:
		return teg
	else:
		return ''
	

# Рекурсия в функции для обхода всех элементов
def iteracions(json, html):
	
	# Проверка на тип list и сохранение тригера
	if type(json) is list:
		type_is_list = 1
	else:
		type_is_list = 0
	
	
	for object in json:
		
		html += CheckTrigerAndAddTeg(type_is_list, '<ul>')
		
		# Если переменная object это список или словарь, то функция вызывает саму себя
		if type(object) is list or type(object) is dict:
			iteracions(object, html)
			
		# Иначе строится переменная html
		else:
			html += CheckTrigerAndAddTeg(type_is_list, '<li>')
			html += '<' + object + '>' + json[object] + '</' + object + '>'
			html += CheckTrigerAndAddTeg(type_is_list, '</li>')

		html += CheckTrigerAndAddTeg(type_is_list, '</ul>')
		type_is_list = 0

	return html
	

def Main(json):
	html = ''
	
	# Проход по всему списку
	html = iteracions(json, html)
	
	return html


html = Main(json)
print(html)
