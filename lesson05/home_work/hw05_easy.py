# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def dir_creator(dirName, q):  # dirName - название директории, q - необходимое количество папок
    import os
    dir_path = ""
    for i in range(1, q + 1):
        dir_path +=dirName + str(i) + "/"
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        print('Такая директория уже сущетвует')
    print("Готово!")
    return dir_path

dir_creator("dir_", 9) #вызов функции


def dir_kill(rem_dir):
    import os
    os.removedirs(rem_dir)
#можем воспользоваться им
#m_test.dir_kill(dir_path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dirList(dir):
    import os

    dir = os.listdir()
    dir_list = [i for i in dir if os.path.isdir(i)]
    n = 1
    print("Содержимое папки:\n\nПапки:\n")
    for _ in dir_list:
        print('{}. {}'.format(n, _))
        n += 1
    dir_files = [i for i in dir if not os.path.isdir(i)]
    n = 1
    print("\nФайлы:\n")
    for _ in dir_files:
        print('{}. {}'.format(n, _))
        n += 1

    return

# надеюсь, я правильно понял условие

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.




def file_copy ():
    import shutil
    import os
    name_file = os.path.realpath(__file__)
    new_file = name_file[:-2] +'copy.py'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'


print(file_copy())

#долго пытался найти, как сделать копию не просто изменением названия
#потом наткнулся на это решение. Доработал его так, чтобы копия файла
#была в формате .py и соответственно открывалась