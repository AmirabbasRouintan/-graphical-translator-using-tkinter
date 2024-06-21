import tkinter as tk
from PIL import Image, ImageTk
import requests
import tkinter.messagebox

root = tk.Tk()
root.title("ixi_flower : translater")
root.geometry("500x800")

image_file = "back.png"
image = Image.open(image_file)
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(root, bg="black", image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

text_area = tk.Text(root, width=31, height=2) 
text_area.configure(font=('Vazirmatn', 17), wrap=None)
text_area.place(x=30, y=150)

def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()

    if not data:
        return "No data found for the word '{}'."

    word_data = data[0]
    word_meaning = ""

    word_meaning += f"Word: {word_data['word']}\n"
    word_meaning += "Phonetic Transcriptions:\n"
    for phonetic in word_data['phonetics']:
        if 'text' in phonetic:
            word_meaning += f"- {phonetic['text']}\n"

    word_meaning += "\nMeanings:\n"
    for meaning in word_data['meanings']:
        word_meaning += f"- {meaning['partOfSpeech']}\n"
        for definition in meaning['definitions']:
            word_meaning += f"  Definition: {definition['definition']}\n"

    return word_meaning

search_button = tk.Button(root, text="Search", command=lambda: search_word(text_area.get("1.0", "end-1c")))
search_button.place(x=380, y=165)

def search_word(word):
    meaning = get_word_meaning(word)
    
    if meaning == "No data found for the word '{}'.":
        tkinter.messagebox.showerror("Error", f"The word '{word}' is not correct.")
    else:
        new_window = tk.Toplevel()
        new_label = tk.Label(new_window, text=meaning, font=('Vazirmatn', 12), bg='#0D0C0C', fg='#FFFFFF')
        new_label.pack(pady=(5,10), padx=(10,10))
        new_window.title("Meaning")

root.mainloop()