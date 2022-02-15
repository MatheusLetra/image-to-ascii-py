from tkinter import * 
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import pywhatkit



compiler = Tk()
compiler.title('Image to ASCII Converter')
compiler.geometry('400x400')
compiler.resizable(width=False, height=False)

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('PNG Files', '*.png'),('JPG Files', '*.jpg'),('JPEG Files', '*.jpeg')])
    directory_path = askdirectory()
    if path != '':
        set_file_path(path)
        pywhatkit.image_to_ascii_art(path,f'{directory_path}\\Ascii-Image')
        messagebox.showinfo("Sucess", f"The ascii image was saved in the folder {directory_path} ")


menu_bar = Menu(compiler)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Select Image', command=open_file)

menu_bar.add_cascade(label='Options', menu=file_menu)
compiler.config(menu=menu_bar)
compiler.mainloop()