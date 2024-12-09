# ოოპ პროექტი: წიგნების მართვის კონსოლ აპლიკაცია

# 1.წიგნების კლასის განსაზღვრა
class Book:
    def __init__ (self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f"წიგნი ({self.name!r}, {self.author!r}, {self.year!r})"

# 2. BookManager კლასი
class BookManager:
    def __init__(self):
        # სიის შექმნა
        self.books = []
    # წიგნის დამატება სიაში:
    def add_book(self, name, author, year):
        new_book = Book(name, author, year)
        self.books.append(new_book)
        print (f"{new_book} დაემატა ბიბლიოთეკას")
    # წიგნების სიის ჩვენება:
    def show_books(self):
        if not self.books:
            print("ბიბილიოთეკაში წიგნები არ არის")
        else:
            for i in self.books:
                print (i)
    # წიგნის მოძებნა სათაურის მიხედვით:
    def search_book(self, name):
        found_book = [book for book in self.books if name.lower() in book.name.lower()]
        if found_book:
            for book in found_book:
                print(book)
        else:
            print("ამ დასახელების წიგნი ვერ მოიძებნა ბიბლიოთეკაში")


bookmanager = BookManager()
bookmanager.add_book("Les Miserables", "Victor Hugo", 1862)
bookmanager.show_books()
bookmanager.search_book("Les Miserables")

# User interface

while True:
    print("მოგესალმებით თქვენ ხართ ბიბლიოთეკის აპლიკაციაში")
    action = input("""აირჩიეთ შემდეგი მოქმედება "
                   "1) - წიგნის დამატება,"
                    2) - ბიბლიოთეკის ჩვენება"
                    3) - წიგნის ძებნა"
                    4) - აპლიკაციიდან გასვლა    
                        """ ).strip().lower()

    if action == "1":
        chamateba1 = input("შეიყვანე სახელი   ").strip().lower()
        chamateba2 = input("შეიყვანე ავტორი    ").strip().lower()
        chamateba3 = int(input("შეიყვანე წელი   ").strip().lower())
        if chamateba3 > 2025:
            print("შეიყვანეთ სწორი წელი!!!")
        else:
            bookmanager.add_book(chamateba1, chamateba2, chamateba3)

    elif action == "2":
        bookmanager.show_books()

    elif action == "3":
        search = input("შეიყვანეთ წიგნის სახელი   ").strip().lower()
        bookmanager.search_book(search)

    elif action == "4":
        print("თქვენ დატოვეთ ბიბლიოთეკის აპლიკაცია, ნახვამდის!")
        break

    else:
        print("არასწორი არჩევანია, უნდა აირჩიოთ (1-4) მოქმედება.")