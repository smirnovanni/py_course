import datetime


class Feedback:
    def __init__(self, text, author, date):
        self.text = text
        self.author = author
        self.date = date


class Book:
    count_books = 0

    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        Book.count_books += 1
        self.feedbacks = []

    def __eq__(self, other):
        flag = True
        if self.name != other.name:
            print('Не совпадает название!')
            flag = False
        if self.author != other.author:
            print('Не совпадает автор!')
            flag = False
        if self.year != other.year:
            print('Не совпадает год издания!')
            flag = False
        if self.genre != other.genre:
            print('Не совпадает жанр!')
            flag = False

        if flag:
            return True
        else:
            return False

    @property
    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def __str__(self):
        fdbk = ""
        for c in self.feedbacks:
            fdbk += c.text + " " + c.author + " " + c.date.strftime('%d.%m.%Y') + "\n"
        return '"{name}". {author}. {genre}. {year} год\n{feedback}'.format(name=self.name, author=self.author,
                                                                            genre=self.genre,
                                                                            year=self.year, feedback=fdbk)

    @property
    def __repr__(self):
        return 'Class {classname}, {dict}'.format(classname=self.__class__, dict=self.__dict__)

    def add_feedback(self, text, author, date):
        self.feedbacks.append(Feedback(text, author, date))

    def __del__(self):
        Book.count_books -= 1

    @staticmethod
    def print_count_book():
        print(Book.count_books)


book1 = Book('Война и мир', 'Лев Толстой', 1867, 'Роман')
book2 = Book('Нос', 'Гоголь', 1836, 'Роман')
book3 = Book('Евгений Онегин', 'Пушкин', 1833, 'Роман')
book3.add_feedback('Книга хорошая', 'Сергей', datetime.datetime.now())
book3.add_feedback('Книга супер', 'Анюта', datetime.datetime.now())
book2.add_feedback('Так себе', 'Анюта', datetime.datetime.now())

#
# if book1 == book3:
#    print('Книги идентичны')
# else:
#    print('Книги различны')
#
# print(book3.__str__)
# print(book3.__repr__)
#
print(Book.print_count_book())  # staticmethod
