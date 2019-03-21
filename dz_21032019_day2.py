"""
Задание 1. Создайте класс Editor, который содержит методы view_document и
edit_document. Пусть метод edit_document выводит на экран информацию о том,
что редактирование документов недоступно для бесплатной версии. Создайте
подкласс ProEditor, в котором данный метод будет переопределён. Введите с
клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса
ProEditor, иначе Editor. Вызовите методы просмотра и редактирования
документов.
"""

import datetime
import hashlib


class Editor:
    def __init__(self, num_doc, date, text):
        self.num_doc = num_doc
        self.date = date
        self.text = text

    def edit_document(self, **kwargs):
        print("Редактирование доступно только в платной версии!!!")

    def view_document(self):
        print('num_doc = {num_doc}, date = {date}, text = {text}'.format(num_doc=self.num_doc,
                                                                         date=self.date.strftime('%d.%m.%Y %H:%M:%S'),
                                                                         text=self.text))


class ProEditor(Editor):
    def __init__(self, num_doc, date, text):
        super().__init__(num_doc, date, text)

    def edit_document(self, **kwargs):
        num_doc, date, text = kwargs.values()
        self.num_doc, self.date, self.text = num_doc, date, text


if hashlib.md5(input("Введите серийный номер платной версии: ").encode(
        'utf-8')).hexdigest() != 'e10adc3949ba59abbe56e057f20f883e':  # '123456'
    e = Editor(1, datetime.datetime.now(), 'Текст документа')
else:
    e = ProEditor(2, datetime.datetime.now(), 'Текст документа')

e.view_document()
e.edit_document(num_doc=3, date=datetime.datetime.now(), text='Текст документа')
e.view_document()
