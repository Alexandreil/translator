from tkinter import *

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
	t = text1.get(1.0, END)
	text2.delete(1.0, END)
	text2.insert(1.0, t)

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
