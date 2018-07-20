from tkinter import *

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

#Переносим на другое поле
def getText(event):
	global text1, text2
	t = text1.get(1.0, END)
	text2.delete(1.0, END)
	text2.insert(1.0, t)

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

root.bind("<Key>", getText)

root.mainloop()
