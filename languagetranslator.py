
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('C:\\Users\\91998\\python\\project1\\icon (1).ico')
# img = PhotoImage(file='C:\\Users\\91998\\python\\project1\\icon-16.png')
# root.tk.call('wm', 'iconphoto', root._w, img)
root['bg'] = 'skyblue'

root.title('Demo Language Translator')
Label(root, text='Language Trsnslator', font= 'Arial 20 bold').pack()

Label(root,text= 'Enter Text', font= 'TimesNewRoman 13 bold', bg='white').place(x = 165, y = 90)

Input_text = Entry(root, width=60 )
Input_text.place(x=30, y=130)
Input_text.get()

Label(root,text='Output', font='TimesNewRoman 13 bold', bg = 'white').place(x=750, y=90)
Output_text = Text(root, font='TimesNewRoman 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y = 130)

language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x= 130, y=180)
dest_lang.set('choose language')

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text='Translate', font='TimesNewRoman 12 bold', pady=5, command=Translate, bg='pink', activebackground='green' )
trans_btn.place(x=445, y=180)

root.mainloop()

