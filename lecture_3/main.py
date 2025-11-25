def main():

    def add_student(students:list):
        """Add new student to list after validating name and checking duplicates."""
        while True:
            name = input("Enter student name: ")
            try:
                if any(char.isdigit() for char in name):
                    raise ValueError("Invalid input. Please enter a name as a string ,  without numbers and punctuation marks!.\n")
                if not all(char.isalnum() for char in name):
                    raise ValueError("Invalid input. Please enter a name as a string, without numbers and punctuation marks!.\n")
                
                for student in students:
                    if name.capitalize() in student:
                        print(f"Student {name.capitalize()} has already been added, enter another student!")
                        break
                else:
                    students.append({name.capitalize():[]})
                    break
            except ValueError as e:
                print(e)


    def add_grade(students:list):
        while True:
            name = input("Enter student name: ").capitalize()
            try:
                if any(char.isdigit() for char in name):
                    raise ValueError("Invalid input. Please enter a name as a string ,  without numbers and punctuation marks!.\n")
                if not all(char.isalnum() for char in name):
                    raise ValueError("Invalid input. Please enter a name as a string, without numbers and punctuation marks!.\n")
                
                for student in students:
                    if name in student:
                        while True:
                            grade = input("Enter a grade (or 'done' to finish): ")
                            if grade == "done": break
                            try:
                                if any(char.isalpha() for char in grade):
                                    raise ValueError("Invalid input. Please enter a number.\n")
                                if not all(char.isalnum() for char in grade):
                                    raise ValueError("Invalid input. Please enter a number.\n")
                                grade_int = int(grade)
                                if  grade_int<0 or grade_int>100:
                                    raise ValueError("Invalid input. Please enter number between 0 and 100.\n")
                                
                                student[name].append(grade_int)
                                
                            except ValueError as e:
                                print(e)
                        break
                else:
                    print("Student not found.")
                break
            except ValueError as e:
                print(e)
        
    
    def gen_report(students:list):
        if students == []:
            print("The list of students is empty.")
        else:
            report_text="--- Student Report ---\n"
            grades = []
            for student in students:
                for key , value in student.items():
                    try:
                        average_grade = round(sum(value)/len(value),1)
                        grades.append(average_grade)
                    except ZeroDivisionError:
                        average_grade = "N/A"
                    report_text += f"{key}'s average grade is {average_grade}\n"
            report_text += "-" *  10
            if grades == []:
                print("Students have no grades")
            else:
                average_overall = round(sum(grades)/len(grades),1)
                report_text += f"\nMax Average: {max(grades)}\nMin Average: {min(grades)}\nOverall Average: {average_overall}"
                print(report_text)

            

    def get_top_students(students:list):
        if students == []:
            print("The list of students is empty.")
        grades = []
        average_grade = lambda x: round(sum(x)/len(x),1)
        for student in students:
            for key, value in student.items():
                try:
                    grades.append(average_grade(value))
                except ZeroDivisionError:
                    grades.append(0)
        max_grade = max(grades)
        max_grade_name = list(students[grades.index(max_grade)].keys())[0]
        print(f"The student with the highest average  is {max_grade_name} with a grade of {max_grade}")
            


    main_menu = "\n--- Student Grade Analyzer ---\n1. Add a new student\n2. Add grades for a student\n3. Generate a full report\n4. Find the top student\n5. Exit program\nEnter your choice: " 
    students = []
    while True:
        menu_item = input(main_menu)
        try:
            menu_item_int = int(menu_item)
            match menu_item_int:
                case 5:
                    break
                case 1:
                    add_student(students=students)
                case 2:
                    add_grade(students=students)
                case 3:
                    gen_report(students=students)
                case 4:
                    get_top_students(students=students)
                case _:
                    print("Invalid input. Please enter a number between 1 and 5!.")

        except ValueError:
            print("Invalid input. Please enter a number.\n")


if __name__ == "__main__":
    main()