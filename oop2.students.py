# სტუდენტის კლასის განსაზღვრა
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_details(self):
        # სტუდენტის დეტალების ჩვენება
        return f"სახელი: {self.name}, ნომერი: {self.roll_number}, შეფასება: {self.grade}"


# სტუდენტების მართვის სისტემა
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        # ახალი სტუდენტის დამატება
        new_student = Student(name, roll_number, grade)
        self.students.append(new_student)
        print(f"სტუდენტი {name} წარმატებით დაემატა.")

    def display_all_students(self):
        # ყველა სტუდენტის ჩვენება
        if not self.students:
            print("სტუდენტების სია ცარიელია.")
        else:
            print("სტუდენტების სია:")
            for student in self.students:
                print(student.display_details())

    def remove_student(self, roll_number):
        # სტუდენტის წაშლა ნომრის მიხედვით
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"სტუდენტი ნომრით {roll_number} წარმატებით წაიშალა.")
                return
        print(f"სტუდენტი ნომრით {roll_number} ვერ მოიძებნა.")

    def search_student(self, roll_number):
        # სტუდენტის ძებნა ნომრის მიხედვით
        for student in self.students:
            if student.roll_number == roll_number:
                print("სტუდენტის დეტალები:")
                print(student.display_details())
                return
        print(f"სტუდენტი ნომრით {roll_number} ვერ მოიძებნა.")

    def update_student_grade(self, roll_number, new_grade):
        # სტუდენტის შეფასების განახლება
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print(f"სტუდენტი ნომრით {roll_number} შეფასება განახლდა: {new_grade}")
                return
        print(f"სტუდენტი ნომრით {roll_number} ვერ მოიძებნა.")


# მთავარი მენიუ
def main():
    sms = StudentManagementSystem()

    while True:
        print("\nსტუდენტების მართვის სისტემა:")
        print("1. ახალი სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის წაშლა")
        print("4. სტუდენტის ძებნა")
        print("5. შეფასების განახლება")
        print("6. გამოსვლა")

        choice = input("აირჩიეთ ოპცია: ")

        if choice == "1":
            name = input("შეიყვანეთ სტუდენტის სახელი: ")
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი: "))
            grade = input("შეიყვანეთ სტუდენტის შეფასება: ")
            sms.add_student(name, roll_number, grade)
        elif choice == "2":
            sms.display_all_students()
        elif choice == "3":
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი წასაშლელად: "))
            sms.remove_student(roll_number)
        elif choice == "4":
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი საძიებლად: "))
            sms.search_student(roll_number)
        elif choice == "5":
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი: "))
            new_grade = input("შეიყვანეთ ახალი შეფასება: ")
            sms.update_student_grade(roll_number, new_grade)
        elif choice == "6":
            print("პროგრამა დასრულდა.")
            break
        else:
            print("არასწორი არჩევანი. გთხოვთ სცადეთ ისევ.")


if __name__ == "__main__":
    main()

