def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_ru = {1: 'АВЕИНОРСТ',
       2: 'ДКЛМПУ',
       3: 'БГЁЬЯ',
       4: 'ЙЫ',
       5: 'ЖЗХЦЧ',
       8: 'ШЭЮ',
       10: 'ФЩЪ'}
text = input().upper()
print(sum([k for i in text for k, v in points_ru.items() if i in v]))
