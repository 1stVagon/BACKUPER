import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from datetime import datetime

def btn_click():
    log_file_path = os.path.join(os.path.dirname('BACKUPER'), "backup-logs.txt")

    try:
        backup_folder = os.path.join(dest_folder.get(),
                            datetime.now().strftime("%a-%d-%m"),
                            f'backup-from-{datetime.now().strftime("%H-%M-%S")}')
        shutil.copytree(src_folder.get(), backup_folder)

        directory = os.path.join(dest_folder.get(), 
                                 datetime.now().strftime("%a-%d-%m"))
        files_count_after_backup_dest = len(os.listdir(directory))
        folders = os.listdir(directory)

        if (files_count_after_backup_dest > 3):
            oldest_folder_path = os.path.join(directory, min(folders))
            shutil.rmtree(oldest_folder_path)
    
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"From Folder: {src_folder.get()}\n")
            log_file.write(f"To Folder: {backup_folder}\n")
            log_file.write(f"Success: Successful\n\n")

    except Exception as err:
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"From Folder: {src_folder.get()}\n")
            log_file.write(f"To Folder: {backup_folder}\n")
            log_file.write(f"Success: Error - {str(err)}\n\n")
            
        
root = Tk()
root.title('Backuper')
root.geometry('350x180')
root.resizable(width=False, height=False)

label = Label(text='from:', foreground='#B71C1C')
label.pack(pady=6)

src_folder = Entry()
src_folder.pack(ipadx=60)

label = Label(text='in:', foreground='#1E90FF')
label.pack(pady=6)

dest_folder = Entry()
dest_folder.pack(ipadx=60)

btn = Button(text='make copy', command=btn_click, bg='Gainsboro')
btn.pack(pady=20)

root.mainloop()
