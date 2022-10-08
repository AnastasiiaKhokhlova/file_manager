

import os
import json
import shutil

class Main():
    def __init__(self):
        with open('Setting.json', 'r') as setting_file:
            self.setting=json.load(setting_file)
        self.d = {'Просмотр содержимого текстового файла': self.file_preview__6,
                  'Переименование файла': self.change_filename__10, 
                  'Удаление файлов по имени':self.delete_file__7,
                  'Создание пустых файлов с указанием имени':self.new_empty_file__4, 
                  'Запись текста в файл':self.write_text__5, 
                  'Создание папки':self.new_folder__1, 
                  'Удаление папки по имени':self.delete_folder__2,
                  'Копирование файлов из одной папки в другую':self.copy_file__8,
                  'Перемещение файлов':self.change_file_directory_9, 
                  'Перемещение между папками':self.change_folder__3}
        
    def new_folder__1(self):
        try:
            foldername=input('Введите имя новой папки: ')
            foldername=self.setting['work_folder']+'/'+foldername
            assert foldername
            os.mkdir(foldername)
            print('Папка создана')
        except:
            print('Введено некорректное название')
        
    def delete_folder__2(self):
        try:
            foldername=input('Введите имя папки, которую хотите удалить: ')
            foldername=self.setting['work_folder']+'/'+foldername
            assert foldername
            os.rmdir(foldername)
            print('Папка удалена')
        except:
            print('Такой папки не существует')
        
    def change_folder__3(self):
        try:
            foldername=input('Введите имя папки, в которую хотите зайти: ')
            foldername=self.setting['work_folder']+'/'+foldername
            assert foldername
            os.chdir(foldername)
            print('Вы переместились')
            ans=input('Хотите вернуться назад?')
            if ans=='да':
                os.chdir(self.setting['work_folder'])
            print('Вы переместились')
        except:
            print('Такой папки не существует')
        
    def new_empty_file__4(self):
        try:
            filename=input('Введите имя нового файла: ')
            filename=self.setting['work_folder']+'/'+filename
            assert filename
            file=open(filename, "w")
            print('Пустой файл создан')
            file.close()
        except:
            print('Некорректное имя файла')
        
    def write_text__5(self):
        try:
            filename=input('Введите имя файла: ')
            filename=self.setting['work_folder']+'/'+filename
            assert filename
            text=input('Введите текст: ')
            with open(filename, 'w+') as file:
                file.write(text)
            print('Текст записан')
        except:
            print('Такого файла не существует')
    
    def file_preview__6(self):
        try:
            filename=input('Введите имя файла: ')
            filename=self.setting['work_folder']+'/'+filename
            assert filename
            with open(filename, 'r') as file:
                content='\n'.join([row for row in file.readlines()])
                print(content)
            print('Файл прочитан')
        except:
            print('Такого файла не существует')
            
            
    def delete_file__7(self):
        try:
            filename=input('Введите имя файла: ')
            filename=self.setting['work_folder']+'/'+filename
            assert filename
            os.remove(filename)
            print('Файл удален')
        except:
            print('Такого файла не существует') 
        
    def copy_file__8(self):
        try:
            filename=input('Введите имя файла, который хотите скопировать: ')
            filename=self.setting['work_folder']+'/'+filename
            foldername=input('Введите папки, в которую хотите скопировать файл: ')
            foldername=self.setting['work_folder']+'/'+foldername
            assert filename, foldername
            shutil.copy(filename, foldername)
            print('Файл скопирован')
        except:
            print('Проверьте, что файл и папка существуют, а их названия записаны корректно')
        
    def change_file_directory_9(self):
        try:
            filename=input('Введите имя файла, который хотите переместить: ')
            filename=self.setting['work_folder']+'/'+filename
            foldername=input('Введите папки, в которую хотите переместить файл: ')
            foldername=self.setting['work_folder']+'/'+foldername
            assert filename, foldername
            shutil.move(filename, foldername)
            print('Файл перемещен')
        except:
            print('Проверьте, что файл и папка существуют, а их названия записаны корректно')
    
    def change_filename__10(self):
        try:
            old_name=input('Введите имя файла, который хотите изменить: ')
            old_name=self.setting['work_folder']+'/'+old_name
            new_name=input('Введите новое имя файла ')
            new_name=self.setting['work_folder']+'/'+new_name
            assert old_name, new_name
            os.rename(old_name, new_name)
            print('Файл переименован')
        except:
            print('Проверьте корректность написания имен')
        
    def rtrn(self, x):
        return self.d[x]()
    
def call():
    command=input('Введите команду из предложенных без номера и других дополнительных символов:\n    1. Создание папки;\n    2. Удаление папки по имени;\n    3. Перемещение между папками;\n    4. Создание пустых файлов с указанием имени;\n    5. Запись текста в файл;\n    6. Просмотр содержимого текстового файла;\n    7. Удаление файлов по имени;\n    8. Копирование файлов из одной папки в другую;\n    9. Перемещение файлов;\n    10. Переименование файлов\n    Дополнения:\n    Имена файлов вводите с расширением\n')
    Main().rtrn(command)
call()




