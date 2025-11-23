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

        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()


