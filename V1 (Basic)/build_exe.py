import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from englisttohindi.englisttohindi import EngtoHindi

def eng_to_hindi():
    input_text = input_text_widget.get("1.0", tk.END)
    sentences = input_text.split('.')  # Split text by full stops to get sentences

    translated_sentences = []
    for sentence in sentences:
        if sentence.strip():  # Check if the sentence is not empty
            trans = EngtoHindi(sentence)
            res = trans.convert
            translated_sentences.append(res)

    result_text = '\n'.join(translated_sentences)

    # Replace English full stops with Hindi full stops
    result_text = result_text.replace('.', ' |')

    result_text_widget.delete("1.0", tk.END)
    result_text_widget.insert(tk.END, result_text)

master = tk.Tk()
master.title("English to Hindi Translator")

# Define custom colors
background_color = "#F5F5F5"
label_color = "#333333"
button_color = "#3498db"
result_color = "#27ae60"

# Set background color
master.configure(bg=background_color)

# Create a ScrolledText widget for the input field
input_text_widget = ScrolledText(master, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 12))
input_text_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Create a ScrolledText widget for the result field
result_text_widget = ScrolledText(master, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 12))
result_text_widget.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="w")

b = ttk.Button(master, text="Translate", command=eng_to_hindi, style="Rounded.TButton")
b.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Make the window resizable
master.rowconfigure(0, weight=1)
master.columnconfigure(0, weight=1)

master.mainloop()
