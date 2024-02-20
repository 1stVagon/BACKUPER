import os
import shutil
from datetime import datetime

def backup_file(src_folder, dest_folder):
    log_file_path = os.path.join(os.path.dirname('BACKUPER'), "backup-logs.txt")

    try:
        backup_folder = os.path.join(dest_folder,
                            datetime.now().strftime("%a-%d-%m"),
                            f'backup-from-{datetime.now().strftime("%H-%M-%S")}')
        shutil.copytree(src_folder, backup_folder)

        directory = os.path.join(dest_folder, 
                                 datetime.now().strftime("%a-%d-%m"))
        files_count_after_backup_dest = len(os.listdir(directory))
        folders = os.listdir(directory)

        if (files_count_after_backup_dest > 3):
            oldest_folder_path = os.path.join(directory, min(folders))
            shutil.rmtree(oldest_folder_path)
    
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"Из папки: {src_folder}\n")
            log_file.write(f"В папку: {backup_folder}\n")
            log_file.write(f"Успешность: Успешно\n\n")

    except Exception as err:
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"Из папки: {src_folder}\n")
            log_file.write(f"В папку: {backup_folder}\n")
            log_file.write(f"Успешность: Ошибка - {str(err)}\n\n")
    
    print('==конец бэкапа==')

src_folder = input("Введите путь к исходной папке для бэкапа: ")
dest_folder = input("Введите путь к папке для сохранения бэкапа: ")
backup_file(src_folder, dest_folder) 
