import os
import shutil

from_dir = "C://Users//djvil//OneDrive//Documents//Prueba"
to_dir = "C://Users//djvil//OneDrive//Desktop//proyectos//Archivos_Documentos"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    ext = os.path.splitext(file)

    if len(ext[1]) == 0 :
        continue
    else:
        print(ext[1])
        if ext[1] in ['.txt', '.doc', '.docx', '.pdf']:
            ruta1 = from_dir+'//' + file
            ruta2 =  to_dir
            ruta3 = to_dir + '//' + file

            if os.path.exists(ruta2):
                print("Moving " + file + ".....")

                shutil.move(ruta1, ruta3) 

            else:
                os.makedirs(ruta2)
                print("Moving " + ext[0] + ".....")
                shutil.move(ruta1, ruta3)  