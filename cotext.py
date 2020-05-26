import datetime
import time

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
        


    def __enter__(self):
        print(f"Время запуска программы: {datetime.datetime.utcnow()}")
        self.time = time.time()
        return self.file_obj
        

    def __exit__(self, type, value, traceback):
        print(f"Время окончания программы: {datetime.datetime.utcnow()}")
        print(f"время работы программы: {time.time() - self.time}")
        self.file_obj.close()
        

lines = ''
with open('prince.txt', encoding='utf-8') as file:
    for line in file:
        lines = line.strip()
          

with File('request.txt', 'w') as opened_file:
    opened_file.write(lines)














# class Timers:
#     def __init__(self, file):
#         self.file = file

#     def reader(self):
#         with open(self.file) as file:
#             print(file.readlines())

#     def __enter__(self):
#         self.file = open(self.file)
#         self.t = time.time()
#         print(datetime.datetime())

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         print(time.time() - self.t) 
#         print(datetime.datetime())

# timers = Timers('prince.txt')
# timers.reader()
