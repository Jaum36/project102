import os
import shutil

front_dir = 'C:/Users/João Victor/Downloads'
to_dir = 'C:/Users/João Victor/Desktop/mandar imagens'

list_of_files = os.listdir(front_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg']:
        path1 = front_dir + '/' + file_name
        path2 = to_dir + '/' + 'Arquivo_Imagem'
        path3 = to_dir + '/' + 'Arquivo_Imagem' + '/' + file_name

        if os.path.exists(path2):
            print("Movendo" + file_name + "...")

            shutil.move(path1, path2)
        else:
            os.makedirs(path2)
            print("Movendo" + file_name + "...")
            shutil.move(path1, path3)
    
    if extension in ['.pdf']:
        path1 = front_dir + '/' + file_name
        path2 = to_dir + '/' + 'Arquivo_Documentos'
        path3 = to_dir + '/' + 'Arquivo_Documentos' + '/' + file_name

        if os.path.exists(path2):
            print("Movendo" + file_name + "...")

            shutil.move(path1, path2)
        else:
            os.makedirs(path2)
            print("Movendo" + file_name + "...")
            shutil.move(path1, path3)