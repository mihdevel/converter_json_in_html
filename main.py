import json

# КОММЕНТАРИЙ
# Вроде сделал правильно, но оно не работает, может что-то не понимаю.
# Долго сидел дебажил на pycharm-e, но переменная html сбрасывается в какой-то момент

# КОММЕНТАРИЙ №2
# Сделал разделение переменной тега с помощью split,
# но из-за предыдущей загвоздки не задачу доделал не до конца.
# Не стал сильно разбираться - много времени занимает.


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
			
			html_structure = {}
			list_id = []
			list_class = []
			# Если в теге указан индификатор или класс
			if '.' in object or '#' in object:
				
				# Сначала split делаю на точку (.)
				str_split_class = object.split('.')
				
				html_structure['teg'] = str_split_class[0]
				html_structure['content'] = json[object]
				
				# А здесь split делаю на решетку (#)
				for str in str_split_class:
					str_split_id = str.split('#')
					if len(str_split_id) > 1:
						list_id.append(str_split_id[1])
						list_class.append(str_split_id[0])
					else:
						list_class.append(str)
				
				html_structure['id'] = list_id
				html_structure['class'] = list_class
			
			else:
				html_structure['teg'] = object
				html_structure['content'] = json[object]
		
			# Построение имен классов тега
			teg_class = ' class='
			for name_class in html_structure['class']:
				teg_class += name_class + ' '
			
			
			# Построение имен айди тега
			teg_id = ' id='
			for name_id in html_structure['id']:
				teg_id += name_id + ' '
				
			html += '<' + html_structure['teg'] + teg_id + teg_class + '>' + html_structure['content'] + '</' + html_structure['teg'] + '>'
			
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
