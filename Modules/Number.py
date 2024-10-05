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
        master.configure(bg='black')
        text_input.configure(bg='White', fg='Black')
        translated_output.configure(bg='White', fg='Black')
        select_button.configure(bg='White', fg='Black')
        translate_button.configure(bg='White', fg='Black')
        copy_button.configure(bg='White', fg='Black')
        mode_button.configure(bg='White', fg='Black')
        current_mode = "dark"
    else:
        master.configure(bg='light grey')
        text_input.configure(bg='white', fg='black')
        translated_output.configure(bg='white', fg='black')
        select_button.configure(bg='Black', fg='White')
        translate_button.configure(bg='Black', fg='White')
        copy_button.configure(bg='Black', fg='White')
        mode_button.configure(bg='Black', fg='White')
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
master.configure(bg='light grey')

Label(master, text="Enter a Number:", bg="White", font=("Arial", 12)).grid(row=0, column=0, sticky=W, padx=10, pady=10)

select_button = Button(master, text="Select File", command=select_file, bg="Black", fg='White', font=("Arial", 12))
select_button.grid(row=0, column=1, padx=10, pady=10)

text_input = Text(master, width=60, height=10, font=("Arial", 12))
text_input.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

scrollbar = Scrollbar(master, command=text_input.yview)
scrollbar.grid(row=1, column=3, sticky='ns')
text_input.config(yscrollcommand=scrollbar.set)

translate_button = Button(master, text="Translate", command=translate_number_to_hindi, bg="Black", fg='White', font=("Arial", 12))
translate_button.grid(row=1, column=4, padx=10, pady=10)

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
