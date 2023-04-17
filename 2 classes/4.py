# 2.4.	Разработать класс ZDate для хранения и манипулирования датой. Разработать класс Session для хранения
# информации об экзаменах, включая дату, преподавателя, группу, дисциплину. Вывести график сдачи экзаменов

class ZDate:
    def __init__(self, year, month, day, hour=0, minute=0, sec=0):
        if year < 0:
            raise Exception('Год > 0')
        if 1 > month or month > 12:
            raise Exception('1 > Месяц or Месяц > 12')
        if 0 >= day or day > 31:
            raise Exception('0 >= День or День > 31')
        if 0 > hour or hour > 23:
            raise Exception('0 > Часы or Часы > 23')
        if 0 > minute or minute > 59:
            raise Exception('0 > Минуты or Минуты > 59')
        if 0 > sec or sec > 59:
            raise Exception('0 > Секунды or Секунды > 59')

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __str__(self):
        return f'{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.sec}'


class Exam:
    def __init__(self, teacher, group, category, date):
        self.teacher = teacher
        self.group = group
        self.category = category
        self.date = date

    def __str__(self):
        return f'{self.teacher}, {self.group}, {self.category}, {self.date}'


class Session:
    def __init__(self):
        self.exams = []

    def add_exam(self, *args):
        self.exams.append(Exam(*args))

    def print(self):
        for exam in self.exams:
            print(exam)


session = Session()
session.add_exam('Бабаева', '41-ИС', 'ПМ', ZDate(2022, 1, 12, 8, 30, 0))
session.add_exam('Бабаasdева', '41-ИС', 'ПМasdasdasd', ZDate(2022, 1, 12, 8, 30, 0))
session.add_exam('Бабаеваasdasd', '41-ИС', 'ПМ', ZDate(2022, 1, 12, 8, 30, 12))
session.print()
