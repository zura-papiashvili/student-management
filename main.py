from student import Student

def display_menu():
    print("\n" + "="*50)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search for Student by Number")
    print("4. Update Student Grade")
    print("5. Log Out")
    print("="*50)

def add_new_student(students):
    print("\n--- Add New Student ---")
    
    try:
        name = input("Enter student's name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return
        
        if students:
            roll_number = max(s.roll_number for s in students) + 1
        else:
            roll_number = 1
        
        grade = input("Enter grade: ").strip().upper()
        if not grade:
            print("Error: Grade cannot be empty!")
            return
        
        student = Student(name, roll_number, grade)
        students.append(student)
        print(f"\n✓ Student '{name}' (Roll Number: {roll_number}) added successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def view_all_students(students):
    print("\n--- View All Students ---")
    
    if not students:
        print("No students found in the system.")
        return
    
    print(f"\nTotal Students: {len(students)}")
    print("-" * 50)
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")
    print("-" * 50)

def search_student_by_number(students):
    print("\n--- Search for Student by Number ---")
    
    if not students:
        print("No students found in the system.")
        return
    
    try:
        roll_number = int(input("Enter roll number to search: "))
        
        found_student = None
        for student in students:
            if student.roll_number == roll_number:
                found_student = student
                break
        
        if found_student:
            print("\n✓ Student Found:")
            print(f"   {found_student}")
        else:
            print(f"\n✗ No student found with roll number {roll_number}.")
            
    except ValueError:
        print("Error: Roll number must be a valid integer!")

def update_student_grade(students):
    print("\n--- Update Student Grade ---")
    
    if not students:
        print("No students found in the system.")
        return
    
    try:
        roll_number = int(input("Enter roll number to update: "))
        
        found_student = None
        for student in students:
            if student.roll_number == roll_number:
                found_student = student
                break
        
        if found_student:
            print(f"\nCurrent student information:")
            print(f"   {found_student}")
            
            new_grade = input("\nEnter new grade: ").strip().upper()
            if not new_grade:
                print("Error: Grade cannot be empty!")
                return
            
            old_grade = found_student.grade
            found_student.grade = new_grade
            print(f"\n✓ Grade updated successfully!")
            print(f"   Roll Number {roll_number}: {old_grade} → {new_grade}")
        else:
            print(f"\n✗ No student found with roll number {roll_number}.")
            
    except ValueError:
        print("Error: Roll number must be a valid integer!")

def main():
    students = []
    
    print("Welcome to the Student Management System!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                view_all_students(students)
            elif choice == "3":
                search_student_by_number(students)
            elif choice == "4":
                update_student_grade(students)
            elif choice == "5":
                print("\nThank you for using the Student Management System!")
                print("Goodbye!")
                break
            else:
                print("\n✗ Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Thank you for using the Student Management System!")
            break
        except Exception as e:
            print(f"\n✗ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

