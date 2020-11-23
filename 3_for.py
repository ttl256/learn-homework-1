"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def avg(lst):
    sum = 0
    for i in lst:
        sum += i
    avg = sum / len(lst)
    return avg

def main():
    class_list = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5a', 'scores': [3,4,4,5,2,5,5,5]},
        {'school_class': '7a', 'scores': [3,4,4,5]}
    ]

    class_avg_list = []
    for class_ in class_list:
        # Calculate average score for a class
        class_avg = round(avg(class_.get("scores")), 2)
        class_name = class_.get("school_class")
        print(f"Average for {class_name} is {class_avg}")
        # Build a list of averages for all classes in school
        class_avg_list.append(class_avg)
    
    print("School average")
    print(round(avg(class_avg_list), 2))

if __name__ == "__main__":
    main()
