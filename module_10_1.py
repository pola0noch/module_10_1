# Домашнее задание по теме "Создание потоков".

import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i + 1} \n")
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


start_time_functions = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = time.time()
print(f"Время работы функций: {end_time_functions - start_time_functions} секунд")

start_time_threads = time.time()

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время работы потоков: {end_time_threads - start_time_threads} секунд")

