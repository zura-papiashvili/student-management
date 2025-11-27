import json
import os

from student import Student

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students.json")

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


def load_students_from_file(file_path: str = DATA_FILE):
    """Load students from a JSON file, returning a list of Student objects."""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Warning: Could not read student data ({exc}). Starting with an empty list.")
        return []

    students = []
    for entry in data:
        try:
            name = entry.get("name", "")
            roll_number = int(entry.get("roll_number", 0))
            grade = entry.get("grade", "")
            students.append(Student(name, roll_number, grade))
        except Exception as exc:
            print(f"Warning: Skipping invalid student record {entry!r} ({exc}).")
    return students


def save_students_to_file(students, file_path: str = DATA_FILE):
    """Persist current students to disk."""
    try:
        serialized = [
            {"name": student.name, "roll_number": student.roll_number, "grade": student.grade}
            for student in students
        ]
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file, indent=4)
    except OSError as exc:
        print(f"Warning: Failed to save student data ({exc}).")


def sanitize_grade_input(raw_grade: str) -> str:
    """Validate and normalize grade input."""
    grade = (raw_grade or "").strip().upper()
    if not grade:
        raise ValueError("Grade cannot be empty!")
    allowed_display = ", ".join(Student.allowed_grades())
    if len(grade) != 1 or grade not in Student.allowed_grades():
        raise ValueError(f"Grade must be one of: {allowed_display}.")
    return grade


def sanitize_roll_number_input(raw_number: str) -> int:
    """Validate roll number input ensuring positive integers."""
    cleaned_value = (raw_number or "").strip()
    if not cleaned_value:
        raise ValueError("Roll number is required.")
    try:
        roll_number = int(cleaned_value)
    except ValueError as exc:
        raise ValueError("Roll number must be a valid integer!") from exc
    if roll_number <= 0:
        raise ValueError("Roll number must be a positive integer!")
    return roll_number

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
        
        grade_input = input("Enter grade: ")
        grade = sanitize_grade_input(grade_input)
        
        student = Student(name, roll_number, grade)
        students.append(student)
        save_students_to_file(students)
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
        roll_number_input = input("Enter roll number to search: ")
        roll_number = sanitize_roll_number_input(roll_number_input)
        
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
            
    except ValueError as exc:
        print(f"Error: {exc}")

def update_student_grade(students):
    print("\n--- Update Student Grade ---")
    
    if not students:
        print("No students found in the system.")
        return
    
    try:
        roll_number_input = input("Enter roll number to update: ")
        roll_number = sanitize_roll_number_input(roll_number_input)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    found_student = None
    for student in students:
        if student.roll_number == roll_number:
            found_student = student
            break
    
    if found_student:
        print(f"\nCurrent student information:")
        print(f"   {found_student}")
        
        try:
            new_grade_input = input("\nEnter new grade: ")
            new_grade = sanitize_grade_input(new_grade_input)
        except ValueError as exc:
            print(f"Error: {exc}")
            return
        
        old_grade = found_student.grade
        found_student.grade = new_grade
        save_students_to_file(students)
        print(f"\n✓ Grade updated successfully!")
        print(f"   Roll Number {roll_number}: {old_grade} → {new_grade}")
    else:
        print(f"\n✗ No student found with roll number {roll_number}.")

def main():
    students = load_students_from_file()
    
    print("Welcome to the Student Management System!")
    if students:
        print(f"Loaded {len(students)} student(s) from storage.")
    
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

