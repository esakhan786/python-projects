from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.title("AI Translator")
root.geometry("500x650")
root.configure(bg="#1e3d59")

Label(root,text="AI Translator",font=("Times New Roman",30,"bold"),bg="#1e3d59",fg="white").pack(pady=20)

Label(root,text="Enter Text",font=("Times New Roman",15,"bold"),bg="#1e3d59",fg="white").pack()

sor_txt = Text(root,font=("Times New Roman",16),wrap=WORD,height=5)
sor_txt.pack(pady=10,padx=10)

lang_frame = Frame(root,bg="#1e3d59")
lang_frame.pack(pady=5)

languages = ['english','urdu','arabic','french','german','spanish','hindi','chinese','turkish']

comb_sor = ttk.Combobox(lang_frame,values=languages,width=15)
comb_sor.set("english")
comb_sor.grid(row=0,column=0,padx=10)

comb_dest = ttk.Combobox(lang_frame,values=languages,width=15)
comb_dest.set("urdu")
comb_dest.grid(row=0,column=1,padx=10)

btn = Button(root,text="Translate",font=("Times New Roman",15,"bold"),
             bg="#f5f0e1",command=lambda: translate_now())
btn.pack(pady=15)

Label(root,text="Translated Text",font=("Times New Roman",15,"bold"),bg="#1e3d59",fg="white").pack()

dest_txt = Text(root,font=("Times New Roman",16),wrap=WORD,height=5)
dest_txt.pack(pady=10,padx=10)

def translate_now():
    text = sor_txt.get(1.0, END)
    target = comb_dest.get()

    translated = GoogleTranslator(source='auto', target=target).translate(text)

    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated)

root.mainloop()