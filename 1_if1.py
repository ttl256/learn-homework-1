"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def what_to_do(age):
    if 4 <= age < 7:
        return "Enjoy your life while you can"
    elif 7 <= age < 18:
        return "Choose math over girls"
    elif 18 <= age < 23:
        return "Knowledge > Grades"
    elif age >= 23:
        return "Welcome to the club" 
    else: 
        raise ValueError("Age must be in [4; inf)")

def main():
    age = int(input("Enter your age: "))
    status = what_to_do(age)
    print(status)

if __name__ == "__main__":
    main()
