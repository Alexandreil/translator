from tkinter import *

#Создаем словарь
word = {'q' : 'й' , 'w' : 'ц' , 'e' : 'у' , 'r' : 'к' , 't' : 'е' , 'y' : 'н' , 'u' : 'г' , 'i' : 'ш' , 'o' : 'щ' , 'p' : 'з' , '[' : 'х' , ']' : 'ъ' , 'a' : 'ф' , 's' : 'ы' , 'd' : 'в' , 'f' : 'а' , 'g' : 'п' , 'h' : 'р' , 'j' : 'о' , 'k' : 'л' , 'l' : 'д' , ';' : 'ж' , "'" : 'э', 'z' : 'я' , 'x' : 'ч' , 'c' : 'с' , 'v' : 'м' , 'b' : 'и' , 'n' : 'т' , 'm' : 'ь' , ',' : 'б' , '.' : 'ю', '/' : '.', '?' : ',' , '`' : 'ё'}
trans = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', '.': '/', ',': '?', 'ё': '`'}

_id_ = 0

def start_click():
	global canvas, text
	#Удаляем ненужное
	B.destroy()
	canvas.destroy()
	#Создаем вторую страницу
	canvas1.pack()
	#Размешаем поля
	text1.place(x = 25, y = 45)
	text2.place(x = 415, y = 45)
	b_get.place(x = 50, y = 300)
#Функция счёта
def schet():
	global _id_, i
	_id_ +=1
	i-=1
#Переносим на другое поле
def getText():
	global i, text, text1, _id_, lis, word, count
	lis = []#Создаем пустой список 
	text = text1.get(1.0, END)

	text = list(text)
	
	i = len(text) #Записываем количество символов
	
	while i != 0:  #Чиним текст
	
		count = text[_id_]
	
		if text[_id_] in ( '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0' , '-' , '_' , '(' , ')', '=' , '+' , '*' , '\\' , '!' , '@' , '#' , '$' , '%' , '^' , '&' , '"' , '№'  , ':'  , '{' , '}' , ' '):#Ищем исключения
			lis.append(count)
			schet()
		
		elif (count == count.upper()) and (count not in ('[' , ']' , ';' , "'" , ',' , '.' , '' , '?' , '/')):#Ищем большие буквы
			count = word[count.lower()]
			lis.append(count.upper())
			schet()
		
		else:#Остольное 
			count = word[count]
			lis.append(count)
			schet()
	text = ''.join(lis)
	text2.insert(1.0, text)

root=Tk()

root.title("Переводчик") #Название проекта

canvas = Canvas(root, width = 300, height = 350, bg = "#FEFEF5")#Создаем первую страницу
canvas.pack()

#Вступительный текст и конечный
text = '''  Здравствуйте! Вы открыли 
программу для перевода 
с ломанного английского 
на русский и наоборот. Надеюсь, 
что она вам понравиться. Если 
будут какие-то неполадки, то про-
шу обратиться в службу
техподдержки. Теперь нажмите 
на кнопку "Пропустить". '''
canvas.create_text(155, 115, text = text, fill = "black", font =("Harrington", "13"))

B = Button(root, text = "Пропустить", width = 9, height = 1, bg = "#F9F7D4", command = start_click)
B.place(x=110, y=320)
	
canvas1 = Canvas(root, width = 800, height = 400, bg = "#FEFEF5")

#Поля ввода для перевода 
text1=Text(root, width = 40, height = 8, font = ("Harrington", "12"), wrap = WORD)
text2=Text(root, width = 40, height = 8, font = ("Harrington", "12"), wrap = WORD)

#Кнопка перевода
b_get = Button(root, text="Перевести", command=getText)

root.mainloop()