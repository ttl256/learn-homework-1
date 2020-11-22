"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def compare_strings(string1, string2):
    if not (type(string1) == str and type(string2) == str):
        return 0
    elif string1 == string2:
        return 1
    else:
        if len(string1) > len(string2):
            return 2
        elif string2 == "learn":
            return 3
        else:
            raise Exception("Don't do anything funny")

def main():
    print(compare_strings(1, 34.34)) #0
    print(compare_strings("test", "test")) #1
    print(compare_strings("test1", "test")) #2
    print(compare_strings("test1", "learn")) #3
    print(compare_strings(1337, "learn")) #0
    print(compare_strings("test", "test1")) #Exception string1 < string2
    
if __name__ == "__main__":
    main()
