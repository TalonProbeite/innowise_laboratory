def main():

    def add_student(students: list):
        """
        Add a new student to the list after validating the entered name.

        The function ensures that the name consists only of alphabetical
        characters, checks whether the student already exists, and adds a new
        dictionary {'name':name,'grades':[]} to the students list.
        """
        while True:
            name_input = input("Enter student name: ").strip()
            try:
                if any(char.isdigit() for char in name_input):
                    raise ValueError(
                        "Invalid input. Please enter a name as a string ,  without numbers and punctuation marks!.\n"
                    )
                if not name_input.isalpha():
                    raise ValueError(
                        "Invalid input. Please enter a name as a string, without numbers and punctuation marks!.\n"
                    )

                name = name_input.capitalize()

                for student in students:
                    if name in student:
                        print(f"Student {name} has already been added, enter another student!")
                        break
                else:
                    students.append({name: []})
                    print(f"Student {name} has been added.")
                    break

            except ValueError as error:
                print(error)

    def add_grade(students: list):
        """
        Add one or multiple grades for an existing student.

        The function validates the student's name, checks that the student
        exists, and then prompts the user to enter grade values. Each grade
        must be a numeric value between 0 and 100. The user can enter multiple
        grades until typing 'done'.
        """
        while True:
            name_input = input("Enter student name: ").strip()
            try:
                if any(char.isdigit() for char in name_input):
                    raise ValueError(
                        "Invalid input. Please enter a name as a string ,  without numbers and punctuation marks!.\n"
                    )
                if not name_input.isalpha():
                    raise ValueError(
                        "Invalid input. Please enter a name as a string, without numbers and punctuation marks!.\n"
                    )

                name = name_input.capitalize()

                for student in students:
                    if name in student:
                        while True:
                            grade_input = input("Enter a grade (or 'done' to finish): ").strip()

                            if grade_input == "done":
                                return

                            try:
                                if any(char.isalpha() for char in grade_input):
                                    raise ValueError("Invalid input. Please enter a number.\n")
                                if not grade_input.isdigit():
                                    raise ValueError("Invalid input. Please enter a number.\n")

                                grade_value = int(grade_input)

                                if grade_value < 0 or grade_value > 100:
                                    raise ValueError(
                                        "Invalid input. Please enter number between 0 and 100.\n"
                                    )

                                student[name].append(grade_value)

                            except ValueError as error:
                                print(error)

                        return
                else:
                    print("Student not found.")
                    return

            except ValueError as error:
                print(error)


    def gen_report(students: list):
        """
        Generate and print a summary report for all students.

        For each student, the function calculates the average of their grades.
        If a student has no grades, their average is displayed as 'N/A'.
        After listing all students, if there are valid averages, the function
        also prints the maximum average, minimum average, and overall class average.

        Parameters:
            students (list): A list of dictionaries containing students
                            and their grade lists.
        """
        if not students:
            print("The list of students is empty.")
            return

        report_text = "--- Student Report ---\n"
        averages = []

        for student in students:
            for name, grades in student.items():
                try:
                    average_value = round(sum(grades) / len(grades), 1)
                    averages.append(average_value)
                except ZeroDivisionError:
                    average_value = "N/A"

                report_text += f"{name}'s average grade is {average_value}\n"

        report_text += "-" * 10

        if not averages:
            print("Students have no grades")
            return

        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = round(sum(averages) / len(averages), 1)

        report_text += (
            f"\nMax Average: {max_avg}"
            f"\nMin Average: {min_avg}"
            f"\nOverall Average: {overall_avg}"
        )

        print(report_text)


    def get_top_students(students: list):
        """
        Find and display the student with the highest average grade.

        The function calculates each student's average grade. If a student
        has no grades, their average is treated as 0. The student with the
        highest average is then printed.

        Parameters:
            students (list): A list of dictionaries storing students
                            and their grade lists.
        """
        if not students:
            print("The list of students is empty.")
            return


        averages = []
        names = []

        for student in students:
            for name, grades in student.items():
                try:
                    avg_value = round(sum(grades) / len(grades), 1)
                except ZeroDivisionError:
                    avg_value = 0

                names.append(name)
                averages.append(avg_value)


        max_average = max(averages)
        max_index = averages.index(max_average)
        top_student = names[max_index]

        print(f"The student with the highest average is {top_student} with a grade of {max_average}")


    main_menu = (
        "\n--- Student Grade Analyzer ---\n"
        "1. Add a new student\n"
        "2. Add grades for a student\n"
        "3. Generate a full report\n"
        "4. Find the top student\n"
        "5. Exit program\n"
        "Enter your choice: "
    )

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
                    print("Invalid input. Please enter a number between 1 and 5!")

        except ValueError:
            print("Invalid input. Please enter a number.\n")


if __name__ == "__main__":
    main()