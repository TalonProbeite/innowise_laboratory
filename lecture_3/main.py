def main():

    def add_student(students: list):
        """
        Add a new student to the list after validating the entered name.

        The function ensures the name consists only of alphabetic characters,
        checks for duplicates, and then adds the student as a dictionary
        {Name: []} to the students list.

        Parameters:
            students (list): A list of dictionaries storing students
                             and their grade lists.
        """
        while True:
            name = input("Enter student name: ").strip()
            try:
                if any(char.isdigit() for char in name):
                    raise ValueError("Invalid input. Please enter a name without numbers.\n")
                if not name.isalpha():
                    raise ValueError("Invalid input. Please enter a name using only letters.\n")

                formatted_name = name.capitalize()

                for student in students:
                    if formatted_name in student:
                        print(f"Student {formatted_name} has already been added. Enter another name.")
                        break
                else:
                    students.append({formatted_name: []})
                    break

            except ValueError as error:
                print(error)

    def add_grade(students: list):
        """
        Add grade values for an existing student.

        The function validates the student's name and verifies their presence
        in the list. It accepts multiple grades until the user enters 'done'.
        Grades must be numeric values between 0 and 100.

        Parameters:
            students (list): A list of dictionaries with student names
                             mapped to their grade lists.
        """
        while True:
            name = input("Enter student name: ").capitalize().strip()
            try:
                if any(char.isdigit() for char in name):
                    raise ValueError("Invalid input. Please enter a name without numbers.\n")
                if not name.isalpha():
                    raise ValueError("Invalid input. Please enter a name using only letters.\n")

                for student in students:
                    if name in student:
                        while True:
                            grade = input("Enter a grade (or 'done' to finish): ").strip()
                            if grade == "done":
                                break
                            try:
                                if not grade.isdigit():
                                    raise ValueError("Invalid input. Please enter a number.\n")

                                grade_value = int(grade)

                                if grade_value < 0 or grade_value > 100:
                                    raise ValueError("Invalid input. Enter a number between 0 and 100.\n")

                                student[name].append(grade_value)

                            except ValueError as error:
                                print(error)
                        break
                else:
                    print("Student not found.")
                break

            except ValueError as error:
                print(error)

    def gen_report(students: list):
        """
        Generate and print a detailed grade report.

        The report includes each student's average grade. If grades exist,
        it also displays the maximum average, minimum average,
        and overall class average.

        Parameters:
            students (list): A list of dictionaries containing students
                             and their grade lists.
        """
        if students == []:
            print("The list of students is empty.")
            return

        report_text = "--- Student Report ---\n"
        average_values = []

        for student in students:
            for name, grades in student.items():
                try:
                    avg_grade = round(sum(grades) / len(grades), 1)
                    average_values.append(avg_grade)
                except ZeroDivisionError:
                    avg_grade = "N/A"

                report_text += f"{name}'s average grade is {avg_grade}\n"

        report_text += "-" * 10

        if average_values == []:
            print("Students have no grades.")
        else:
            overall_average = round(sum(average_values) / len(average_values), 1)
            report_text += (
                f"\nMax Average: {max(average_values)}"
                f"\nMin Average: {min(average_values)}"
                f"\nOverall Average: {overall_average}"
            )
            print(report_text)

    def get_top_students(students: list):
        """
        Determine and display the student with the highest average grade.

        If a student has no grades, they are treated as having an average of 0.

        Parameters:
            students (list): A list of dictionaries mapping student names
                             to their grade lists.
        """
        if students == []:
            print("The list of students is empty.")
            return

        compute_avg = lambda grades: round(sum(grades) / len(grades), 1) if grades else 0

        averages = []

        for student in students:
            for _, grade_list in student.items():
                averages.append(compute_avg(grade_list))

        max_grade = max(averages)
        max_name = list(students[averages.index(max_grade)].keys())[0]

        print(f"The student with the highest average is {max_name} with a grade of {max_grade}")

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
