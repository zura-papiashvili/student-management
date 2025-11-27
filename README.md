# Student Management System

Console-based student management system written in Python. It demonstrates core OOP ideas (encapsulation, inheritance, and polymorphism) while providing a simple menu-driven workflow for managing students.

## Features
- Student model inherits from a generic Person base class with validated properties.
- Menu actions: add student, view all, search by roll number, update grade, exit.
- Input validation for names, roll numbers (positive integers), and grades (letters A-F).
- Automatic roll number assignment for new students.
- Persistence layer backed by `students.json`, so data survives between runs.

## Requirements
- Python 3.9+

## Usage
1. Install dependencies (standard library only, so no extra steps required).
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow on-screen prompts to interact with the system.

## Data Storage
- Student data resides in `students.json` in the project root.
- The file is loaded on startup; every add/update operation saves back to disk.
- You can pre-populate the file with an array of objects using keys `name`, `roll_number`, and `grade`.

## Extensibility Ideas
- Add delete functionality for students.
- Enhance grade handling (e.g., GPA, numeric scores).
- Introduce unit tests for validation helpers and menu functions.
- Replace JSON persistence with a database layer if requirements grow.
