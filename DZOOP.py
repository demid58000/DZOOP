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
Средняя оценка за домашние задания:{round(self.average_grade(), 1)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы:{", ".join(self.finished_courses)}'''

    def average_grade(self):
        sum_ = 0
        count = 0
        for elem in self.grades.values():
            sum_ += sum(elem)
            count += len(elem)

        if count == 0:
            return 0
        return sum_ / count

    # def compare_students(self, student):
    #   if isinstance(student, Student):
    #     if self.average_grade() < student.average_grade():
    #       return f"""{self.name} {self.surname} получает оценки ниже, чем {student.name} {student.surname} """
    #     elif self.average_grade() > student.average_grade():
    #       return f"""{self.name} {self.surname} получает оценки выше, чем {student.name} {student.surname} """
    #     else:
    #       return f"""{self.name} {self.surname} получает оценки такие же, как и  {student.name} {student.surname} """
    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self.average_grade() < other_student.average_grade()
        return 'Не можем сравнить'

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
Средняя оценка за лекции: {round(self.average_grade(), 1)}'''

    def __lt__(self, other_lector):
        if isinstance(other_lector, Lectures):
            return self.average_grade() < other_lector.average_grade()
        return 'Не можем сравнить'

    def average_grade(self):
        sum_ = 0
        count = 0
        for elem in self.grades.values():
            sum_ += sum(elem)
            count += len(elem)

        if count == 0:
            return 0
        return sum_ / count
    # def compare_lectures(self, lector):
    #   if isinstance(lector, Lectures):
    #     if self.average_grade() < lector.average_grade():
    #       return f"""{self.name} {self.surname} получает оценки ниже, чем {lector.name} {lector.surname} """
    #     elif self.average_grade() > lector.average_grade():
    #       return f"""{self.name} {self.surname} получает оценки выше, чем {lector.name} {lector.surname} """
    #     else:
    #       return f"""{self.name} {self.surname} получает оценки такие же, как и  {lector.name} {lector.surname} """


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


def all_average_grades_lectures(*lectures, course_name):
    sum_ = 0
    count = 0
    for lector in lectures:
        if course_name in lector.courses_attached:
            sum_ += sum(lector.grades[course_name])
            count += len(lector.grades[course_name])
    if count == 0:
        return 0
    return round(sum_ / count, 1)


student1 = Student('Bob', "Marley", 'man')
student2 = Student('Bob2', "Marley", 'man')

best_student = Student('Ruoy', 'Eman', 'female')
best_student.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student2.courses_in_progress += ['C++', 'Python']
student2.finished_courses += ['C']

cool_lector = Lectures('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

cool_reviever = Reviewer('Bob', 'Salivan')
cool_reviever.courses_attached += ['Python', 'C++', 'Java']

cool_reviever2 = Reviewer('Matt', 'Salivan')
cool_reviever2.courses_attached += ['C++', 'Java']

cool_lector2 = Lectures('Bob', 'Marley')
cool_lector2.courses_attached += ['Java', 'C++']

cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(student1, 'Python', 10)
cool_reviever.rate_hw(student2, 'Python', 10)

student1.marks(cool_lector, 'Python', 10)
best_student.marks(cool_lector, 'Python', 10)

best_student.marks(cool_lector, 'Python', 9)
print(best_student)
print(cool_lector)
print(cool_reviever)

print(cool_reviever)
print(cool_reviever2)
print(cool_lector)
print(cool_lector2)
print(best_student)
print(student2)
print('---------------------------------')
print(best_student.average_grade(), student2.average_grade())
print(best_student.__lt__(student2))
print(best_student < student2)
print(best_student > student2)
print('---------------------------------')
print(best_student < cool_lector)
print(best_student > cool_lector)
print('---------------------------------')
print(cool_lector.average_grade(), cool_lector.average_grade())
print(cool_lector > cool_lector2)

all_average_grades_students(student1, student2, course_name='Python')
all_average_grades_lectures(cool_lector, cool_lector2, course_name='Python')