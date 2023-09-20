import tkinter as tk
from tkinter import ttk

from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

langaueg_data = lt.languages()
langaueg_names =[lang['name'] for lang in langaueg_data]
langaueg_codes = {lang['name']: lang['code']for lang in langaueg_data}
print(langaueg_codes)
# print(langaueg_names)



# print(langaueg_data)

app = tk.Tk()
app.geometry('700x400')
app.title('translation')
app.config(bg='white')
app_name = tk.Label(app, text='motargm', font='arial 15 bold',bg= 'white')
app_name.place(x= 270, y= 10 )

# input details

input_label = tk.Label(app, text='Enter Text', font='arial 13 bold',bg= 'white')
input_label.place(x= 85, y= 45)

input_text = tk.Text(app, font= 'arial 10', height=11 , width=30)
input_text.place(x=15, y=100)

input_lang = ttk.Combobox(app, width=19, values=langaueg_names)
input_lang.place(x=55 ,y=75)
input_lang.set('choose input language')
# -----------------------------------------------------------

# output details

output_label = tk.Label(app, text='output', font='arial 13 bold',bg= 'white')
output_label.place(x= 490, y= 45)

output_text = tk.Text(app, font= 'arial 10', height=11 , width=30)
output_text.place(x=400, y=100)

output_lang = ttk.Combobox(app, width=19, values=langaueg_names)
output_lang.place(x=440 ,y=75)
output_lang.set('choose output language')
# -----------------------------------------------------------

# translate button

def translate():
  translated_text = lt.translate(input_text.get('1.0',tk.END),langaueg_codes[input_lang.get()] ,langaueg_codes[output_lang.get()] )
  output_text.insert('1.0',translated_text)
# ------------------------------------------------------
# clear button

def Clear():
  output_text.delete('1.0',tk.END)
  input_text.delete('1.0',tk.END)


clear_btn = tk.Button(app, text='clear', font='arial 10 bold',padx=5, width=8, command=Clear)
clear_btn.place(x=305, y=220)
# ------------------------------------------------------



trans_btn = tk.Button(app, text='Translate', font='arial 10 bold',command=translate)
trans_btn.place(x=295.5, y=180)

app.mainloop()



