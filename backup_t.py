#!/usr/bin/python3
import os

BACKUP_DIRECTORY = '/mnt/dumps/tulpan1C'
LISTING_FILE = BACKUP_DIRECTORY + '/.listing'
FTPS_PATH = 'tulpan.ask-gps.ru'
USER = 'backup'
PASS = ''
FTPS_STR = 'ftps://' + USER + ':' + PASS + '@' + FTPS_PATH + '/'
L_SOURCE = []
if not os.path.isdir(BACKUP_DIRECTORY):
        os.mkdir(BACKUP_DIRECTORY)
        print('CREATE BACKUP DIR')

#print('FTPS_STR =' , FTPS_STR)
os.chdir(BACKUP_DIRECTORY)

print("\nНачало скачивания архивов\n")

os.system(f'wget -m --no-check-certificate -rnd {FTPS_STR}')

print("\nОкончание скачивания архивов\n")

#print(os.system('ls'))


def rotate():
        # Получаем листинг файлов источника
        f = open(LISTING_FILE)
        for line in f:
                #print(line)
                L_SOURCE.append(line.split()[8])
#       print('L_SOURCE = ', L_SOURCE)


        # Получаем листинг файлов получателя
        L_DEST = os.listdir()
        L_DEST.remove('.listing')
#       print('L_DEST = ', L_DEST)

        # Список лишних файлов на получателе
        L_UNIC = list(set(L_DEST) - set(L_SOURCE))
#       print('\n l_UNIC = ', L_UNIC)

        # Ротируем лишние файлы
        if L_SOURCE:    # Если листинг файла источника пустой, не будем ротировать, на всяк
                if L_UNIC:
                        print("В каталоге назначения есть файлы, которых нет у источника. Выполняем ротацию\n")
                        for file in L_UNIC:
                                os.remove(file)
                                print("Удаляю файл ", file)
                else:
                        print("Ротировать нечего. Выход")

rotate()
