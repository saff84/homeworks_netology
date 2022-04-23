class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def sr_bal(self):
        all_balls = 0
        sum_all_balls = 0
        for keys in self.grades.values():
            for key_items in keys:
                all_balls += 1
                sum_all_balls += key_items
        if all_balls != 0:
            return sum_all_balls / all_balls
        else:
            return 'Заполните оценки'

    def __str__(self):
        return f'Имя: {str(self.name)} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.sr_bal()} \nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы: Введение в программирование'

    def __lt__(self, other):
        stud1 = self.sr_bal()
        stud2 = other.sr_bal()
        return stud1 < stud2
    def __gt__(self, other):
        stud1 = self.sr_bal()
        stud2 = other.sr_bal()
        return stud1 > stud2


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции: {self.sr_bal}')

    def sr_bal(self):
        all_balls = 0
        sum_all_balls = 0
        for keys in self.grades.values():
            for key_items in keys:
                all_balls += 1
                sum_all_balls += key_items
        if all_balls != 0:
            return sum_all_balls / all_balls
        else:
            return 'Заполните оценки'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.sr_bal()}'

    def __lt__(self, other):
        lector1 = self.sr_bal()
        lector2 = other.sr_bal()
        return lector1 < lector2
    def __gt__(self, other):
        lector1 = self.sr_bal()
        lector2 = other.sr_bal()
        return lector1 > lector2


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


#Студенты
stud1 = Student('Ruoy', 'Eman', 'female')
stud1.courses_in_progress += ['Python']
stud1.courses_in_progress += ['Git']
stud1.courses_in_progress += ['Engish']
# stud1.grades['Python'] = [5, 5, 3, 2, 5]
# stud1.grades['Git'] = [3, 4, 2, 5, 3]
# stud1.grades['Engish'] = [3, 4, 2, 5, 3]
stud1.finished_courses += ['php']
stud1.finished_courses += ['c++']
stud1.finished_courses += ['c#']


stud2 = Student('Ivan', 'Eman', 'male')
stud2.courses_in_progress += ['Python2']
stud2.courses_in_progress += ['Git2']
stud2.courses_in_progress += ['Engish2']
# stud2.grades['Python2'] = [5, 5, 3, 2, 5]
# stud2.grades['Git2'] = [3, 4, 2, 5, 3]
# stud2.grades['Engish2'] = [3, 4, 2, 5, 3]
stud2.finished_courses += ['php2']
stud2.finished_courses += ['c++2']
stud2.finished_courses += ['c#2']

#Лекторы
lector1 = Lecturer('Alexandr', 'Ivanovich')
lector1.courses_attached += ['Python']
lector1.courses_attached += ['Git']
lector1.courses_attached += ['Git2']


lector2 = Lecturer('Ivan', 'Aleksandrovich')
lector2.courses_attached += ['Engish2']
lector2.courses_attached += ['c++2']
lector2.courses_attached += ['c#2']


#Ревьюеры
rev1 = Reviewer('Grigirii', 'Vladlenovich')
rev1.courses_attached += ['Python']
rev1.courses_attached += ['Git']
rev1.courses_attached += ['Git2']

rev2 = Reviewer('Sergey', 'Viktorovich')
rev2.courses_attached += ['Engish2']
rev2.courses_attached += ['c++2']
rev2.courses_attached += ['c#2']


#Начисление оценок
stud1.rate_lecturer(lector1 ,'Python', 5)
stud1.rate_lecturer(lector2 ,'Git', 5)
stud1.rate_lecturer(lector1 ,'Python', 3)
stud1.rate_lecturer(lector2 ,'Git', 4)

stud2.rate_lecturer(lector2 ,'Engish2', 5)
stud2.rate_lecturer(lector2 ,'Engish2', 4)
stud2.rate_lecturer(lector2 ,'Engish2', 3)
stud2.rate_lecturer(lector2 ,'Engish2', 5)

rev1.rate_hw(stud1,'Python', 5)
rev1.rate_hw(stud1,'Git', 5)
rev1.rate_hw(stud2,'Git2', 5)
rev1.rate_hw(stud1,'Python', 4)
rev1.rate_hw(stud1,'Git', 4)
rev1.rate_hw(stud2,'Git2', 3)
rev1.rate_hw(stud1,'Python', 3)
rev1.rate_hw(stud1,'Git', 3)
rev1.rate_hw(stud2,'Git2', 3)

rev2.rate_hw(stud2, 'English2', 4 )
rev2.rate_hw(stud2, 'English2', 5 )
rev2.rate_hw(stud2, 'English2', 3 )
rev2.rate_hw(stud2, 'English2', 4 )
rev2.rate_hw(stud2, 'English2', 2 )


rev2.rate_hw(stud1, 'English', 5 )
rev2.rate_hw(stud1, 'English', 4 )
rev2.rate_hw(stud1, 'English', 5 )
rev2.rate_hw(stud1, 'English', 4 )
rev2.rate_hw(stud1, 'English', 3 )


def sr_ball_po_stud(students_list, predmet):
    all_bals = 0
    sum_all_bals = 0
    for i in students_list:
        for cours in i.grades:
            if cours == predmet:
                for balls in i.grades[cours]:
                    all_bals += 1
                    sum_all_bals += balls

    if all_bals != 0:
        return f'Средний балл студентов по предмету {predmet}: {sum_all_bals / all_bals  }'
    else:
        return f'Такого предмета {predmet} нет у студентов'


def sr_ball_po_lectors(lectors_list, predmet):
    all_bals = 0
    sum_all_bals = 0
    for i in lectors_list:
        for cours in i.grades:
            if cours == predmet:
                for balls in i.grades[cours]:
                    all_bals += 1
                    sum_all_bals += balls

    if all_bals != 0:
        return f'Средний балл лекторов по предмету {predmet}: {sum_all_bals / all_bals  }'
    else:
        return f'Такого предмета {predmet} нет у лекторов'


print(lector1)
print()
print(lector2)
print()
print(stud1)
print()
print(stud2)
print()
print(lector1 > lector2)
print()
print(lector1 < lector2)
print()
print(stud1 > stud2)
print()
print(stud1 < stud2)
print()
print(sr_ball_po_stud([stud1, stud2], 'Python' ))
print()
print(sr_ball_po_stud([lector1, lector2], 'Python' ))

