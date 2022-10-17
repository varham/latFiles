import shutil
import zipfile

import win32api
import os
import json
from zipfile import ZipFile

def sys_info():
    total, used, free = shutil.disk_usage("/")
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print("[+] Имена логических дисков - " + str(drives))
    print("[+] Всего : %d Gb" % (total // (2**30)))
    print("[+] Используется : %d Gb" % (used // (2**30)))
    print("[+] Свободно : %d Gb" % (free // (2**30)))
    input("[*] Нажмите кнопку для продолжения")

def work_with_files():
    print("[*] Выберите нужный пункт ")
    print("[1] Создать файл")
    print("[2] Записать строку в файл")
    print("[3] Прочитать файл")
    print("[4] Удалить файл")
    print("[5] Выйти")
    usr_input = int(input("-> "))
    if usr_input == 1:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".txt"
        if not os.path.exists(file_name):
            with open(file_name, 'w'): pass
            input("[*] Файл создан. Нажмите кнопку для продолжения.")
            work_with_files()
    elif usr_input == 2:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        usr_string = input("[*] Введите строку")
        file_name = file_name + ".txt"
        if os.path.exists(file_name):
            f = open(file_name, 'w')
            f.write(usr_string)
            f.close()
            input("[*] Строка записана. Нажмите кнопку для продолжения.")
            work_with_files()
        else:
            input("[!] Такого файла нет!")
            work_with_files()
    elif usr_input == 3:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".txt"
        if os.path.exists(file_name):
            with open(file_name) as f:
                lines = f.readlines()
                print(lines)
                input("[*] Файл прочитан. Нажмите кнопку для продолжения.")
                work_with_files()
        else:
            input("[!] Такого файла нет!")
            work_with_files()
    elif usr_input == 4:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            input("[*] Файл удален. Нажмите кнопку для продолжения.")
            work_with_files()
        else:
            input("[!] Такого файла нет!")
            work_with_files()
    else:
        pass

def work_with_json():
    print("[*] Выберите нужный пункт ")
    print("[1] Создать JSON на основе")
    print("[2] Создать объект")
    print("[3] Прочитать JSON")
    print("[4] Удалить JSON")
    print("[5] Выйти")
    usr_input = int(input("-> "))
    if usr_input == 1:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".json"
        base_file = input("[*] Введите имя файла базы (без разрешения) ")
        base_file = base_file + ".json"
        with open(base_file) as f:
            data = json.load(f)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)
            input("[*] Создан новый файл на основе " + str(base_file))
            work_with_json()
    elif usr_input == 2:
        color = input("[*] Введите цвет ")
        value = input("[*] Введите значение")
        data = {"color": color, "value": value}
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".json"
        with open(file_name, 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            work_with_json()
    elif usr_input == 3:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".json"
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data = json.load(f)
                print(data)
                input("[*] Файл прочитан ")
                work_with_json()
        else:
            input("[*] Такого файла не существует")
            work_with_json()
    elif usr_input == 4:
        file_name = input("[*] Введите имя файла (без разрешения) ")
        file_name = file_name + ".json"
        if os.path.exists(file_name):
            os.remove(file_name)
            input("[*] Файл удален. Нажмите кнопку для продолжения.")
            work_with_json()
        else:
            input("[!] Такого файла нет!")
            work_with_json()
    else:
        pass

def work_with_rar():
    print("[*] Выберите нужный пункт ")
    print("[1] Создать zip архив")
    print("[2] Разархивировать файл")
    print("[3] Удалить файл и архив")
    print("[4] Выйти")
    usr_input = int(input("-> "))
    if usr_input == 1:
        zip_file_name = input("[*] Введите имя архива (без разрешения) ")
        zip_file_name = zip_file_name + ".zip"
        file_name = input("[*] Введите имя файла (с разрешением) ")
        try:
            zipfile.ZipFile(zip_file_name, mode='w').write(file_name)
            input("[*] Файл разархивирован!")
            work_with_rar()
        except:
            work_with_rar()
            pass
    elif usr_input == 2:
        zip_file_name = input("[*] Введите имя архива (без разрешения) ")
        zip_file_name = zip_file_name + ".zip"
        if os.path.exists(zip_file_name):
            with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
                zip_ref.extractall()
            input("[*] Архив разархивирован!")
            work_with_rar()
        else:
            input("[*] Такого архива нет!")
            work_with_rar()
    elif usr_input == 3:
        zip_file_name = input("[*] Введите имя архива (без разрешения) ")
        zip_file_name = zip_file_name + ".zip"
        if os.path.exists(zip_file_name):
            os.remove(zip_file_name)
            input("[*] Архив удален!")
            work_with_rar()
        else:
            input("[*] Такого архива нет!")
            work_with_rar()
    else:
        pass





def main():
    while True:
        print("[*] Работа с файлами. Выберите необходимый пункт")
        print("[1] Вывести информацию о системе")
        print("[2] Работа с файлами")
        print("[3] Работа с JSON")
        print("[5] Работа с архивами")
        print("[0] Выйти")
        usr_input = int(input("-> "))
        if (usr_input == 1):
            sys_info()
        elif (usr_input == 2):
            work_with_files()
        elif (usr_input == 3):
            work_with_json()
        elif (usr_input == 5):
            work_with_rar()
        elif (usr_input == 0):
            break

if __name__ == "__main__":
    main()

