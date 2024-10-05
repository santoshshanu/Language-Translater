from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi
import re

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

# Label for Input
Label(master, text="Enter Text:", bg="light grey", font=("Arial", 12)).grid(row=0, column=0, sticky=W, padx=10, pady=10)

# Text Input Area
text_input = Text(master, width=60, height=10, font=("Arial", 12))
text_input.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

# Scrollbar for Text Input
scrollbar = Scrollbar(master, command=text_input.yview)
scrollbar.grid(row=1, column=3, sticky='ns')
text_input.config(yscrollcommand=scrollbar.set)

# Translate Button
b = Button(master, text="Translate", command=eng_to_hindi, bg="Light Blue", fg='Red', font=("Arial", 12))
b.grid(row=1, column=4, padx=10, pady=10)

# Label for Result
Label(master, text="Result:", bg="light grey", font=("Arial", 12)).grid(row=2, column=0, sticky=W, padx=10, pady=10)

# Translated Output Area
translated_output = Text(master, width=60, height=10, font=("Arial", 12), state="disabled")
translated_output.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

# Scrollbar for Translated Output
output_scrollbar = Scrollbar(master, command=translated_output.yview)
output_scrollbar.grid(row=3, column=3, sticky='ns')
translated_output.config(yscrollcommand=output_scrollbar.set)

# Copy Button
copy_button = Button(master, text="Copy", command=copy_to_clipboard, bg="Light Blue", fg='Red', font=("Arial", 12))
copy_button.grid(row=3, column=4, padx=10, pady=10)

mainloop()
