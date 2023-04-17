from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# class App(QApplication):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.win = QMainWindow()
#         uic.loadUi('ui.ui', self.win)
#
#
# app = App(sys.argv)
# app.exec()

def print_to_pechat():
    with open('pechat.txt', mode='a', encoding='utf=8') as pechat:
        lines = []
        with open('zhurnal.txt', mode='r', encoding='utf-8') as file:
            for index, line in enumerate(file):
                if index % 6 == 0:
                    lines.append('\n')
                lines[-1] += ' ' + line.strip()
        pechat.writelines(lines)


def append():
    with open('zhurnal.txt', mode='r', encoding='utf-8') as file:
        pass
        # добавляет в журнал
        # for index, line in enumerate(file):
        #     if index % 6 == 0:
        #         lines.append('\n')
        #     lines[-1] += ' ' + line.strip()


def print_to_excel():
    import pandas as pd
    values = []
    with open('zhurnal.txt', mode='r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            if index % 6 == 2:
                values.append(line.strip())
    df = pd.DataFrame([
        ['ФИО'],
        values
    ])
    filepath = 'export.xlsx'
    df.to_excel(filepath, index=False, index_label=None, header=False)

print_to_excel()
