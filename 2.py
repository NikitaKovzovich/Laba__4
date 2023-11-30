# Разработать класс Faculty, включающий в себя название факультета.
# Реализовать класс Student, включающий следующие компоненты данных:
# Ф.И.О. студента, год рождения, результаты сдачи последней сессии.
# Классы должны содержать методы доступа и изменения всех полей.
# Написать программу, которая считывает данные о студентах и выдает информацию об их успеваемости.

class Faculty:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_student_info(self):
        print(f"\nФакультет: {self.name}")
        print("\nИнформация о студентах:")
        for student in self.students:
            student.display_info()

class Student:
    def __init__(self, full_name, birth_year):
        self.full_name = full_name
        self.birth_year = birth_year
        self.exam_results = []

    def add_exam_result(self, result):
        self.exam_results.append(result)

    def calculate_average_score(self):
        if not self.exam_results:
            return 0
        return sum(map(float, self.exam_results)) / len(self.exam_results)

    def display_info(self):
        average_score = self.calculate_average_score()
        print(f"Студент: {self.full_name}")
        print(f"Год рождения: {self.birth_year}")
        print(f"Средний балл за сессию: {average_score:.2f}")



faculty_name = input("Введите название факультета: ")
faculty = Faculty(faculty_name)

while True:
    student_name = input("\nВведите ФИО студента (0 - выход): ")
    if student_name.lower() == '0':
        break

    birth_year = input("Введите год рождения студента: ")
    student = Student(student_name, birth_year)

    for i in range(3):
        result = input(f"Введите результат сдачи экзамена {i + 1} для студента {student_name} (1-10): ")

        while not result.isdigit() or not (1 <= int(result) <= 10):
            print("Ошибка! Введите корректный результат сдачи экзамена (1-10).")
            result = input(f"Введите результат сдачи экзамена {i + 1} для студента {student_name} (1-10): ")

    faculty.add_student(student)

faculty.display_student_info()