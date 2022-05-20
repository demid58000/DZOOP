class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания:{round(self.avarage_grade(), 1)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы:{", ".join(self.finished_courses)}'''

    def avarage_grade(self):
        sum_ = 0
        count = 0
        for elem in self.grades.values():
            sum_ += sum(elem)
            count += len(elem)

        if count == 0:
            return 0
        return sum_ / count

    def compare_students(self, student):
        if isinstance(student, Student):
            if self.average_grade() < student.average_grade():
                return f"""{self.name} {self.surname} получает оценки ниже, чем {student.name} {student.surname} """
            elif self.average_grade() > student.average_grade():
                return f"""{self.name} {self.surname} получает оценки выше, чем {student.name} {student.surname} """
            else:
                return f"""{self.name} {self.surname} получает оценки такие же, как и  {student.name} {student.surname} """

    def marks(self, lector, course, mark):
        if isinstance(lector, Lectures) and (course in self.finished_courses \
                                             or course in self.courses_in_progress) and course in lector.courses_attached:
            if course not in lector.grades:
                lector.grades[course] = [mark]
            else:
                lector.grades[course] += [mark]
        else:
            return ('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectures(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {round(self.avarage_grade(), 1)}'''

    def avarage_grade(self):
        sum_ = 0
        count = 0
        for elem in self.grades.values():
            sum_ += sum(elem)
            count += len(elem)
        return sum_ / count

    def compare_lectures(self, lector):
        if isinstance(lector, Lectures):
            if self.average_grade() < lector.average_grade():
                return f"""{self.name} {self.surname} получает оценки ниже, чем {lector.name} {lector.surname} """
            elif self.average_grade() > lector.average_grade():
                return f"""{self.name} {self.surname} получает оценки выше, чем {lector.name} {lector.surname} """
            else:
                return f"""{self.name} {self.surname} получает оценки такие же, как и  {lector.name} {lector.surname} """


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


def all_average_grades_students(*students, course_name):
    sum_ = 0
    count = 0
    for student in students:
        if course_name in student.courses_in_progress:
            sum_ += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    if count == 0:
        return 0
    return round(sum_ / count, 1)


student1 = Student('Bob', "Marley", 'man')
student2 = Student('Bob2', "Marley", 'man')
all_average_grades_students(student1, student2, course_name="Python")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lector = Lectures('Some', 'Buddy')
cool_lector.courses_attached += ['Python']
cool_reviever = Reviewer('Bob', 'Salivan')

cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student, 'Python', 10)

best_student.marks(cool_lector, 'Python', 9)
print(best_student)
print(cool_lector)
print(cool_reviever)