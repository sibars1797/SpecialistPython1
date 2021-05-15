# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    import os
    path = os.path.join('data', file)
    with open(path, 'a', encoding='UTF-8') as f:
        print(text, file=f)


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
