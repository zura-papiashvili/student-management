class Person:
    """Represents a generic person in the system."""

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        cleaned_name = value.strip()
        if not cleaned_name:
            raise ValueError("Name cannot be empty.")
        self._name = cleaned_name

    def describe(self) -> str:
        return f"Name: {self.name}"


class Student(Person):
    """Represents a student with roll number and grade."""

    _allowed_grades = tuple("ABCDEF")

    def __init__(self, name: str, roll_number: int, grade: str):
        super().__init__(name)
        self.roll_number = roll_number
        self.grade = grade

    @property
    def roll_number(self) -> int:
        return self._roll_number

    @roll_number.setter
    def roll_number(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Roll number must be an integer.")
        if value <= 0:
            raise ValueError("Roll number must be a positive integer.")
        self._roll_number = value

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Grade must be a string.")
        cleaned_grade = value.strip().upper()
        if len(cleaned_grade) != 1 or cleaned_grade not in self._allowed_grades:
            allowed_display = ", ".join(self._allowed_grades)
            raise ValueError(f"Grade must be one of: {allowed_display}.")
        self._grade = cleaned_grade

    @classmethod
    def allowed_grades(cls) -> tuple:
        return cls._allowed_grades

    def describe(self) -> str:
        # Demonstrates polymorphism compared to Person.describe
        return f"{super().describe()}, Roll Number: {self.roll_number}, Grade: {self.grade}"

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return (
            "Student("
            f"name='{self.name}', roll_number={self.roll_number}, grade='{self.grade}'"
            ")"
        )

