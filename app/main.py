from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


# Создаем класс наследник, через него может отслеживать изменения в папках
class Handler(FileSystemEventHandler):
	# При любых изменениях в папке, мы перемещаем файлы в ней
	def on_modified(self, event):
		for filename in os.listdir(folder_track):
			file = folder_track + filename
			new_path = folder_dest + '\\' + filename
			print(file+'\n'+new_path)
			os.rename(file, new_path)





# Папка что отслеживается
folder_track = 'D:\\'
# Папка куда перемещать будем
folder_dest = 'D:\\test'

# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

# Программа будет срабатывать каждые 10 милисекунд
try:
	while (True):
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()
