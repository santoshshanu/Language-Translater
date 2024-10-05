from tkinter import *
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract
from englisttohindi.englisttohindi import EngtoHindi
import re
import inflect

p = inflect.engine()
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

current_mode = "light"

def toggle_mode():
    global current_mode
    if current_mode == "light":
        master.configure(bg='#121212')
        text_input.configure(bg='white', fg='black')
        translated_output.configure(bg='white', fg='black')
        select_button.configure(bg='#6200EA', fg='white', activebackground='#BB86FC')
        translate_button.configure(bg='#6200EA', fg='white', activebackground='#BB86FC')
        copy_button.configure(bg='#6200EA', fg='white', activebackground='#BB86FC')
        mode_button.configure(bg='#6200EA', fg='white', activebackground='#BB86FC')
        current_mode = "dark"

    else:
        master.configure(bg='white')
        text_input.configure(bg='white', fg='black')
        translated_output.configure(bg='white', fg='black')
        select_button.configure(bg='#BB86FC', fg='black', activebackground='#6200EA')
        translate_button.configure(bg='#BB86FC', fg='black', activebackground='#6200EA')
        copy_button.configure(bg='#BB86FC', fg='black', activebackground='#6200EA')
        mode_button.configure(bg='#BB86FC', fg='black', activebackground='#6200EA')
        current_mode = "light"

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.tif")])
    if file_path:
        extract_text(file_path)

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    text_input.delete("1.0", END)
    text_input.insert(END, text)

def convert_number_to_english(number):
    """Converts a number to its English text representation."""
    return p.number_to_words(number)

def translate_number_to_hindi():
    input_number = text_input.get("1.0", END).strip()
    english_text = convert_number_to_english(input_number)
    translated_text = EngtoHindi(english_text).convert

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
master.title("Number to Hindi Translator")
master.geometry("800x600") 
master.configure(bg='white') 

title_font = ("Arial", 20, "bold")
button_font = ("Arial", 12)

title_label = Label(master, text="Number to Hindi Translator", font=title_font, bg='white')
title_label.pack(pady=20)

frame = Frame(master, bg='white')
frame.pack()

Label(frame, text="Enter a Number:", font=("Arial", 12), bg='white').grid(row=0, column=0, padx=10, pady=10)
text_input = Text(frame, width=60, height=10, font=("Arial", 12))
text_input.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

input_scrollbar = Scrollbar(frame, command=text_input.yview)
input_scrollbar.grid(row=1, column=3, sticky='ns')
text_input.config(yscrollcommand=input_scrollbar.set)

select_button = Button(frame, text="Select File", command=select_file, font=button_font, bg='#6200EA', fg='white', activebackground='#BB86FC')
select_button.grid(row=2, column=0, padx=10, pady=10)
translate_button = Button(frame, text="Translate", command=translate_number_to_hindi, font=button_font, bg='#6200EA', fg='white', activebackground='#BB86FC')
translate_button.grid(row=2, column=1, padx=10, pady=10)
copy_button = Button(frame, text="Copy", command=copy_to_clipboard, font=button_font, bg='#6200EA', fg='white', activebackground='#BB86FC')
copy_button.grid(row=2, column=2, padx=10, pady=10)
mode_button = Button(frame, text="Dark Mode", command=toggle_mode, font=("Arial", 10), bg='#6200EA', fg='white', activebackground='#BB86FC')
mode_button.grid(row=0, column=2, padx=10, pady=10)

result_frame = Frame(master, bg='white')
result_frame.pack()

Label(result_frame, text="Result in Hindi:", font=("Arial", 12), bg='white').grid(row=0, column=0, padx=10, pady=10)
translated_output = Text(result_frame, width=60, height=10, font=("Arial", 12), state="disabled")
translated_output.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

output_scrollbar = Scrollbar(result_frame, command=translated_output.yview)
output_scrollbar.grid(row=1, column=3, sticky='ns')
translated_output.config(yscrollcommand=output_scrollbar.set)

mainloop()