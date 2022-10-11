class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'Python': 10, 'Git': 10}
        self.average = []
    def rate_lec(self, lectorer, course, grade):
        if isinstance(lectorer, Lectorer) and course in self.courses_in_progress and course in lectorer.courses_attached:
            if course in lectorer.grades:
                lectorer.grades[course] += [grade]
            else:
                lectorer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average(self):
        grade = []
        amount = []
        for y in self.grade.items():
            grade.append(y)
            for x in grade:
                amount.extend(x)
        self.average = sum(amount)/len(amount)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\nСредняя оценка: {self.average}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res1 = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res1
        

class Lectorer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {'Python': 9, 'Git': 10}
    def average(self):
        t = []
        f = []
        for k, y in self.grades.items():
            t.append(y)
            for x in t:
                f.extend(x)
        self.average = sum(f)/len(f)     
    def __str__(self):
        res2 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}'
        return res2
    
    

some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в програмирование']
some_reviewer = Reviewer('Artem', 'Ladov')
print(some_student)