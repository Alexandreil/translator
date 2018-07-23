from tkinter import *

#Создаем словарь
word = {'\n':'\n',  'q' : 'й' , 'w' : 'ц' , 'e' : 'у' , 'r' : 'к' , 't' : 'е' , 'y' : 'н' , 'u' : 'г' , 'i' : 'ш' , 'o' : 'щ' , 'p' : 'з' , '[' : 'х' , ']' : 'ъ' , 'a' : 'ф' , 's' : 'ы' , 'd' : 'в' , 'f' : 'а' , 'g' : 'п' , 'h' : 'р' , 'j' : 'о' , 'k' : 'л' , 'l' : 'д' , ';' : 'ж' , "'" : 'э', 'z' : 'я' , 'x' : 'ч' , 'c' : 'с' , 'v' : 'м' , 'b' : 'и' , 'n' : 'т' , 'm' : 'ь' , ',' : 'б' , '.' : 'ю', '/' : '.', '?' : ',' , '`' : 'ё' , " " : " " , " !" : " !" }
trans = {'\n':'\n','й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', '.': '/', ',': '?', 'ё': '`'}

def start_click():
	#Удаляем ненужное
	B.destroy()
	canvas.destroy()
	label2.destroy()
	#Создаем вторую страницу
	canvas1.pack()
	#Размешаем поля
	text1.place(x = 25, y = 70)
	text2.place(x = 515, y = 70)
	#Прокрутка
	scroll_1.place(x = 390, y = 70, height = 150)
	scroll_2.place(x = 880, y = 70, height = 150)
	label1.place(x=10,y=10)
#Переносим на другое поле
def getText(event):
	global text
	text = text1.get(1.0, END)
	text2.delete(1.0, END)
	translater()
	text2.insert(1.0, text)

def translater():
	global text, i
	_id_ = 0
	i = len(text) #Записываем количество символов
	lis = []#Создаем пустой список 
	
	while i != 0:  #Чиним текст
		count = text[_id_]

		if count in ( '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0' , '-' , '_' , '(' , ')', '=' , '+' , '*' , '\\' , '!' , '@' , '#' , '$' , '%' , '^' , '&' , '"' , '№'  , ':'  , '{' , '}' , ' '):#Ищем исключения
			lis.append(count)
			_id_ +=1
			i-=1
		
		elif (count == count.upper()) and (count not in ('[' , ']' , ';' , "'" , ',' , '.' , ' ' , '?' , '/')):#Ищем большие буквы
			count = word[count.lower()]
			lis.append(count.upper())
			_id_ +=1
			i-=1
		
		else:#Остольное 
			count = word[count]
			lis.append(count)
			_id_ +=1
			i-=1

	text = ''.join(lis)
root=Tk()

root.title("Переводчик") #Название проекта

canvas = Canvas(root, width = 300, height = 350, bg = "#C2C2C2")#Создаем первую страницу
canvas.pack()
#Вступительный текст и конечный
text = "Здравствуйте! Вы открыли\nпрограмму для перевода\nс ломанного английского\nна русский и наоборот. Надеюсь,\n что она вам понравиться. Если\nбудут какие-то неполадки, то про-\nшу обратиться в службу\nтехподдержки. Теперь нажмите\n на кнопку 'Пропустить'."
label2 = Label(text=text, justify=CENTER, font = ("Times New Roman", "14"), bg = "#C2C2C2")
label2.place(x = 10, y = 10)

B = Button(root, text = "Пропустить", width = 9, height = 1,bg = "#C2C2C2", command = start_click)
B.place(x=110, y=320)
	
canvas1 = Canvas(root, width = 900, height = 400, bg = "#FFFFFF")
#Поля ввода для перевода 
text1=Text(canvas1, width = 40, height = 8, font = ("Times New Roman", "14"), wrap = WORD)
text2=Text(canvas1, width = 40, height = 8, font = ("Times New Roman", "14"), wrap = WORD)

scroll_1 = Scrollbar(canvas1, orient="vertical", command=text1.yview)
scroll_2 = Scrollbar(canvas1, orient="vertical", command=text2.yview) 

text1.configure(yscrollcommand=scroll_1.set)
text2.configure(yscrollcommand=scroll_2.set)

label1 = Label(canvas1, text="NeighborПереводчик", fg="black",  font = ("Times New Roman", "20"), bg = "#FFFFFF")

root.bind("<Key>", getText)

root.mainloop()
