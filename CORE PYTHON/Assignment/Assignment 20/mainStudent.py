from SY__init__ import SYMARKS
from TY__init__ import TYMARKS

class Student:
    def __init__(self,roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculateResult(self):
        computer_total = self.sy_marks.computer_total+self.ty_marks.theory+self.ty_marks.practicle

        percentage = (computer_total/300)*100

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return computer_total, percentage, grade

    def display_result(self):
        print('----student Result----')
        print(f'Roll Number: {self.roll_no}')
        print(f'Nmae: {self.name}')

        self.sy_marks.displayMarks()
        self.ty_marks.displayMarks()

        total, percent, grade = self.calculateResult()
        print(f"Total Computer Marks : {total}")
        print(f"Percentage           : {percent:.2f}%")
        print(f"Grade                : {grade}")


if __name__ == "__main__":
        # Create SY and TY mark objects
    sy = SYMARKS(98, 80, 78)
    ty = TYMARKS(60, 85)

        # Create student object
    student1 = Student(1, "Radha", sy, ty)

        # Display the student's result
    student1.display_result()


