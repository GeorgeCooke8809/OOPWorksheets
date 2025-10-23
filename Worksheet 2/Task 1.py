class Person:
    def __init__(self, surname, firstname, gender):
        self.surname = surname
        self.firstname = firstname
        self.gender = gender

    def viewDetails(self):
        print(f"First Name: {self.firstname}\nSurname: {self.surname}\nGender: {self.gender}")


class Student(Person):
    def __init__(self, surname, firstname, gender, target, score, street):
        super().__init__(surname, firstname, gender)
        self.target = target
        self.base_score = score
        self.street_number = street

    def add_target_grade(self, grade):
        self.target = grade

    def add_base_score(self, score):
        self.base_score = score

    def set_street_number(self, number):
        self.street_number = number

    def view_details(self):
        print(f"Name: {self.surname}, {self.firstname}\nGender: {self.gender}\nGrade: {self.grade}Score: {self.score}\nStreet: {self.street_number}")


class Teacher(Person):
    def __init__(self, surname, firstname, gender, subject, faculty):
        super().__init__(surname, firstname, gender)
        self.subjects = (subject)
        self.faculty = faculty

    def add_subject(self, subject):
        self.subjects.append(subject)

    def update_faculty(self, faculty):
        self.faculty = faculty
    
    def view_subjects(self):
        print("Subjects:")
        for i in self.subjects:
            print(f"- {i}")

    def view_details(self):
        print(f"Name: {self.surname}, {self.firstname}\nGender: {self.gender}\nFaculty: {self.faculty}")
        self.view_subjects()


teacher = Teacher("Smith", "Tomasz", "Male")