class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

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

    # def __ne__(self):
    #    None

    @property
    def __str__(self):
        return '"{name}". {author}. {genre}. {year} год'.format(name=self.name, author=self.author, genre=self.genre,
                                                                year=self.year)

    @property
    def __repr__(self):
        return 'Class {classname}'.format(classname=self.__class__)  # , self.__dict__)


book1 = Book('Война и мир', 'Лев Толстой', 1867, 'Роман')
book2 = Book('Война и мир', 'Лев Толстой', 1867, 'Роман')
book3 = book1

if book1 == book3:
    print('Книги идентичны')
else:
    print('Книги различны')

print(book3)

print(book3.__repr__)
