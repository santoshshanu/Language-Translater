from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi
import re

current_mode = "light"

def toggle_mode():
    global current_mode
    if current_mode == "light":
        master.configure(bg='black')
        text_input.configure(bg='White', fg='Black')
        translated_output.configure(bg='White', fg='Black')
        b.configure(bg='White', fg='Black')
        copy_button.configure(bg='White', fg='Black')
        mode_button.configure(bg='White', fg='Black')
        current_mode = "dark"
    else:
        master.configure(bg='light grey')
        text_input.configure(bg='white', fg='black')
        translated_output.configure(bg='white', fg='black')
        b.configure(bg='Black', fg='White')
        copy_button.configure(bg='Black', fg='White')
        mode_button.configure(bg='Black', fg='White')
        current_mode = "light"

def eng_to_hindi():
    input_text = text_input.get("1.0", END)
    sentences = re.split(r'[.!\n]', input_text)
    translated_sentences = []

    for sentence in sentences:
        if sentence.strip():  
            trans = EngtoHindi(sentence)
            translated_sentence = trans.convert
            translated_sentences.append(translated_sentence)
            translated_sentences.append("|")

    translated_text = ' '.join(translated_sentences)
    translated_output.config(state="normal")
    translated_output.delete("1.0", END)
    translated_output.insert(END, translated_text)
    translated_output.config(state="disabled")

def copy_to_clipboard():
    translated_text = translated_output.get("1.0", END)
    master.clipboard_clear()
    master.clipboard_append(translated_text)
    master.update()

master = Tk()
master.title("English to Hindi Translator")
master.configure(bg='light grey')

Label(master, text="Enter Text in English:", bg="White", font=("Arial", 12)).grid(row=0, column=0, sticky=W, padx=10, pady=10)

text_input = Text(master, width=60, height=10, font=("Arial", 12))
text_input.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

scrollbar = Scrollbar(master, command=text_input.yview)
scrollbar.grid(row=1, column=3, sticky='ns')
text_input.config(yscrollcommand=scrollbar.set)

b = Button(master, text="Translate", command=eng_to_hindi, bg="Black", fg='White', font=("Arial", 12))
b.grid(row=1, column=4, padx=10, pady=10)

Label(master, text="Result in Hindi:", bg="White", font=("Arial", 12)).grid(row=2, column=0, sticky=W, padx=10, pady=10)

translated_output = Text(master, width=60, height=10, font=("Arial", 12), state="disabled")
translated_output.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

output_scrollbar = Scrollbar(master, command=translated_output.yview)
output_scrollbar.grid(row=3, column=3, sticky='ns')
translated_output.config(yscrollcommand=output_scrollbar.set)

copy_button = Button(master, text="Copy", command=copy_to_clipboard, bg="Black", fg='White', font=("Arial", 12))
copy_button.grid(row=3, column=4, padx=10, pady=10)

mode_button = Button(master, text="Dark Mode", command=toggle_mode, bg="Black", fg='White', font=("Arial", 10))
mode_button.grid(row=0, column=4, padx=10, pady=10, sticky=E)

mainloop()
